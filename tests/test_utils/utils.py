from pyspark.sql import DataFrame


def to_csv(df: DataFrame) -> str:
    return df.toPandas().to_csv(lineterminator="\n", index=False)
