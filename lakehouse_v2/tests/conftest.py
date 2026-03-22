import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    """Local SparkSession for unit tests — no Databricks cluster needed."""
    return (
        SparkSession.builder
        .master("local[2]")
        .appName("unit-tests")
        .config("spark.sql.shuffle.partitions", "2")
        .getOrCreate()
    )
