
from datetime import datetime, timedelta

from airflow.sdk import dag, task

from crypto_etl.extract import extract
from crypto_etl.transform import transform
from crypto_etl.load import load


@dag(
    dag_id="crypto_etl_pipeline",
    schedule="*/15 * * * *",
    start_date=datetime(2026, 11, 1),
    catchup=False,
    max_active_runs=1,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=2)
    },
)

def crypto_etl_pipeline():

    @task
    def extract_task():
        return extract()

    @task
    def transform_task(rows):
        return transform(rows)

    @task
    def load_task(records):
        return load(records)

    raw_data = extract_task()
    transformed_data = transform_task(raw_data)
    load_task(transformed_data)


crypto_etl_pipeline()
