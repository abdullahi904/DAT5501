import pandas as pd
import sys

def print_menu(items, header=None):
    if header:
        print(header)
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

def prompt_index(max_index, prompt="Enter number (or 'q' to quit): "):
    while True:
        s = input(prompt).strip().lower()
        if s in ("q", "quit", "exit"):
            return None
        if s.isdigit():
            idx = int(s)
            if 1 <= idx <= max_index:
                return idx - 1
        print(f"Please enter a number between 1 and {max_index}, or 'q' to quit.")

def main():
    csv_path = "books_archive.csv"
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        sys.exit(1)

    required_cols = ["Topic", "Subtopic", "Title", "Author"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print(f"Error: Missing columns in CSV: {', '.join(missing)}")
        sys.exit(1)

    # Clean up whitespace
    for c in required_cols:
        df[c] = df[c].map(lambda x: x.strip() if isinstance(x, str) else x)

    topics = sorted([t for t in df["Topic"].dropna().unique() if str(t).strip()], key=lambda x: str(x).lower())
    if not topics:
        print("No topics found in the CSV.")
        sys.exit(1)

    print("Welcome to the Book Recommender (pandas).")
    print("Pick a topic, then a subtopic to see recommended books.\n")

    while True:
        print_menu(topics, header="Topics:")
        t_idx = prompt_index(len(topics), prompt="Select a topic number (or 'q' to quit): ")
        if t_idx is None:
            print("Goodbye!")
            return
        topic = topics[t_idx]

        df_t = df[df["Topic"] == topic]
        subtopics = sorted([s for s in df_t["Subtopic"].dropna().unique() if str(s).strip()], key=lambda x: str(x).lower())
        if not subtopics:
            print("\nNo subtopics found for this topic. Please choose another topic.\n")
            continue

        while True:
            print()
            print_menu(subtopics, header=f"Subtopics for '{topic}':")
            s_idx = prompt_index(len(subtopics), prompt="Select a subtopic number (or 'q' to quit): ")
            if s_idx is None:
                print("Goodbye!")
                return
            subtopic = subtopics[s_idx]

            df_s = df_t[df_t["Subtopic"] == subtopic]
            books = df_s[["Title", "Author"]].values.tolist()

            print()
            print(f"Recommended books for '{topic}' > '{subtopic}':")
            for i, (title, author) in enumerate(books, start=1):
                title_str = title if pd.notna(title) and str(title).strip() else "Untitled"
                author_str = author if pd.notna(author) and str(author).strip() else ""
                print(f"{i}. {title_str}" + (f" — {author_str}" if author_str else ""))

            print()
            next_action = input("Press Enter to pick another subtopic, 't' to choose a new topic, or 'q' to quit: ").strip().lower()
            if next_action in ("q", "quit", "exit"):
                print("Goodbye!")
                return
            if next_action == "t":
                print()
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")