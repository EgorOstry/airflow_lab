# airflow_lab

This repository contains an educational project to demonstrate the use of Apache Airflow with Docker Compose. The project sets up an Airflow environment along with a PostgreSQL database. A predefined Airflow DAG (Directed Acyclic Graph) is included, which downloads NYC Taxi datasets for the first six months of 2023 and combines them into a single PostgreSQL table.

Follow these steps to run the project:

1.Clone the repository:
``` bash
git clone https://github.com/EgorOstry/airflow_lab.git
cd airflow_lab
```

2. Create .env file with PG_USER=*** PG_PASS=*** PG_DB=*** PG_PORT=***
for example
``` bash
touch .env
echo "PG_USER='root'" >> .env
echo "PG_PASS='root'" >> .env
echo "PG_DB='ny_taxi'" >> .env
echo "PG_PORT='5432'" >> .env
```

Run

``` bash
echo -e "AIRFLOW_UID=$(id -u)" >> .env
```

3.Initialize the Airflow database and initialize the metadata:
``` bash
docker-compose run airflow-cli db init
docker-compose up airflow-init
``` 
4.Start the Airflow environment in detached mode:
``` bash
docker-compose up -d
``` 
5.Access the Airflow web interface by opening the following URL in your web browser:
`http://localhost:8080/home`
   - **Username:** Airflow
   - **Password:** Airflow

6. Connect to the PostgreSQL database:
   - **Host:** localhost
   - **Port:** PG_PORT from .env
   - **Username:** PG_USER from .env
   - **Password:** PG_PASS from .env


6.Start the "IngestionDag" DAG in the Airflow web interface to initiate the data ingestion process.

That's it! You've successfully set up and executed the Airflow project to download and combine NYC Taxi datasets into a PostgreSQL database.
Feel free to explore the Airflow web interface and customize the DAG or the project as needed for your educational purposes.
