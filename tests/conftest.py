import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    spark = SparkSession.builder.appName("PySpark tests").getOrCreate()
    yield spark
    spark.stop()
