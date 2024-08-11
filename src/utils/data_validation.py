import re
from pyspark.sql import DataFrame
# from pyspark.sql.functions import col

def validate_column_name_length(df: DataFrame, max_length: int = 255) -> DataFrame:
    """
    Trims column names to the specified maximum length.
    """
    new_columns = [col_name[:max_length] for col_name in df.columns]
    return df.toDF(*new_columns)

def remove_special_characters_from_columns(df: DataFrame) -> DataFrame:
    """
    Removes special characters, escape sequences, and trims column names.
    """
    cleaned_columns = []
    for col_name in df.columns:
        # Remove escape sequences and special characters
        cleaned_name = re.sub(r'[\n\t\\\/]', '', col_name)
        # Replace spaces with underscores and strip leading/trailing spaces
        cleaned_name = re.sub(r'\s+', '_', cleaned_name.strip())
        cleaned_columns.append(cleaned_name)
    return df.toDF(*cleaned_columns)

def clean_column_names(df: DataFrame, max_length: int = 255) -> DataFrame:
    """
    Cleans column names by removing special characters and ensuring length constraints.
    """
    df = remove_special_characters_from_columns(df)
    df = validate_column_name_length(df, max_length)
    return df
