import unittest
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
import os

class TestDataAggregation(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.appName("DataAggregationTest").getOrCreate()
        data = [("biz_1", "2024-01-01", 5.0), ("biz_1", "2024-01-08", 4.0), ("biz_2", "2024-01-03", 3.0)]
        self.review_df = self.spark.createDataFrame(data, ["business_id", "date", "stars"])

    def test_weekly_average_stars(self):
        weekly_stars = self.review_df.groupBy("business_id").agg(avg("stars").alias("avg_stars"))
        result = weekly_stars.collect()
        expected = [("biz_1", 4.5), ("biz_2", 3.0)]
        self.assertEqual(sorted(result), sorted(expected))

    def tearDown(self):
        self.spark.stop()

if __name__ == "__main__":
    unittest.main()
