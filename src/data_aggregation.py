import os
# from pyspark.sql import SparkSession
from pyspark.sql.functions import weekofyear, avg
from src.utils.file_utils import create_directory
from src.utils.spark_session import spark_session

def aggregate_data():
    # spark = SparkSession.builder.appName("Data Aggregation").getOrCreate()
    spark = spark_session("Data Aggregation")

    input_dir = "data/cleaned"
    output_dir = "data/aggregated"

    # Ensure the output directory exists
    create_directory(output_dir)

    # Load necessary datasets
    review_path = os.path.join(input_dir, "yelp_academic_dataset_review.parquet")
    checkin_path = os.path.join(input_dir, "yelp_academic_dataset_checkin.parquet")

    if not os.path.exists(review_path) or not os.path.exists(checkin_path):
        print("Error: Necessary datasets for aggregation are missing.")
        spark.stop()
        return

    review_df = spark.read.parquet(review_path)
    checkin_df = spark.read.parquet(checkin_path)

    # Aggregate: Weekly average stars per business
    weekly_stars = review_df.groupBy("business_id", weekofyear("date").alias("week")) \
                            .agg(avg("stars").alias("avg_stars"))

    weekly_stars_output = os.path.join(output_dir, "weekly_stars.parquet")
    weekly_stars.write.mode("overwrite").parquet(weekly_stars_output)
    print(f"Aggregated weekly stars saved to {weekly_stars_output}")

    # Aggregate: Number of check-ins per business
    checkin_counts = checkin_df.groupBy("business_id").count().withColumnRenamed("count", "checkin_count")

    checkin_counts_output = os.path.join(output_dir, "checkin_counts.parquet")
    checkin_counts.write.mode("overwrite").parquet(checkin_counts_output)
    print(f"Aggregated check-in counts saved to {checkin_counts_output}")

    spark.stop()
