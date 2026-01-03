"""Automasi preprocessing (Kriteria 1 - Skilled/Advance)

Input : creditscoring_raw/creditscoring_raw.csv
Output: preprocessing/creditscoring_preprocessing/creditscoring_preprocessed.csv

Label : target
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.impute import SimpleImputer

TARGET_COL = "target"
NUM_COLS = ['age', 'monthly_income', 'loan_amount', 'tenure_months', 'num_credit_lines', 'has_previous_default']
CAT_COLS = ['job_type', 'education_level', 'city', 'marital_status']

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    df = pd.read_csv(args.input)

    required = NUM_COLS + CAT_COLS + [TARGET_COL]
    missing_cols = [c for c in required if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Kolom wajib tidak ditemukan: {missing_cols}. Kolom tersedia: {list(df.columns)}")

    df[NUM_COLS] = SimpleImputer(strategy="median").fit_transform(df[NUM_COLS])
    df[CAT_COLS] = SimpleImputer(strategy="most_frequent").fit_transform(df[CAT_COLS])
    df[TARGET_COL] = df[TARGET_COL].astype(int)
    for c in CAT_COLS:
        df[c] = df[c].astype(str)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)

    print("Sukses preprocessing!")
    print(f"- Input:  {args.input} rows={len(df)}")
    print(f"- Output: {args.output} cols={len(df.columns)}")

if __name__ == "__main__":
    main()
