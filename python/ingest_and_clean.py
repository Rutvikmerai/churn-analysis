import pandas as pd
from pathlib import Path

RAW_CSV = Path("/mnt/data/churn_project/data/raw/Customer-Churn-Records.csv")
CLEAN_CSV = Path("/mnt/data/churn_project/data/clean/customer_churn_clean.csv")

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Strip, lower, replace spaces with underscores
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.replace("\s+", "_", regex=True)
        .str.replace(r"[^0-9a-zA-Z_]", "", regex=True)
        .str.lower()
    )
    return df

def coerce_types(df: pd.DataFrame) -> pd.DataFrame:
    # Example coercions: yes/no -> 1/0; 'TotalCharges' to numeric if present, etc.
    yes_no_cols = [c for c in df.columns if any(x in c for x in ["churn", "partner", "dependents", "paperless", "phoneservice"])]
    for c in yes_no_cols:
        try:
            df[c] = df[c].astype(str).str.strip().str.lower().map({"yes": 1, "no": 0}).astype("Int64")
        except Exception:
            pass

    # Try to parse dates
    for c in df.columns:
        if any(k in c for k in ["date", "signup", "tenure_start"]):
            try:
                df[c] = pd.to_datetime(df[c], errors="ignore")
            except Exception:
                pass

    # Numeric coercion example
    for c in df.columns:
        if df[c].dtype == "object":
            # try convert to numeric where appropriate
            num = pd.to_numeric(df[c], errors="ignore")
            if str(num.dtype) != "object":
                df[c] = num
    return df

def clean_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Remove obvious whitespace
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].astype(str).str.strip()
    # Replace empty strings with NA
    df = df.replace({"": pd.NA, "NA": pd.NA, "NaN": pd.NA})
    return df

def main():
    df = pd.read_csv(RAW_CSV)
    df = clean_values(df)
    df = standardize_columns(df)
    df = coerce_types(df)
    # Optional: drop duplicate rows
    df = df.drop_duplicates()
    CLEAN_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_CSV, index=False)
    print(f"Saved cleaned CSV to: {CLEAN_CSV}. Shape: {df.shape}")

if __name__ == "__main__":
    main()