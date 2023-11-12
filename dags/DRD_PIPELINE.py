from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define default_args to specify the start date and other DAG parameters
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG with the defined default_args
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple Airflow DAG with multiple tasks',
    schedule_interval=timedelta(days=1),  # You can adjust the schedule interval as needed
)

# Define the Python functions to be executed by each task
def task_1_function():
    print("Executing Task 1")

def task_2_function():
    print("Executing Task 2")

def task_3_function():
    print("Executing Task 3")

# Define the tasks using the PythonOperator
task_1 = PythonOperator(
    task_id='task_1',
    python_callable=task_1_function,
    dag=dag,
)

task_2 = PythonOperator(
    task_id='task_2',
    python_callable=task_2_function,
    dag=dag,
)

task_3 = PythonOperator(
    task_id='task_3',
    python_callable=task_3_function,
    dag=dag,
)

# Set the task dependencies
task_1 >> task_2 >> task_3
