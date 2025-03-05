import pandas as pd

print(" Script is running...")

#  File path (Ensure CSV is correct!)
csv_file = "C:/Users/brian/OneDrive/Documents/california-population-and-housing-estimates-dashboard-2020-2024-metadata.csv"

try:
    # Load the dataset
    df = pd.read_csv(csv_file)

    print(" Data loaded successfully!\n")

    #  Step 1: Rename columns
    df.columns = ['Category', 'Details']

    #  Step 2: Drop duplicate rows
    df = df.drop_duplicates()

    #  Step 3: Remove rows where 'Details' is empty (NaN)
    df = df.dropna(subset=['Details'])

    #  Step 4: Strip whitespace
    df['Category'] = df['Category'].str.strip()
    df['Details'] = df['Details'].str.strip()

    #  Step 5: Save cleaned data to a new CSV file
    cleaned_csv_file = "C:/Users/brian/OneDrive/Documents/cleaned_housing_data.csv"
    df.to_csv(cleaned_csv_file, index=False)

    print(f" Cleaned data saved to: {cleaned_csv_file}")

except FileNotFoundError:
    print(" ERROR: CSV file not found! Check the file path and try again.")
except pd.errors.EmptyDataError:
    print(" ERROR: CSV file is empty!")
except Exception as e:
    print(f" Unexpected ERROR: {e}")
