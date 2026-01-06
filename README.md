# Kriteria 1 - Eksperimen & Preprocessing (creditscoring)

## Dataset
- **Sumber data (link):** https://github.com/eko-andri-prasetyo/Eksperimen_SML_EkoAndriPrasetyo/blob/main/creditscoring_raw/creditscoring_raw.csv
- **File raw:** `creditscoring_raw/creditscoring_raw.csv`
- **Catatan:** Dataset bersifat **synthetic/dibuat untuk kebutuhan latihan submission**.

## Notebook Eksperimen (mengikuti Template Dicoding)
- `notebook.ipynb` (struktur 1–5 sesuai Template Eksperimen MSML)

## Folder & File
- Raw folder: `creditscoring_raw/`
- Raw file  : `creditscoring_raw/creditscoring_raw.csv`

- Output folder: `preprocessing/creditscoring_preprocessing/`
- Output file  : `preprocessing/creditscoring_preprocessing/creditscoring_preprocessed.csv`

## Jalankan otomatisasi preprocessing
```bash
python preprocessing/automate_EkoAndriPrasetyo.py \
  --input creditscoring_raw/creditscoring_raw.csv \
  --output preprocessing/creditscoring_preprocessing/creditscoring_preprocessed.csv
```
