from src.data_ingestion import ingest_data
from src.data_cleaning import clean_all_data
from src.data_aggregation import aggregate_data
from src.utils.file_utils import create_directory_structure

def build_data_lake():
    # Create necessary directories
    create_directory_structure()

    # Ingest Data
    ingest_data()

    # Clean Data
    clean_all_data()

    # Aggregate Data
    aggregate_data()


if __name__ == "__main__":
    build_data_lake()