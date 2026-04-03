import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

file_path = "Dataset.csv"
df = pd.read_csv(file_path)

# Encode all categorical columns
le_dict = {}
for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        le_dict[col] = le if col == 'Suggested Job Role' else None

X = df.drop('Suggested Job Role', axis=1)
y = df['Suggested Job Role']

# Feature Importance
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

importances = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print("Feature Importances:")
print(importances)

# Correlation with target (Spearman to handle ordinal/categorical rank)
corr = df.corr(method='spearman')['Suggested Job Role'].sort_values(ascending=False)
print("\nCorrelation with Suggested Job Role:")
print(corr)