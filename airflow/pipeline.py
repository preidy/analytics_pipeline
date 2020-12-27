import datetime
import sys
sys.path.append('/home/preidy/Code/analytics_pipeline/airflow/')

from airflow import DAG
from airflow.contrib.operators.bigquery_operator import BigQueryOperator


default_args = {
   'retries': 0,
   'start_date': datetime.datetime(2019, 8, 10)
}

dag = DAG(
    'analytics_pipeline',
    default_args=default_args,
    schedule_interval=None, # set to '0 8 * * *' for daily at 8am
    catchup=False,
    # tells airflow where sql is
    template_searchpath='/home/preidy/Code/analytics_pipeline/airflow/sql/'
)

extract_and_load = BigQueryOperator(
    task_id='extract_and_load',
    sql='extract_sql.sql',
    destination_dataset_table='pat-scratch.analytics_pipeline.raw__nyc_311',
    write_disposition='WRITE_TRUNCATE', # overwrite entire table if it exists,
    use_legacy_sql=False,
    location='US',
    project_id='pat-scratch',
    dag=dag
    
)
