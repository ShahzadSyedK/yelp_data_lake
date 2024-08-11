import unittest
from pyspark.sql import SparkSession
from src.query_service import QueryService
import os

class TestQueryService(unittest.TestCase):
    def setUp(self):
        self.qs = QueryService()
        # Create sample dataframes and register as temp views
        data = [("biz_1", 5.0), ("biz_2", 4.0)]
        df = self.qs.spark.createDataFrame(data, ["business_id", "stars"])
        df.createOrReplaceTempView("business")

    def test_run_query(self):
        query = "SELECT business_id FROM business WHERE stars > 4.5"
        self.qs.run_query(query)
        result_df = self.qs.spark.sql(query)
        results = result_df.collect()
        expected = [("biz_1",)]
        self.assertEqual([row.business_id for row in results], [item[0] for item in expected])

    def tearDown(self):
        self.qs.stop_session()

if __name__ == "__main__":
    unittest.main()
