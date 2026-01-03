# Kriteria 1 - Eksperimen & Preprocessing

Struktur folder mengikuti rubrik Dicoding.

## Jalankan preprocessing otomatis
```bash
python preprocessing/automate_EkoAndriPrasetyo.py   --input creditscoring_raw/creditscoring_raw.csv   --output preprocessing/creditscoring_preprocessing/credit_scoring_preprocessed.csv
```

## (Opsional Advance) Workflow GitHub Actions
Jika ingin poin Advance, buat workflow yang menjalankan script preprocessing dan meng-commit/menyimpan output terbaru.
