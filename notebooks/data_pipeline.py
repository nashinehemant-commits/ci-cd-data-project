# Production-ready pipeline (no Databricks %run)

import pandas as pd
import os


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path)


def clean_data(df):
    df = df.dropna()
    df['amount'] = df['amount'].astype(float)
    return df


def save_data(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def run_pipeline(input_path, output_path):
    df = load_data(input_path)
    df = clean_data(df)
    save_data(df, output_path)


# Allow local execution
if __name__ == "__main__":
    run_pipeline("data/sample.csv", "data/output.csv")