from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


# Define a DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'retries': 1,
}

dag = DAG(
    'historic_etl',
    default_args=default_args,
    description='A DAG that runs historic_extractor',
    schedule_interval='@daily',  
)

run_docker = BashOperator(
    task_id='run_docker',
    # Coloque o path absoluto para o diretório extract_exchange do git.
    bash_command='cd /path/extract_exchange && docker-compose run --rm app historic_extractor/run.py VALE3.SA',
    dag=dag,
)

run_docker
