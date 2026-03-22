import pytest
from pyspark.sql import SparkSession
from lakehouse_v2.silver_transformations import normalize_product_line

@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder
        .master("local[2]")
        .appName("unit-tests")
        .getOrCreate()
    )

def test_product_line_mountain(spark):
    df = spark.createDataFrame([("M",)], ["prd_line"])
    result = normalize_product_line(df, "prd_line")
    assert result.collect()[0]["prd_line"] == "Mountain"

def test_product_line_road(spark):
    df = spark.createDataFrame([("R",)], ["prd_line"])
    result = normalize_product_line(df, "prd_line")
    assert result.collect()[0]["prd_line"] == "Road"

def test_product_line_touring(spark):
    df = spark.createDataFrame([("T",)], ["prd_line"])
    result = normalize_product_line(df, "prd_line")
    assert result.collect()[0]["prd_line"] == "Touring"

def test_product_line_other_sales(spark):
    df = spark.createDataFrame([("S",)], ["prd_line"])
    result = normalize_product_line(df, "prd_line")
    assert result.collect()[0]["prd_line"] == "Other Sales"

def test_product_line_unknown_becomes_na(spark):
    df = spark.createDataFrame([("Z",)], ["prd_line"])
    result = normalize_product_line(df, "prd_line")
    assert result.collect()[0]["prd_line"] == "n/a"