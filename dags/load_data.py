from airflow import DAG
from datetime import datetime, timedelta
import pendulum
from airflow.operators.python import PythonOperator
from tasks_template import (get_data, upload_data)
# @dag(
#     dag_id="load_velib",
#     schedule_interval="@hourly",
#     start_date=pendulum.datetime(2023,6,16),
#     catchup=False
# )

default_args = {
    'owner': 'esteban',
    'retries': 5,
    'retry_delay' : timedelta(minutes=5)
}
with DAG(
    dag_id="load_velib_v2",
    schedule_interval="@hourly",
    start_date=pendulum.datetime(2023,6,16),
    catchup=False
) as dag :
    get = PythonOperator(
        task_id = "get_data",
        python_callable = get_data
    )

    upload = PythonOperator(
        task_id = "upload_data",
        python_callable = upload_data
    )
    
    get >> upload

        
