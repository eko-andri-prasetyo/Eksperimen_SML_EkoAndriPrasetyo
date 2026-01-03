"""Automasi preprocessing (Kriteria 1 - Skilled/Advance)

Cara pakai:
  python preprocessing/automate_EkoAndriPrasetyo.py \
      --input creditscoring_raw/credit_scoring_raw.csv \
      --output preprocessing/creditscoring_preprocessing/credit_scoring_preprocessed.csv

Catatan:
- Ganti nama file/dataset sesuai dataset aslimu.
- Target/label diasumsikan bernama: target
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer


@dataclass
class PreprocessResult:
    X: pd.DataFrame
    y: pd.Series
    feature_names: List[str]


def build_preprocess_pipeline(cat_cols: List[str], num_cols: List[str]) -> ColumnTransformer:
    numeric = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
    ])

    categorical = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric, num_cols),
            ("cat", categorical, cat_cols),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )
    return preprocessor


def preprocess(df: pd.DataFrame, target_col: str = "target") -> PreprocessResult:
    if target_col not in df.columns:
        raise ValueError(f"Kolom target '{target_col}' tidak ditemukan. Kolom tersedia: {list(df.columns)}")

    y = df[target_col].astype(int)
    X_raw = df.drop(columns=[target_col])

    cat_cols = [c for c in X_raw.columns if X_raw[c].dtype == "object"]
    num_cols = [c for c in X_raw.columns if c not in cat_cols]

    pre = build_preprocess_pipeline(cat_cols, num_cols)
    X_np = pre.fit_transform(X_raw)

    feature_names = list(pre.get_feature_names_out())
    X = pd.DataFrame(X_np, columns=feature_names)

    return PreprocessResult(X=X, y=y, feature_names=feature_names)


def save_preprocessed(result: PreprocessResult, output_csv: Path) -> None:
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    out = result.X.copy()
    out["target"] = result.y.values
    out.to_csv(output_csv, index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path CSV dataset raw")
    parser.add_argument("--output", required=True, help="Path CSV output dataset hasil preprocessing")
    parser.add_argument("--target-col", default="target", help="Nama kolom target/label")
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    result = preprocess(df, target_col=args.target_col)
    save_preprocessed(result, Path(args.output))

    print("Sukses!")
    print(f"- Input rows: {len(df)}")
    print(f"- Output shape: {result.X.shape} (+ target)")
    print(f"- Output: {args.output}")


if __name__ == "__main__":
    main()
