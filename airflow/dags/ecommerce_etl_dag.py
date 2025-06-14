from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess
import sys
import subprocess
import logging

default_args = {
    'owner': 'data-engineer',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    'ecommerce_etl_dag',
    default_args=default_args,
    description='ETL DAG for E-commerce API data',
    schedule='@daily',
    catchup=False
) as dag:
    def load_products():
        result = subprocess.run(
            [sys.executable, "/opt/warehouse/loaders/load_products.py"],
            capture_output=True,
            text=True
        )

        logging.info("STDOUT:\n%s", result.stdout)
        logging.error("STDERR:\n%s", result.stderr)

        if result.returncode != 0:
            raise Exception(f"Script failed with return code {result.returncode}")


    def load_users():
        subprocess.run([sys.executable, "/opt/warehouse/loaders/load_users.py"], check=True)

    def load_carts():
        subprocess.run([sys.executable, "/opt/warehouse/loaders/load_carts.py"], check=True)

    t1 = PythonOperator(task_id='load_products', python_callable=load_products)
    t2 = PythonOperator(task_id='load_users', python_callable=load_users)
    t3 = PythonOperator(task_id='load_carts', python_callable=load_carts)

    t1 >> t2 >> t3
