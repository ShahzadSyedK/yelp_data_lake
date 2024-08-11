#!/bin/bash

# Ensure script stops on first error
set -e

# Activate virtual environment if applicable
# source venv/bin/activate

# Build the data lake
python3 -c "
from src.data_ingestion import ingest_data
from src.data_cleaning import clean_all_data
from src.data_aggregation import aggregate_data
from src.utils.file_utils import create_directory_structure

# Create necessary directories
create_directory_structure()

# Ingest Data
ingest_data()

# Clean Data
clean_all_data()

# Aggregate Data
aggregate_data()
"

echo "Data Lake build process completed successfully."
