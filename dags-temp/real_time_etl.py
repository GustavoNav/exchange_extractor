from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'retries': 1,
}

dag = DAG(
    'real_time_etl',
    default_args=default_args,
    description='A simple DAG that runs real_time_extractor',
    schedule_interval=timedelta(minutes=3),  # Intervalo de 3 minutos
    catchup=False,
)

run_docker = BashOperator(
    task_id='run_docker',
    # Coloque o path absoluto para o diretório extract_exchange do git.
    bash_command='cd /path/extract_exchange && docker-compose run --rm app real_time_extractor/run.py VALE3.SA',
    dag=dag,
)

run_docker
