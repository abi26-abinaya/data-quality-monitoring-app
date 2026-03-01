import pandas as pd

def run_quality_checks(file_path):
    df = pd.read_csv(file_path)

    # Missing values
    missing = df.isnull().sum()

    # Duplicates
    duplicates = df.duplicated().sum()

    # Invalid age rule
    invalid_age = df[(df['age'] < 0) | (df['age'] > 100)]

    # Cleaning
    df = df.drop_duplicates()
    df['name'] = df['name'].fillna("Unknown")
    df['age'] = df['age'].fillna(df['age'].mean())
    df.loc[df['age'] > 100, 'age'] = df['age'].median()

    # Quality Score
    total_cells = df.size
    missing_cells = df.isnull().sum().sum()
    quality_score = ((total_cells - missing_cells) / total_cells) * 100

    return df, missing, duplicates, invalid_age, quality_score