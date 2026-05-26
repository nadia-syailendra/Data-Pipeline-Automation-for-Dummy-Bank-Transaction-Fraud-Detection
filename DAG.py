'''
=================================================
Milestone 3

Nama  : Nadia Syailendra
Batch : CODA-016-RMT

Program ini dibuat untuk menjalankan automasi data pipeline menggunakan DAG di platform Airflow.
=================================================
'''

#Import datetime, timedelta, DAG and bash operator
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

#Define DAG start date, retry and retry delay
default_args = {
    'owner': 'nadia',
    'start_date': dt.datetime(2026, 11, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

#Define DAG schedule and graph for automated ETL
with DAG('P2M3_Nadia_Syailendra_DAG',
         default_args=default_args,
         #schedule_interval='*/5 * * * *', #For testing purpose
         schedule_interval='10-30/10 9 * * 6',
         catchup=False,
         #catchup=True #If want to backfill data from start_date
         ) as dag:

    python_extract = BashOperator(task_id='python_extract', bash_command='sudo -u airflow python /opt/airflow/scripts/extract.py')
    python_transform = BashOperator(task_id='python_transform', bash_command='sudo -u airflow python /opt/airflow/scripts/transform.py')
    python_load = BashOperator(task_id='python_load', bash_command='sudo -u airflow python /opt/airflow/scripts/load.py')
    

python_extract >> python_transform >> python_load