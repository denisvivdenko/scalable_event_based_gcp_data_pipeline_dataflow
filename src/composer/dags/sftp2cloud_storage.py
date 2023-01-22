from airflow import DAG
from airflow.providers.sftp.operators.sftp import SFTPOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta


dag = DAG("sftp_dag",
    start_date=datetime.now(),
    schedule_interval=None,
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "email_on_failure": False,
        "email_on_retry": False
    }
)


put_file = SFTPOperator(
    task_id="test_sftp",
    ssh_conn_id="sftp_connection_id",
    local_filepath="/home/airflow/gcs/data/covid_data.csv",
    remote_filepath="/home/denys/covid_data.csv",
    operation="get",
    create_intermediate_dirs=True,
    dag=dag
)


start_pipeline = DummyOperator(task_id="start_pipeline", dag=dag)

start_pipeline >> put_file
