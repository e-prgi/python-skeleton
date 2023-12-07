from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

from python_skeleton.utils.spark import get_spark_session


def transform(path: Path):
    df: DataFrame = read_data(path)
    df: DataFrame = filter_by_age(df, 22)
    write_data(df, path)


def read_data(path: Path) -> DataFrame:
    spark: SparkSession = get_spark_session()
    return spark.read.csv(path.as_posix(), header=True)


def filter_by_age(df: DataFrame, age: int) -> DataFrame:
    return df.filter(F.col("age") == age)


def write_data(df: DataFrame, path: Path):
    df.write.parquet(f"{resolve_output_path(path).as_posix()}", mode="overwrite")


def resolve_output_path(input_path: Path) -> Path:
    return input_path.parent.joinpath("output.parquet")
