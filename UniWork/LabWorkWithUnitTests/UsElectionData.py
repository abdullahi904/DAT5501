import pandas as pd, numpy as np, matplotlib.pyplot as plt

path = r"C:\Users\agedow001\Downloads\US-2016-primary (3).csv"
candidate = "Donald Trump"

# Robust read (auto-detect delimiter) and normalize headers
df = pd.read_csv(path, sep=None, engine="python", encoding="utf-8-sig")
df.columns = (df.columns
              .str.replace("\ufeff","", regex=False)  # remove BOM if present
              .str.strip()
              .str.lower())


# Locate required columns
def pick(names):
    for n in names:
        if n in df.columns: return n
    raise KeyError(f"Missing columns {names}. Got: {df.columns.tolist()}")

state_col     = pick(["state","state_name"])
candidate_col = pick(["candidate","cand_name"])
votes_col     = pick(["votes","total_votes"])
party_col     = next((c for c in ["party","party_simplified"] if c in df.columns), None)

# clean
df[votes_col] = pd.to_numeric(df[votes_col], errors="coerce")
df = df.dropna(subset=[state_col, candidate_col, votes_col])

# Candidate's party
party = (df.loc[df[candidate_col]==candidate, party_col].mode().iat[0]
         if party_col and not df.loc[df[candidate_col]==candidate, party_col].empty else None)

# Candidate votes per state
cand = (df[df[candidate_col]==candidate]
        .groupby(state_col, as_index=False)[votes_col].sum()
        .rename(columns={votes_col:"cand"}))

# Denominator: party totals per state (or all votes)
base = df if party is None else df[df[party_col]==party]
tot  = base.groupby(state_col, as_index=False)[votes_col].sum().rename(columns={votes_col:"tot"})

# Fraction and Histogram
res = cand.merge(tot, on=state_col)
res["fraction"] = res["cand"] / res["tot"]

print(f"{candidate} | party: {party or 'unknown/all'}")
print(res.sort_values("fraction", ascending=False)[[state_col,"fraction"]].head(10).to_string(index=False))

plt.figure(figsize=(8,5))
plt.hist(res["fraction"], bins=15, edgecolor="k", alpha=0.8)
plt.xlabel("Fraction of votes in state"); plt.ylabel("Number of states")
plt.title(f"State vote share for {candidate}")
plt.tight_layout(); plt.show()