import argparse
from scripts.build_data_lake import build_data_lake
from scripts.run_query import execute_query
from scripts.test_cases import run_all_tests

def main():
    parser = argparse.ArgumentParser(description="Yelp Data Lake Operations")
    parser.add_argument("action", choices=["build", "test", "query"], help="Action to perform")
    parser.add_argument("--query", type=str, help="SQL query to execute (required if action is 'query')")

    args = parser.parse_args()

    if args.action == "build":
        build_data_lake()
    elif args.action == "test":
        run_all_tests()
    elif args.action == "query":
        if not args.query:
            print("Error: --query argument is required when action is 'query'.")
            return
        execute_query(args.query)

if __name__ == "__main__":
    main()

    
# import argparse
# import subprocess

# def build_data_lake():
#     try:
#         subprocess.run(['bash', 'scripts/build_data_lake.sh'], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error while building data lake: {e}")
#         exit(1)

# def run_all_tests():
#     try:
#         subprocess.run(['python3', 'scripts/test_cases.py'], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error while running tests: {e}")
#         exit(1)

# def execute_query(query):
#     try:
#         subprocess.run(['python3', 'scripts/run_query.py', '--query', query], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error while executing query: {e}")
#         exit(1)

# def main():
#     parser = argparse.ArgumentParser(description="Yelp Data Lake Operations")
#     parser.add_argument("action", choices=["build", "test", "query"], help="Action to perform")
#     parser.add_argument("--query", type=str, help="SQL query to execute (required if action is 'query')")

#     args = parser.parse_args()

#     if args.action == "build":
#         build_data_lake()
#     elif args.action == "test":
#         run_all_tests()
#     elif args.action == "query":
#         if not args.query:
#             print("Error: --query argument is required when action is 'query'.")
#             return
#         execute_query(args.query)

# if __name__ == "__main__":
#     main()
