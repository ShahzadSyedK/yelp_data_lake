from pyspark import SparkConf
from pyspark.sql import SparkSession

def spark_session(app_name):
    # Set Spark configuration for memory and thread management 
    # due to limited resources avaialable at dev environment
    conf = SparkConf() \
        .setAppName(app_name) \
        .set("spark.sql.parquet.enableVectorizedReader", "true") \
        .set("spark.sql.orc.enableVectorizedReader", "true") \
        .set("spark.executor.memory", "8g") \
        .set("spark.driver.memory", "4g") \
        .set("spark.executor.cores", "2") \
        .set("spark.executor.instances", "2") \
        .set("spark.sql.parquet.columnarReaderBatchSize", "2048") \
        .set("spark.sql.orc.columnarReaderBatchSize", "2048") \
        .set("spark.dynamicAllocation.enabled", "true") \
        .set("spark.dynamicAllocation.minExecutors", "1") \
        .set("spark.dynamicAllocation.maxExecutors", "4") \
        .set("spark.memory.fraction", "0.6") \
        .set("spark.memory.storageFraction", "0.5") \
        .set("spark.executor.extraJavaOptions", "-XX:+UseG1GC") \
        .set("spark.driver.extraJavaOptions", "-XX:+UseG1GC") \
        .set("spark.sql.shuffle.partitions", "100")  # Adjusted based on the data size
    
    spark = SparkSession.builder \
        .config(conf=conf) \
        .getOrCreate()

    return spark    
