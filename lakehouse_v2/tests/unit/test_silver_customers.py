import pytest
from pyspark.sql import SparkSession
from lakehouse_v2.silver_transformations import (
    trim_string_columns,
    normalize_gender,
    normalize_marital_status,
    filter_null_customer_id    
)

@pytest.fixture(scope="session")
def spark():
    return (
        SparkSession.builder
        .master("local[2]")
        .appName("unit-tests")
        .getOrCreate()
    )

def test_gender_male_normalized(spark):
    df = spark.createDataFrame([("M",)], ["cst_gndr"])
    result = normalize_gender(df, "cst_gndr")
    assert result.collect()[0]["cst_gndr"] == "Male"

def test_gender_female_normalized(spark):
    df = spark.createDataFrame([("F",)], ["cst_gndr"])
    result = normalize_gender(df, "cst_gndr")
    assert result.collect()[0]["cst_gndr"] == "Female"   

def test_gender_unknown_becomes_na(spark):
    df = spark.createDataFrame([("X",)], ["cst_gndr"])
    result = normalize_gender(df, "cst_gndr")
    assert result.collect()[0]["cst_gndr"] == "n/a"   

def test_marital_status_single(spark):
    df = spark.createDataFrame([("S",)], ["cst_marital_status"])
    result = normalize_marital_status(df, "cst_marital_status")
    assert result.collect()[0]["cst_marital_status"] == "Single"      

def test_marital_status_married(spark):
    df = spark.createDataFrame([("M",)], ["cst_marital_status"])
    result = normalize_marital_status(df, "cst_marital_status")
    assert result.collect()[0]["cst_marital_status"] == "Married"   

def test_null_customer_id_dropped(spark):
    df = spark.createDataFrame([(None,), ("123",)], ["customer_id"])
    result = filter_null_customer_id(df, "customer_id")
    assert result.count() == 1

def test_trim_string_columns(spark):
    df = spark.createDataFrame([("  John  ", "  Doe  ")], ["first_name", "last_name"])
    result = trim_string_columns(df)
    assert result.collect()[0]["first_name"] == "John"
    assert result.collect()[0]["last_name"] == "Doe"
    