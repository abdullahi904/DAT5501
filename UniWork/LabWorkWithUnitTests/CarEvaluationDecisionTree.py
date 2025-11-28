# Decision tree for UCI Car Evaluation (predicts the 'class' label)
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import classification_report, confusion_matrix

# 1) Load dataset (UCI id=19: Car Evaluation)
car = fetch_ucirepo(id=19)
X = car.data.features.copy()          # features: buying, maint, doors, persons, lug_boot, safety
y = car.data.targets["class"].copy()  # target: unacc, acc, good, vgood

# 2) Define ordered categories for ordinal encoding (matches X column order)
cat_orders = {
    "buying":  ["low", "med", "high", "vhigh"],
    "maint":   ["low", "med", "high", "vhigh"],
    "doors":   ["2", "3", "4", "5more"],
    "persons": ["2", "4", "more"],
    "lug_boot":["small", "med", "big"],
    "safety":  ["low", "med", "high"]
}
categories = [cat_orders[col] for col in X.columns]  # ensure order aligns with X.columns

# 3) Train/test split (stratify keeps class proportions)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4) Pipeline: encode categorical features -> decision tree
pipe = Pipeline([
    ("enc", OrdinalEncoder(categories=categories)),
    ("clf", DecisionTreeClassifier(max_depth=4, random_state=42))  # tweak max_depth if needed
])

# 5) Train and predict
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

# 6) Evaluate (precision/recall per class + averages)
print("\nClassification report (precision/recall/F1):")
print(classification_report(y_test, y_pred, digits=3))

print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))

# 7) Show the learned tree rules
tree_text = export_text(pipe.named_steps["clf"], feature_names=list(X.columns))
print("\nDecision tree rules:")
print(tree_text)

# 8) Example prediction for a sample car
sample = pd.DataFrame([{
    "buying": "med", "maint": "med", "doors": "4",
    "persons": "4", "lug_boot": "big", "safety": "high"
}])
print("\nSample car prediction:", pipe.predict(sample)[0])