# Yelp Data Lake

## Overview

This project constructs a data lake using Yelp's dataset, following a series of steps: ingestion, cleaning, aggregation, and querying. Each stage of data processing is organized into corresponding directories within the `data/` directory:

- **data/raw/**: Contains the raw JSON data.
- **data/cleaned/**: Stores cleaned data in Parquet format.
- **data/aggregated/**: Holds the aggregated data in Parquet format.
- **data/output/**: Final outputs or derived datasets.

The entire project is containerized using Docker for easy deployment and management.

## Project Structure

- **README.md**: Documentation of the project.
- **Dockerfile**: Defines the Docker image for the application.
- **docker-compose.yml**: Configuration for Docker Compose, setting up services.
- **main.py**: Entry point to build, test, and query the data lake.
- **scripts/**: Contains scripts for building the data lake, running queries, and testing.
- **src/**: Contains source code for data ingestion, cleaning, aggregation, and utility functions.
- **data/**: Directory that houses raw, cleaned, aggregated, and output data.
- **tests/**: Unit tests to validate each component of the application.

## Detailed Description of Files

### Dockerfile
Defines the environment for the project using Python 3.9 and OpenJDK 11. It installs the necessary dependencies, sets up the directory structure, and copies the application code into the container. The Dockerfile ensures that the application can be executed within a container with all required tools and libraries.

### docker-compose.yml
Specifies the Docker services required for the project. It includes a service for building the data lake (`yelp_data_lake`), which mounts the data directory from the host to the container and runs the `main.py` script to build the data lake.

### main.py
The main entry point for the project. It provides a command-line interface to:
- Build the data lake.
- Run unit tests.
- Execute SQL queries against the data lake.

### scripts/
- **BUILD_DATA_LAKE.py**: Orchestrates the data lake construction by executing the following steps:
  1. **Data Ingestion:** Converts raw JSON files to Parquet format.
  2. **Data Cleaning:** Cleans and deduplicates the data.
  3. **Data Aggregation:** Aggregates the cleaned data into useful metrics.
- **RUN_QUERY.py**: Provides a command-line tool to run SQL queries against the data lake, utilizing the temporary views created from the cleaned and aggregated datasets.

### src/
Contains the core processing scripts:
- **DATA_INGESTION.py**: Handles the ingestion of raw Yelp data from JSON to Parquet format.
- **DATA_CLEANING.py**: Cleans and deduplicates the ingested data.
- **DATA_AGGREGATION.py**: Aggregates the cleaned data to produce metrics such as weekly average stars and check-in counts.
- **QUERY_SERVICE.py**: Manages SQL queries against the processed data, allowing for complex data retrieval operations.
- **UTILS/**: Utility functions for directory management (`file_utils.py`), Spark session configuration (`spark_session.py`), and data validation/cleaning (`data_validation.py`).

### tests/
Contains unit tests to validate the functionality of the data processing pipeline:
- **TEST_DATA_INGESTION.py**: Tests the data ingestion process.
- **TEST_DATA_CLEANING.py**: Tests the data cleaning functions.
- **TEST_DATA_AGGREGATION.py**: Validates the data aggregation logic.
- **TEST_QUERY_SERVICE.py**: Ensures the query service correctly executes SQL queries.

## How to Run

### Download Data Files

Download Yelp’s JSON dataset from https://www.yelp.com/dataset/download. Store following five files in folder 'data/raw/'

- yelp_academic_dataset_business.json
- yelp_academic_dataset_checkin.json
- yelp_academic_dataset_review.json
- yelp_academic_dataset_tip.json
- yelp_academic_dataset_user.json

### Build the Docker Image

To build the Docker image for the project, run the following command in the directory containing the Dockerfile:

```bash
docker build -t yelp_data_lake
```

###  Build the Data Lake

To build the data lake, use Docker Compose:

```bash
docker-compose up
```
This command will create the necessary directory structure, ingest, clean, and aggregate the data, and store the results in the appropriate directories.

###  Run Tests
To run the unit tests within the Docker container:

```bash

docker run --rm yelp_data_lake python3 main.py test
```

### Execute Query
To execute a query against the data lake:

```bash

docker run --rm yelp_data_lake python3 main.py query --query "SELECT * FROM business WHERE stars > 4"
```
## Notes
- Ensure the raw JSON files are placed in the data/raw/ directory before building the data lake.
- The project assumes the availability of Yelp's dataset in the specified format.
