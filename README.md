
# Datasets Used
- Telecom Churn Data - 

# Folder Structure
```text
churn_analysis/
├── data/
│   ├── raw/                 # Original CSVs (gitignored)
│   └── processed/           # Cleaned feature tables
├── pipeline/
│   ├── feature_pipeline.py  # Ingestion and feature engineering
│   └── config.yaml          # All parameters in one place
├── notebooks/
│   ├── 01_descriptive_baseline.ipynb
│   ├── 02_survival_analysis.ipynb
│   ├── 03_shap_attribution.ipynb
│   ├── 04_uplift_modelling.ipynb
│   ├── 05_statistical_validation.ipynb
│   └── 06_financial_impact.ipynb
├── api/
│   ├── main.py              # FastAPI app
│   └── schemas.py           # Pydantic request/response models
├── monitoring/
│   ├── drift_monitor.py
│   └── reports/
├── reports/
│   ├── templates/           # Jinja2 HTML templates
│   └── generate_report.py
├── tests/
│   ├── test_pipeline.py
│   └── test_api.py
├── mlruns/              # MLflow tracking (local)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.yaml
├── Makefile             # One command to run everything
├── .github/workflows/ci.yml
└── README.md
```
