from airflow import DAG
from datetime import datetime




with DAG(dag_id = "user_processing",start_time = datetime(2023,1,1),schedule_interval = "@daily",catchup = False) as dag:
    None