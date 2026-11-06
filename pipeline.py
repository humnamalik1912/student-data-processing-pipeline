
import pandas as pd


# 1. Load data from CSV
def load(file_path="students_messy.csv"):
    df = pd.read_csv(file_path)
    return df


# 2. Clean the dataset
def clean(df):
    df = df.copy()

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove extra spaces from text values
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Replace empty strings with missing values
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate records
    df = df.drop_duplicates()

    # Reset row indexes
    df = df.reset_index(drop=True)

    return df


# 3. Add new features
def add_features(df):
    df = df.copy()

    # Create full name if first and last names exist
    if {"first_name", "last_name"}.issubset(df.columns):
        df["full_name"] = (
            df["first_name"].fillna("").astype(str)
            + " "
            + df["last_name"].fillna("").astype(str)
        ).str.strip()

    # Create age group if age column exists
    if "age" in df.columns:
        age = pd.to_numeric(df["age"], errors="coerce")

        df["age_group"] = "Adult"
        df.loc[age < 18, "age_group"] = "Minor"
        df.loc[age.isna(), "age_group"] = "Unknown"

    # Add email domain if email column exists
    if "email" in df.columns:
        df["email_domain"] = (
            df["email"].str.extract(r"@(.+)$")[0]
        )

    # Add missing value indicator
    df["has_missing_values"] = df.isna().any(axis=1)

    return df


# Run the complete pipeline
if __name__ == "__main__":

    data = load()

    cleaned_data = clean(data)

    processed_data = add_features(cleaned_data)

    processed_data.to_csv("students_clean.csv", index=False)

    print("Pipeline executed successfully!")
    print("\nProcessed Data:")
    print(processed_data)

    print("\nOutput saved as students_clean.csv")
