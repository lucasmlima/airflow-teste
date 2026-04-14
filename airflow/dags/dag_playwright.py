from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="dag_playwright",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    executar_scraping = BashOperator(
        task_id="executar_scraping",
        bash_command="docker run --rm -e PYTHONUNBUFFERED=1 python-teste"
    )