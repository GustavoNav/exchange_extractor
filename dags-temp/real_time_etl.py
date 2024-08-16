from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Define a DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),  # Ajuste start_date conforme necessário
    'retries': 1,
}

dag = DAG(
    'real_time_etl',
    default_args=default_args,
    description='A simple DAG that runs pwd command',
    schedule_interval=timedelta(minutes=3),  # Intervalo de 3 minutos
    catchup=False,  # Define se deve executar execuções passadas
)

# Define a tarefa
run_docker = BashOperator(
    task_id='run_docker',
    bash_command='cd /home/gustavo/projetos/extract_exchange && docker-compose run --rm app real_time_extractor/run.py VALE3.SA',
    dag=dag,
)

run_docker
