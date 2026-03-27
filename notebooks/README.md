# Databricks Notebooks

These notebooks are deployed to Databricks via the Asset Bundle job defined in `lakehouse_v2/resources/lakehouse_v2_job.yml`.

## Ingestion Notebooks (Bronze Layer)

| Notebook | Purpose |
|---|---|
| `bronze_jdbc_ingestion` | Ingests 6 ERP/CRM tables from PostgreSQL into Bronze Delta tables |
| `bronze_api_ingestion` | Pulls REST Countries API data into Bronze Delta tables |
| `bronze_kafka_streaming` | Consumes Kafka sales events into Bronze Delta tables via Structured Streaming |
| `kafka_producer` | Publishes fake sales events to Kafka topic for testing |

## Data Quality Notebooks

| Notebook | Purpose |
|---|---|
| `dq_great_expectations` | Runs automated Great Expectations DQ checks on Bronze CRM customers — validates 18,494 records against 4 rules on every pipeline run |

## ML Notebooks

| Notebook | Purpose |
|---|---|
| `ml_sales_forecast` | Engineers features from Gold tables, trains a Random Forest sales forecasting model, logs to MLflow, registers in Model Registry, and exposes a live REST endpoint via Databricks Model Serving |
| `ml_customer_segmentation` | Engineers customer-level features from 18,484 customers, trains a KMeans clustering model to segment into 3 value tiers, and registers in Model Registry |

## Pipeline Execution Order
```
api_ingestion
      ↓
jdbc_ingestion
      ↓
bronze_ingestion
      ↓
silver_transformations
      ↓
gold_transformations
      ↓
ml_retraining (sales_forecast)
      ↓
ml_customer_segmentation
```