
import pandas as pd
import os
import duckdb
import yaml
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,         # configuring logging system
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_config(path='pipeline/config.yaml'):
    with open(path) as f:
        return yaml.safe_load(f)
    
def load_telco(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Data Cleaning: TotalCharges column has spaces instead of nulls
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
    df['TotalCharges'].fillna(df['MonthlyCharges'], inplace=True)

    #Encoding bindary churn
    df['Churn_binary'] = (df['Churn'] == 'Yes').astype(int)

    # Encoding binary - senior citizen
    df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)

    logger.info(f"Loaded {len(df):,} Telco records. Churn rate: {df['Churn_binary'].mean():.1%}")

    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Calculating revenue per month of tenure - value density
    df['revenue_per_tenure'] = df['TotalCharges'] / df['tenure'].clip(lower=1)

    # Check if customer is on a long term contract
    df['is_long_term'] = (df['Contract'] != 'Month-to-month').astype(int)

    # Service count - breadth of product usage
    service_cols = ['PhoneService','MultipleLines','InternetService',
                    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                    'TechSupport', 'StreamingTV', 'StreamingMovies']
    df['service_count'] = df[service_cols].apply(
        lambda row: sum(1 for v in row if v not in ['No','No phone service','No internet service']),
                        axis = 1)

    # Calculating tenure bands for Cohort Analysis
    df['tenure_band'] = pd.cut(df['tenure'],
                               bins = [0,3,6,12,24,72],
                               labels=['0-3m','3-6m','6-12m','12-24m','24m+'])
    return df

def run_pipeline():
    config = load_config()
    df = load_telco(config['data']['telco_path'])
    df = engineer_features(df)
    output = config['data']['processed_path']
    Path(output).parent.mkdir(parents = True, exist_ok=True)
    df.to_parquet(output, index=False)
    logger.info(f"Pipeline complete. {len(df):,} records saved to {output}")
    return df

if __name__ == '__main__':
    run_pipeline()

