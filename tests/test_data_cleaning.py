import unittest
from pyspark.sql import SparkSession
from src.utils.data_validation import clean_column_names

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.appName("DataCleaningTest").getOrCreate()
        data = [("Alice", 25), ("Bob", 30), ("Charlie", None)]
        columns = ["Name\n", "Age\t"]
        self.df = self.spark.createDataFrame(data, columns)

    def test_clean_column_names(self):
        cleaned_df = clean_column_names(self.df)
        expected_columns = ["Name", "Age"]
        self.assertEqual(cleaned_df.columns, expected_columns)

    def tearDown(self):
        self.spark.stop()

if __name__ == "__main__":
    unittest.main()
