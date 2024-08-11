from src.utils.spark_session import spark_session

class QueryService:
    def __init__(self):
        self.spark = spark_session("Query Service")
        

    def initialize_views(self):
        # Load data and create temporary views
        data_dirs = {
            "business": "data/cleaned/yelp_academic_dataset_business.parquet",
            "user": "data/cleaned/yelp_academic_dataset_user.parquet",
            "review": "data/cleaned/yelp_academic_dataset_review.parquet",
            "checkin": "data/cleaned/yelp_academic_dataset_checkin.parquet",
            "tip": "data/cleaned/yelp_academic_dataset_tip.parquet",
            "weekly_stars": "data/aggregated/weekly_stars.parquet",
            "checkin_counts": "data/aggregated/checkin_counts.parquet"
        }

        for view_name, path in data_dirs.items():
            try:
                df = self.spark.read.parquet(path)
                df.createOrReplaceTempView(view_name)
                print(f"Temporary view '{view_name}' created from {path}")
            except Exception as e:
                print(f"Error creating view '{view_name}': {e}")

    def run_query(self, query_str):
        try:
            result_df = self.spark.sql(query_str)
            result_df.show(truncate=False)
        except Exception as e:
            print(f"Error executing query: {e}")

    def stop_session(self):
        self.spark.stop()
