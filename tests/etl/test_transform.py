from pyspark.sql import DataFrame, SparkSession
from pyspark.testing import assertDataFrameEqual

from python_skeleton.etl.transform import filter_by_age


def test_filter_by_age(spark: SparkSession):
    input_data: list[dict[str, str]] = [
        {"age": "24", "name": "John"},
        {"age": "22", "name": "Jane"},
    ]
    input_df: DataFrame = spark.createDataFrame(input_data)

    actual_df: DataFrame = filter_by_age(input_df, 22)

    expected_data: list[dict[str, str]] = [
        {"age": "22", "name": "Jane"},
    ]
    expected_df: DataFrame = spark.createDataFrame(expected_data)

    assertDataFrameEqual(actual_df, expected_df)
