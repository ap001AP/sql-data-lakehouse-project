from pyspark.sql import DataFrame
from pyspark.sql.types import StringType, DateType
import pyspark.sql.functions as F
from pyspark.sql.functions import col, trim, when, upper, coalesce, lit, to_date, length, regexp_replace, substring, current_date



# Trim whitespace from all the string columns
def trim_string_columns(df: DataFrame) -> DataFrame:
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))
    return df 

# Normalize gender codes to full names 
def normalize_gender(df: DataFrame, col_name: str) -> DataFrame:
    return df.withColumn(
        col_name,
        when(upper(col(col_name)).isin("M", "MALE"), "Male")
        .when(upper(col(col_name)).isin("F", "FEMALE"), "Female")
        .otherwise("n/a")
    )

# Normalize  marital status codes to full names 
def normalize_marital_status(df: DataFrame, col_name: str) -> DataFrame:
    return df.withColumn(
        col_name,
        when(upper(col(col_name))== "S", "Single")
        .when(upper(col(col_name))== "M", "Married")
        .otherwise("n/a")
    )

# Normalize product line codes to full names
def normalize_product_line(df: DataFrame, col_name: str) -> DataFrame:
    return df.withColumn(
        col_name,
        when(upper(col(col_name))== "M", "Mountain")
        .when(upper(col(col_name))== "R", "Road")
        .when(upper(col(col_name))== "S", "Other Sales")
        .when(upper(col(col_name))== "T", "Touring")
        .otherwise("n/a")
    )

# Remove customers_id that have NULL values
def filter_null_customer_id(df: DataFrame, col_name: str) -> DataFrame:
    return df.filter(col(col_name).isNotNull())

# Convert integer date format YYYYMMDD to proper date
def clean_sales_dates(df: DataFrame, col_name: str) -> DataFrame:
    return df.withColumn(
        col_name,
        when(
            (col(col_name)==0) | (length(col(col_name)) != 8),
            None
        ).otherwise(F.to_date(col(col_name).cast("string"), "yyyyMMdd"))
    )

