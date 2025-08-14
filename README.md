# Customer Churn Analysis Project

**Goal**: Analyze customer churn, build segmentation and a predictive churn model, and ship a dashboard.

## Dataset
- Source: Kaggle (CSV loaded as `Customer-Churn-Records.csv`).
- Rows: 10000
- Columns: 18
- Encoding used on load: default
- Potential churn field(s): Not detected automatically

## Repo Structure
```text
churn_project/
├─ data/
│  ├─ raw/               # put original CSVs here
│  └─ clean/             # outputs from cleaning
├─ python/               # .py analysis/ETL scripts
├─ notebooks/            # Jupyter notebooks (EDA, modeling)
├─ sql/                  # DDL + load scripts for MySQL
├─ powerbi/              # PBIX files / data sources
├─ reports/              # exports (PDF, PPTX)
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## Quickstart
```bash
# 1) Create & activate a virtual env (example for Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Launch Jupyter for EDA
jupyter lab
```

## Load to MySQL
1. Create the table:
   ```sql
   SOURCE sql/create_customer_churn_raw.sql;
   ```
2. Load the CSV (edit the absolute path first):
   ```sql
   SOURCE sql/load_customer_churn_raw.sql;
   ```
3. Column mapping for sanitized names is in: `sql/column_name_mapping.csv`

## Next Steps
- Run `python/ingest_and_clean.py` to produce a clean CSV in `data/clean/`.
- Start EDA in `notebooks/01_eda.ipynb` (create in Jupyter).
- Build features & model in new notebooks (02_modeling.ipynb).
- Publish a Power BI dashboard using the clean CSV or a MySQL view.