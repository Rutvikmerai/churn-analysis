Customer Churn Analysis

Goal. Analyze customer churn for a retail/banking dataset, identify key churn drivers, and build a predictive model to flag at-risk customers. Deliverables include a clean dataset, notebooks/scripts, and a BI dashboard.

Business Questions

What is the overall churn rate and how is it trending?

Which factors (e.g., tenure, credit score, product usage, satisfaction) most strongly relate to churn?

Which customer segments have the highest churn risk?

Can we predict churn with enough accuracy to target retention offers?

Data

Source: Kaggle – https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn

Raw file in repo structure: data/raw/Customer-Churn-Records.csv

Target (label): If your dataset includes a column like Exited or Churn, that is the churn indicator (1 = churned, 0 = stayed).
If it’s named differently, define your churn logic here.

Tech Stack

Python (pandas, numpy, scikit-learn, matplotlib), Jupyter

MySQL (optional: for storing/serving data)

Power BI (dashboard)

Git/GitHub (version control)

Project Structure
churn_project/
├─ data/
│  ├─ raw/               # original CSVs (not tracked by git)
│  └─ clean/             # cleaned datasets for analysis/BI
├─ python/               # .py scripts (ETL, utilities)
│  └─ ingest_and_clean.py
├─ notebooks/            # EDA & modeling notebooks
├─ sql/                  # DDL + load scripts for MySQL
│  ├─ create_customer_churn_raw.sql
│  ├─ load_customer_churn_raw.sql
│  └─ column_name_mapping.csv
├─ powerbi/              # PBIX files & data sources
├─ reports/              # exported reports
├─ requirements.txt
├─ .gitignore
└─ README.md

Setup & Run
# 1) Create and activate a virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Clean the raw data
python python/ingest_and_clean.py

# 4) Start Jupyter for EDA
jupyter lab

Optional: Load to MySQL

Create the table:

SOURCE sql/create_customer_churn_raw.sql;


Edit sql/load_customer_churn_raw.sql and set the absolute file path to your CSV.

Load the data:

SOURCE sql/load_customer_churn_raw.sql;

Analysis Plan (Roadmap)

01_eda.ipynb: data overview, missing values, distributions, correlations.

02_modeling.ipynb: baselines (LogReg, Tree/RandomForest), metrics (ROC/AUC, PR AUC, recall@k), feature importance/SHAP.

03_segmentation.ipynb: RFM/tenure-based segments and risk buckets.

Power BI: overview KPIs, segment drilldowns, driver visuals.

Author

Rutvik Mukeshbhai Merai
Tools: Python, MySQL, Power BI, Excel, Git/GitHub, Jupyter, Kaggle