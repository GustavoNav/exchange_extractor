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
    description='A simple DAG that runs pwd command',
    schedule_interval='@daily',  
)

# Define a tarefa
run_pwd = BashOperator(
    task_id='run_docker',
    # Coloque o path para o diretório extract_exchange do git.
    bash_command='cd /home/gustavo/projetos/extract_exchange && docker-compose run --rm app historic_extractor/run.py VALE3.SA',
    dag=dag,
)

run_pwd
