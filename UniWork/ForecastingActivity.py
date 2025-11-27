import pandas as pd, numpy as np, matplotlib.pyplot as plt

csv_path = r"C:\Users\agedow001\Downloads\gdp-per-capita-maddison-project-database.csv"
country_name = "United States"

df = pd.read_csv(csv_path)

# minimal column detection
country_col = [c for c in df.columns if c.lower() in ("entity","country","location")][0]
year_col    = [c for c in df.columns if c.lower()=="year"][0]
gdp_col     = [c for c in df.columns if ("gdp" in c.lower() and "capita" in c.lower())][0]

d = df[df[country_col]==country_name][[year_col,gdp_col]].dropna().sort_values(year_col)
years, y = d[year_col].to_numpy(), d[gdp_col].to_numpy()

h = min(10, len(years)-1)                       # hold out last 10 (at least 1 train point left)
tr_x, te_x = years[:-h], years[-h:]
tr_y, te_y = y[:-h], y[-h:]
mu, s = tr_x.mean(), tr_x.std() or 1.0          # scale to reduce numeric issues
Xtr, Xte = (tr_x-mu)/s, (te_x-mu)/s

results, preds = [], {}
for deg in range(1,10):
    p = np.polyfit(Xtr, tr_y, deg)
    yhat = np.polyval(p, Xte)
    mae = np.mean(np.abs(te_y - yhat))
    rmse = np.sqrt(np.mean((te_y - yhat)**2))
    results.append((deg, mae, rmse))
    preds[deg] = yhat

print(f"Country: {country_name}")
print("Degree | MAE | RMSE")
for deg, mae, rmse in results:
    print(f"{deg:6} | {mae:.3f} | {rmse:.3f}")
best = min(results, key=lambda r: r[2])
print(f"Best degree by RMSE: {best[0]} (RMSE={best[2]:.3f}, MAE={best[1]:.3f})")

plt.figure(figsize=(10,6))
plt.plot(tr_x, tr_y, label="Train")
plt.plot(te_x, te_y, label="Test (actual)")
for deg, yhat in preds.items():
    plt.plot(te_x, yhat, label=f"Deg {deg}")
plt.title(f"GDP per capita forecast: {country_name}")
plt.xlabel("Year"); plt.ylabel(gdp_col); plt.legend(ncol=2, fontsize=8); plt.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()

# --- Model testing: reduced chi^2 and BIC on training fit ---
n = len(tr_y)
deg_list, redchi2, bic = [], [], []
for deg in range(1, 10):
    p = np.polyfit(Xtr, tr_y, deg)
    fit = np.polyval(p, Xtr)
    rss = np.sum((tr_y - fit)**2)
    rss = max(rss, 1e-12)              # guard for exact fit
    p_params = deg + 1                  # coefficients incl. intercept
    dof = max(n - p_params, 1)          # avoid zero/negative dof for high deg
    redchi2.append(rss / dof)
    bic.append(n * np.log(rss / n) + p_params * np.log(n))
    deg_list.append(deg)

print("\nModel testing (training set):")
for d, rc2, b in zip(deg_list, redchi2, bic):
    print(f"deg={d}: reduced chi^2={rc2:.3f}, BIC={b:.3f}")
best_bic_deg = deg_list[int(np.argmin(bic))]
best_rc2_deg = deg_list[int(np.argmin(redchi2))]
print(f"Best by BIC: degree {best_bic_deg}")
print(f"Best by reduced chi^2: degree {best_rc2_deg}")

plt.figure(figsize=(9,4))
plt.plot(deg_list, redchi2, 'o-', label='reduced chi^2')
plt.plot(deg_list, bic, 'o-', label='BIC')
plt.xlabel('Polynomial degree'); plt.grid(True, alpha=0.3)
plt.title('Model testing metrics (training fit)')
plt.legend(); plt.tight_layout(); plt.show()