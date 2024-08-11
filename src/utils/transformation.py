from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, ArrayType, MapType

def transform_column_to_lowercase(df: DataFrame, column_name: str) -> DataFrame:
    """
    Transforms the specified column to lowercase.
    """
    if column_name in df.columns:
        return df.withColumn(column_name, col(column_name).lower())
    return df


def flatten_struct(df):
    # Recursive function to flatten all nested structures
    flat_cols = []
    nested_cols = []

    # Separate columns into flat and nested
    for column_name, dtype in df.dtypes:
        if '.' in column_name:
            continue
        if isinstance(df.schema[column_name].dataType, StructType):
            nested_cols.append(column_name)
        elif isinstance(df.schema[column_name].dataType, ArrayType):
            nested_cols.append(column_name)
        elif isinstance(df.schema[column_name].dataType, MapType):
            nested_cols.append(column_name)
        else:
            flat_cols.append(column_name)

    # Flatten struct columns
    for nested_column in nested_cols:
        new_columns = [col(f"{nested_column}.{field.name}").alias(f"{nested_column}_{field.name}")
                       for field in df.schema[nested_column].dataType]
        df = df.select("*", *new_columns).drop(nested_column)

    return df
