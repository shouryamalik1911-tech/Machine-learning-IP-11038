import pandas as pd

file_path = "Dataset.csv"
df = pd.read_csv(file_path)

# Look for rows that have very specific 'tech' inputs but are labeled as CRM or non-tech
tech_mask = (df['Interested subjects'] == 'programming') & \
            (df['interested career area '].str.contains('developer', case=False)) & \
            (df['coding skills rating'] > 8)

subset = df[tech_mask]
print(f"Total rows with high tech profile: {len(subset)}")
print("\nCareer labels for these tech profiles:")
print(subset['Suggested Job Role'].value_counts())