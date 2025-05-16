import pandas as pd

# Load dataset
df = pd.read_csv('Shark Tank India Dataset.csv')

# Step 1: Clean Data
# Remove rows where deal_amount is missing (no deal was made)
df_cleaned = df.dropna(subset=['deal_amount'])

# Convert deal_amount to numeric
df_cleaned['deal_amount'] = (
    df_cleaned['deal_amount']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.replace('₹', '', regex=False)
    .astype(float)
)

# Also clean pitcher_ask_amount if needed
df_cleaned['pitcher_ask_amount'] = (
    df_cleaned['pitcher_ask_amount']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.replace('₹', '', regex=False)
    .astype(float)
)

# Step 2: Select required columns
columns_to_keep = [
    'brand_name',
    'idea',
    'deal',
    'pitcher_ask_amount',
    'ask_amount',       # Only include if it exists
    'deal_amount',
    'deal_ammount'      # Only include if it exists (or correct typo)
]

# Filter only columns that exist in the DataFrame
columns_existing = [col for col in columns_to_keep if col in df_cleaned.columns]

# Select them
df_selected = df_cleaned[columns_existing]

# Step 3: Save to CSV
df_selected.to_csv('Cleaned_Industry_Trends.csv', index=False)

# Optional: Preview the cleaned data
print(df_selected.head())
 # type: ignore