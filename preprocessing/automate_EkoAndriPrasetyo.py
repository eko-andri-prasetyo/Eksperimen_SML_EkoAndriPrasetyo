"""Automasi preprocessing (Kriteria 1)

Input : creditscoring_raw/creditscoring_raw.csv
Output: preprocessing/creditscoring_preprocessing/creditscoring_preprocessed.csv

Catatan:
- Preprocessing diselesaikan di tahap ini (imputasi + encoding) agar modelling.py (Kriteria 2)
  tidak perlu melakukan preprocessing lagi.
- Target/label: target (0/1)
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


TARGET_COL = "target"

NUM_COLS = [
    "age",
    "monthly_income",
    "loan_amount",
    "tenure_months",
    "num_credit_lines",
    "has_previous_default",
]

CAT_COLS = [
    "job_type",
    "education_level",
    "city",
    "marital_status",
]


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # validasi kolom
    required = NUM_COLS + CAT_COLS + [TARGET_COL]
    missing_cols = [c for c in required if c not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Kolom wajib tidak ditemukan: {missing_cols}. "
            f"Kolom tersedia: {list(df.columns)}"
        )

    out = df.drop_duplicates().copy()

    # imputasi numerik -> median
    for c in NUM_COLS:
        out[c] = pd.to_numeric(out[c], errors="coerce")
        out[c] = out[c].fillna(out[c].median())

    # imputasi kategorikal -> modus
    for c in CAT_COLS:
        out[c] = out[c].astype("string")
        mode_val = out[c].mode(dropna=True)
        out[c] = out[c].fillna(mode_val.iloc[0] if len(mode_val) else "")

    # target -> int
    out[TARGET_COL] = pd.to_numeric(out[TARGET_COL], errors="coerce").fillna(0).astype(int)

    # one-hot encoding agar siap training
    X = out[NUM_COLS + CAT_COLS]
    y = out[TARGET_COL]
    X_enc = pd.get_dummies(X, columns=CAT_COLS, drop_first=False)

    final_df = pd.concat([X_enc, y], axis=1)
    return final_df


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Path ke CSV raw")
    p.add_argument("--output", required=True, help="Path output CSV preprocessed")
    args = p.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(in_path)
    df_out = preprocess(df)
    df_out.to_csv(out_path, index=False)

    print("Sukses preprocessing!")
    print(f"- Input : {in_path} rows={len(df)} cols={len(df.columns)}")
    print(f"- Output: {out_path} rows={len(df_out)} cols={len(df_out.columns)}")


if __name__ == "__main__":
    main()
