import os
import sys
from src.utils.file_utils import create_directory
from src.utils.spark_session import spark_session
from src.utils.transformation import flatten_struct
from pyspark.sql.types import StringType, ArrayType
from pyspark.sql.functions import col, substring, explode


def ingest_data():

    spark = spark_session("Data Ingestion")
    raw_data_dir = "data/raw"
    output_dir = "data/input"

    # Ensure the output directory exists
    create_directory(output_dir)

    # List of dataset files
    datasets = [
        "yelp_academic_dataset_user.json",
        "yelp_academic_dataset_business.json",
        "yelp_academic_dataset_checkin.json",
        "yelp_academic_dataset_tip.json",
        "yelp_academic_dataset_review.json"
    ]

    for dataset in datasets:
        input_path = os.path.join(raw_data_dir, dataset)
        if not os.path.exists(input_path):
            print(f"Error: {input_path} does not exist.")
            continue

        df = spark.read.json(input_path)

        # Handle large strings by truncating them
        max_string_length = 1000  # Adjust based on your needs
        string_cols = [field.name for field in df.schema.fields if isinstance(field.dataType, StringType)]
        for col_name in string_cols:
            df = df.withColumn(col_name, substring(col(col_name), 1, max_string_length))

        # Flatten the JSON structure
        while True:
            flat_df = flatten_struct(df)
            if len(flat_df.columns) == len(df.columns):
                break
            df = flat_df

        # Handle array columns (explode them)
        array_cols = [field.name for field in df.schema.fields if isinstance(field.dataType, ArrayType)]
        for col_name in array_cols:
            df = df.withColumn(col_name, explode(col(col_name)))

        output_path = os.path.join(output_dir, dataset.replace(".json", ".parquet"))
        df.write.mode("overwrite").parquet(output_path)
        print(f"Ingested and saved {dataset} to {output_path}")
        if sys.stdin.isatty():
            input("Ingestion completed. Press any key to proceed...")

    spark.stop()
