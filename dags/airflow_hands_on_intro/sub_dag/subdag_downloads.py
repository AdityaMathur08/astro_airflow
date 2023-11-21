# sub dag is nothing but a dag with taks grouped togather
from airflow import DAG
from airflow.operators.bash import BashOperator

# function that returns a DAG object

def subdag_downloads(parent_dag_id,child_dag_id,args):
    with DAG(f"{parent_dag_id}.{child_dag_id}",
             start_date = args['start_date'],
             schedule_interval = args['schedule_interval'],
             catchup = args['catchup']):
        download_a = BashOperator(
            task_id='download_a',
            bash_command='sleep 10'
        )
 
        download_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 10'
        )
    
        download_c = BashOperator(
            task_id='download_c',
            bash_command='sleep 10'
        )

        return DAG
    