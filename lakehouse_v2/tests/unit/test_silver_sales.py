import pytest
from pyspark.sql import SparkSession
from lakehouse_v2.silver_transformations import clean_sales_dates


@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder
        .master("local[2]")
        .appName("unit-tests")
        .getOrCreate()
    )

def test_valid_date_parsed(spark):
    df = spark.createDataFrame([(20210101,)], ["sls_order_dt"])
    result = clean_sales_dates(df, "sls_order_dt")
    assert result.collect()[0]["sls_order_dt"] is not None

def test_zero_date_becomes_null(spark):
    df = spark.createDataFrame([(0,)], ["sls_order_dt"])
    result = clean_sales_dates(df, "sls_order_dt")
    assert result.collect()[0]["sls_order_dt"] is None

def test_invalid_date_becomes_null(spark):
    df = spark.createDataFrame([(999,)], ["sls_order_dt"])
    result = clean_sales_dates(df, "sls_order_dt")
    assert result.collect()[0]["sls_order_dt"] is None