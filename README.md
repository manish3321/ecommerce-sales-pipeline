E-Commerce Sales Analytics Pipeline


🚀 Overview

The Global E-Commerce Sales Analytics Pipeline is a real-world, production-ready ETL and analytics project built using open-source tools like Apache Airflow, PostgreSQL, Docker, and Tableau. The goal of this project is to simulate an end-to-end data engineering workflow: from ingesting data via APIs to transforming, storing, and visualizing it to extract actionable business insights.

This project demonstrates how modern data teams process raw data into business-ready insights and present it through intuitive dashboards that drive decision-making.


📈 Project Objectives

                Build a scalable ETL pipeline for global e-commerce datasets
                
                Automate extraction and loading of product, user, and cart data
                
                Store cleaned data into a PostgreSQL data warehouse
                
                Visualize key metrics like sales trends, user engagement, and cart patterns in Tableau
                
                Use Docker for easy reproducibility and deployment
                
                Showcase the pipeline as a portfolio project for Data Engineering and BI roles

📊 Tech Stack & Tools
                
                Tool
                
                Purpose
                
                Python
                
                Core ETL scripting
                
                Apache Airflow
                
                Workflow orchestration (scheduling ETL DAGs)
                
                PostgreSQL
                
                Data warehouse backend
                
                Docker & Docker Compose
                
                Containerizing the entire pipeline
                
                Tableau Public
                
                Data visualization and dashboarding
                
                Git & GitHub
                
                Version control and portfolio deployment
                
                🛀 Architecture Diagram

Data Flow:

Public API ➔ Python Scripts ➔ Airflow DAG ➔ PostgreSQL ➔ Tableau Dashboards

Extraction: Python scripts fetch JSON data from an e-commerce public API

Loading: The data is inserted into a PostgreSQL database using psycopg

Scheduling: Airflow DAG orchestrates daily data ingestion

Visualization: Tableau connects directly to PostgreSQL and visualizes KPIs

📁 Project Structure

Ecommerce/
│
├── airflow/
│   └── dags/
│       └── ecommerce_etl_dag.py        # Airflow DAG definition
│
├── warehouse/
│   └── loaders/
│       ├── load_products.py            # Fetch & load product data
│       ├── load_users.py               # Fetch & load user data
│       └── load_carts.py               # Fetch & load cart data
│
├── transformations/                   # (Optional) Transform logic with pandas
├── Data/                               # Storage for raw or intermediate files
├── requirements.txt                    # Python package dependencies
├── docker-compose.yml                 # Container orchestration
└── README.md

🔄 Data Pipeline Components

1. Data Extraction

          Uses Python's requests module to fetch data from the FakeStore API.
          
          load_products.py, load_users.py, and load_carts.py parse and validate this data.

2. Data Loading

          Transforms the JSON data into structured SQL inserts
          
          PostgreSQL stores the data into relational tables: products, users, carts

3. DAG Scheduling

          DAG ecommerce_etl_dag.py runs every 24 hours
          
          Tasks are defined using PythonOperator
          
          Dependencies set as: load_products >> load_users >> load_carts

4. Data Warehouse (PostgreSQL)

          Hosted via Docker and exposed on port 5433
          
          Database: retaildb
          
          Schema normalization used to ensure relational integrity

📆 Airflow DAG Snapshot

          with DAG(
              'ecommerce_etl_dag',
              schedule_interval='@daily',
              default_args=default_args,
              catchup=False,
              description='ETL DAG for E-commerce API data'
          ) as dag:
              t1 = PythonOperator(task_id='load_products', python_callable=load_products)
              t2 = PythonOperator(task_id='load_users', python_callable=load_users)
              t3 = PythonOperator(task_id='load_carts', python_callable=load_carts)
          
              t1 >> t2 >> t3

📊 Tableau Dashboard

The Tableau dashboard is built by directly connecting to the PostgreSQL database running in Docker.

Key Insights Visualized

          ₹ Total Sales by Product Category
          
          👨️ Top Purchasing Users
          
          🛒 Cart Abandonment Trends
          
          🌎 Sales by Country (via user address)
          
          📅 Daily & Weekly Revenue Trends
          
          🔗 Link to Tableau Public Dashboard

🚪 How to Run This Project

              Prerequisites
              
              Docker & Docker Compose
              
              Git
              
              Tableau Desktop or Tableau Public

Steps

              git clone https://github.com/manish3321/ecommerce-sales-pipeline.git
              cd ecommerce-sales-pipeline
              docker-compose up --build

              Access Airflow UI: http://localhost:8080
              
              Username: admin  Password: admin
              
              Trigger ecommerce_etl_dag
              
              Connect Tableau to PostgreSQL (host: ****, port: 5433, db: *****)

🚀 Achievements

              End-to-end working data pipeline in Docker
              
              Airflow DAGs with proper task dependencies
              
              Custom loader scripts with error handling
              
              Tableau dashboard powered by live PostgreSQL data
              
              Clean GitHub project with production potential



🚪 Security & Best Practices

            Environment variables are managed securely in Docker Compose
            
            Airflow secrets and database passwords externalized (optional: .env)
            
            Retry logic in DAGs and subprocesses



📕 Future Enhancements

          Add Airflow email alerts and logging enhancements
          
          Integrate dbt for transformation layer
          
          Host PostgreSQL and Airflow on cloud (AWS/GCP/Azure)
          


👨‍💼 About the Author

Manish Bhattarai
Data Engineer | Pythonista | BI EnthusiastGitHub: @manish3321LinkedIn: https://www.linkedin.com/in/manish-bhattarai-347497148/


