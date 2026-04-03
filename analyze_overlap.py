import pandas as pd

file_path = "Dataset.csv"
df = pd.read_csv(file_path)

target_col = 'Suggested Job Role'
print("Class Distribution:")
print(df[target_col].value_counts())

# Check how tech-related features correlate with target
tech_features = ['interested career area ', 'Interested subjects', 'workshops', 'certifications']
for feat in tech_features:
    print(f"\nTop 5 {feat} for 'CRM Technical Developer':")
    print(df[df[target_col] == 'CRM Technical Developer'][feat].value_counts().head(5))
    
    print(f"\nTop 5 {feat} for 'Software Developer':")
    print(df[df[target_col] == 'Software Developer'][feat].value_counts().head(5))