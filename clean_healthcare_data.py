import pandas as pd
import re
import os

# Load the dataset
file_path = 'healthcare_dataset.csv'

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

df = pd.read_csv(file_path)
print("✅ Data loaded successfully from healthcare_dataset.csv\n")

# Show the first few rows
print("🔍 Preview of original data:")
print(df.head(), "\n")

# Check for 'Name' column
if 'Name' not in df.columns:
    print("❌ The dataset does not contain a 'Name' column.")
    exit()

# Normalize names
def normalize_name(name):
    name = name.lower()
    name = re.sub(r'[^a-z\s]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

df['Normalized_Name'] = df['Name'].astype(str).apply(normalize_name)
print("✅ Names normalized.\n")

# Show duplicates based on normalized names
duplicates = df[df.duplicated('Normalized_Name', keep=False)]

if not duplicates.empty:
    print("⚠️ Potential duplicate records found:")
    print(duplicates[['Name', 'Normalized_Name']])
else:
    print("✅ No potential duplicate names found.\n")

# Save cleaned data
output_file = 'cleaned_healthcare_detailed_data.csv'
df.to_csv(output_file, index=False)
print(f"📁 Cleaned data saved to: {output_file}")
