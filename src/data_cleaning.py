import os
# from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from src.utils.data_validation import clean_column_names
from src.utils.file_utils import create_directory
from src.utils.spark_session import spark_session

def clean_all_data():
    # spark = SparkSession.builder.appName("Data Cleaning").getOrCreate()
    spark = spark_session("Data Cleaning")
    input_dir = "data/input"
    output_dir = "data/cleaned"

    # Ensure the output directory exists
    create_directory(output_dir)

    parquet_files = [f for f in os.listdir(input_dir) if f.endswith(".parquet")]

    for file in parquet_files:
        input_path = os.path.join(input_dir, file)
        df = spark.read.parquet(input_path)

        # Clean column names
        df = clean_column_names(df)

        # Remove duplicates
        df = df.dropDuplicates()

        # # Remove rows with nulls in critical columns (assuming 'text' is critical)
        # if 'text' in df.columns:
        #     df = df.filter(col("text").isNotNull())

        output_path = os.path.join(output_dir, file)
        df.write.mode("overwrite").parquet(output_path)
        print(f"Cleaned and saved {file} to {output_path}")

    spark.stop()
