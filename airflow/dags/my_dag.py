
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'code2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='first description',
    start_date=datetime(2024,8,15),
    schedule_interval='@daily',
):
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )

    task1