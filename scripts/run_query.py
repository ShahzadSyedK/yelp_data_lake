import argparse
from src.query_service import QueryService

def execute_query(query_str):
    qs = QueryService()
    qs.initialize_views()
    qs.run_query(query_str)
    qs.stop_session()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute a SQL query on the Yelp Data Lake.")
    parser.add_argument("--query", type=str, required=True, help="SQL query to execute.")
    args = parser.parse_args()

    execute_query(args.query)
