
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

# Analysis
## Descriptive - Baseline
### Key Findings
- Customers on month-to-month contracts exhibit the highest churn rate (over 40%), making contract type the strongest structural indicator for churn
- Churn is concentrated on the first six months of the customers's lifecycle, suggesting onboarding and early customer engagement would show retention opportuntiies
- Customers that chose Fiber Optics as their internet service type shows higher churn rate indicating - pricing strategies, dissatisfaction with the service or misalignment in expectations


## Survival Analysis
- Long-term contracts were the strongest protective factor against churn
- Higher monthly charges increased churn risk, indicating price sensitivity
- Greater product adoption significantly reduced churn risk

# Resources
- What is Churn? by IBM - https://www.ibm.com/think/topics/customer-churn
