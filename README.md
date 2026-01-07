# Kriteria 1 - Eksperimen & Preprocessing (Credit Scoring)

Repo ini berisi notebook eksperimen **sesuai Template Eksperimen MSML** (struktur 1–5, dan tahap terakhir adalah **5. Data Preprocessing**).

## Dataset yang digunakan
Dataset: **Credit Scoring (synthetic)** (format CSV)

- **Sumber data (tautan):**
  - GitHub (view): https://github.com/eko-andri-prasetyo/Eksperimen_SML_EkoAndriPrasetyo/blob/main/creditscoring_raw/creditscoring_raw.csv
  - GitHub (raw): https://raw.githubusercontent.com/eko-andri-prasetyo/Eksperimen_SML_EkoAndriPrasetyo/main/creditscoring_raw/creditscoring_raw.csv
- **Lokasi file raw di repo:** `creditscoring_raw/creditscoring_raw.csv`
- **Target:** `target` (0 = tidak default, 1 = default)

> Catatan: Dataset ini bersifat **synthetic** untuk kebutuhan latihan/proyek dan disediakan di repo agar reviewer dapat mengaksesnya dengan mudah.

## Notebook yang diperiksa reviewer
- `notebook.ipynb` (root)
- `preprocessing/Eksperimen_EkoAndriPrasetyo.ipynb`

## Output preprocessing
- Output folder: `preprocessing/creditscoring_preprocessing/`
- Output file  : `preprocessing/creditscoring_preprocessing/creditscoring_preprocessed.csv`

## Jalankan otomatisasi preprocessing
```bash
python preprocessing/automate_EkoAndriPrasetyo.py \
  --input creditscoring_raw/creditscoring_raw.csv \
  --output preprocessing/creditscoring_preprocessing/creditscoring_preprocessed.csv
```
