# airflow_lab

This repository contains an educational project to demonstrate the use of Apache Airflow with Docker Compose. The project sets up an Airflow environment along with a PostgreSQL database. A predefined Airflow DAG (Directed Acyclic Graph) is included, which downloads NYC Taxi datasets for the first six months of 2023 and combines them into a single PostgreSQL table.

Follow these steps to run the project:

1.Clone the repository:
git clone https://github.com/EgorOstry/airflow_lab.git
cd airflow_lab

2.Initialize the Airflow database and initialize the metadata:
docker-compose run airflow-cli db init
docker-compose up airflow-init

3.Start the Airflow environment in detached mode:
docker-compose up -d

4.Access the Airflow web interface by opening the following URL in your web browser:
http://localhost:8080/home
Login: Airflow
Password: Airflow

5.Connect to the PostgreSQL database:
Host: localhost
Port: 5432
Username: root
Password: root

6.Start the "IngestionDag" DAG in the Airflow web interface to initiate the data ingestion process.

That's it! You've successfully set up and executed the Airflow project to download and combine NYC Taxi datasets into a PostgreSQL database.
Feel free to explore the Airflow web interface and customize the DAG or the project as needed for your educational purposes.
