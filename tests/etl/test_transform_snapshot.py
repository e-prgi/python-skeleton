import os.path
from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from pytest_snapshot.plugin import Snapshot

from python_skeleton.etl.transform import filter_by_age
from tests.test_utils.utils import to_csv

SAMPLES: str = "samples"
SNAPSHOTS: str = "snapshots"
ROOT_TEST_PATH: Path = Path(os.path.dirname(__file__))
SAMPLES_PATH: Path = ROOT_TEST_PATH.joinpath(SAMPLES)
SNAPSHOTS_PATH: Path = ROOT_TEST_PATH.joinpath(SNAPSHOTS)


def test_filter_by_age(spark: SparkSession, snapshot: Snapshot):
    input_df: DataFrame = spark.read.csv(SAMPLES_PATH.joinpath("data.csv").as_posix(), header=True)

    actual_df: DataFrame = filter_by_age(input_df, 22)

    snapshot.snapshot_dir = SNAPSHOTS_PATH
    snapshot.assert_match(to_csv(actual_df), "data.csv")
