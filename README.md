# Data Lakehouse — Version 3

## Overview
Version 3 builds on top of [Data Lakehouse V2](https://github.com/ap001AP/sql-data-lakehouse-project/tree/lakehouse_v2) by adding a **dbt transformation layer** with automated data quality tests and data lineage documentation. The ML and observability layers are currently in progress.

---

## What's New in V3

- **dbt Core Integration**: Replaced Gold layer SQL notebooks with version-controlled dbt models — staging views and Gold dimension/fact tables are now defined as `.sql` files with full lineage tracking and auto-generated documentation.
- **Automated Data Quality Tests**: Built 17 dbt schema tests covering uniqueness, null checks, and referential integrity across all staging and Gold models.
- **Duplicate Customer Deduplication**: Discovered and resolved 5 duplicate customer IDs in the Silver layer using a `ROW_NUMBER()` window function to keep the most recent record per customer.
- **Null Sales Amount Fix**: Identified 8 rows with null `sales_amount` and imputed values using `price * quantity` directly in the staging model.
- **Data Lineage Graph**: Auto-generated dbt documentation with a visual lineage graph showing the full data flow from Silver sources through staging views to Gold tables.

### In Progress
- **MLflow + Feature Store**: Training sales forecasting and customer segmentation models on Gold data with experiment tracking and model registry.
- **Model Serving**: Deploying trained models as REST API endpoints via Databricks Model Serving.
- **Great Expectations**: Cross-layer data observability and alerting.

---

## Architecture
```
Source Systems
CSV Files · PostgreSQL (Render) · REST Countries API · Apache Kafka (Aiven)
        ↓
Bronze Layer — Raw ingestion into Delta tables
        ↓
Silver Layer — PySpark transformations, data quality, standardization
        ↓
dbt Staging Views — stg_customers, stg_products, stg_sales
        ↓
Gold Layer — dim_customers, dim_products, fact_sales (built by dbt)
        ↓
ML Layer (in progress) — Feature Store → MLflow → Model Serving REST API
```

---

## dbt Data Lineage
```
stg_customers → dim_customers ↘
stg_products  → dim_products  → fact_sales
stg_sales                     ↗
```

---

## dbt Tests — 17/17 Passing

| Model | Tests |
|---|---|
| `stg_customers` | unique + not_null on customer_id |
| `stg_products` | unique + not_null on product_id |
| `stg_sales` | not_null on order_number, sales_amount, quantity, price |
| `dim_customers` | unique + not_null on customer_key, not_null on customer_id, first_name, last_name |
| `dim_products` | unique + not_null on product_key |
| `fact_sales` | not_null on order_number, sales_amount |

---

## CI/CD Pipeline

Every push to `lakehouse_v3` branch triggers:
```
Push to GitHub
      ↓
Run unit tests (pytest)
      ↓ (only if all tests pass)
Deploy bundle to Databricks dev environment
```

---

## Tech Stack
| Tool | Purpose |
|---|---|
| **Databricks** | Unified analytics and pipeline platform |
| **Delta Lake** | Storage format for all Lakehouse layers |
| **Unity Catalog** | Data governance and schema management |
| **dbt Core** | SQL transformation models with testing and lineage |
| **PostgreSQL** | Operational source database (Render) |
| **Apache Kafka** | Real-time streaming via Aiven managed Kafka |
| **Spark Structured Streaming** | Continuous Kafka to Delta ingestion |
| **PySpark / Spark SQL** | Silver layer transformations |
| **pytest** | Unit testing for transformation logic |
| **Databricks Asset Bundles** | Infrastructure-as-Code for job definitions |
| **GitHub Actions** | CI/CD pipeline automation |
| **MLflow** | ML experiment tracking and model registry *(in progress)* |

---

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.
