import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_directory_structure():
    directories = [
        "data/raw",
        "data/cleaned",
        "data/aggregated",
        "data/output"
    ]
    for dir_path in directories:
        create_directory(dir_path)
