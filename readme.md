


Configuração do airflow:

O airflow é configurado localmente com o airflowctl, para baixar:

pip install airflowctl


inicie o airflow:

airflowctl init airflow_project --build-start

mova o conteudo do diretório dags da raiz para airflow_project/dags
general_etl.py
historic_etl.py
real_time_etl.py

por fim, acesso o localhost:8080 , logue com o usuário e senha criados pelo airflow (mostrado no terminal) e coloque as dags para executarem.