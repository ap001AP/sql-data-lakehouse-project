# Data Lakehouse — Version 2

## Overview
Version 2 of the Data Lakehouse project builds on top of [Data Lakehouse v1](https://github.com/ap001AP/sql-data-lakehouse-project/tree/main?tab=readme-ov-file) by evolving the architecture from a manually operated pipeline into a **production-grade, automated data platform**.

Version 3: [View V3](https://github.com/ap001AP/sql-data-lakehouse-project/tree/lakehouse_v3)

---

## What's New in V2

- **Live Database Ingestion**: Replaced manual CSV ingestion with a live PostgreSQL operational database (hosted on Render) using a Python database connector that automatically ingests 6 ERP and CRM tables (115,000+ rows) directly into Bronze Delta tables.
- **REST API Ingestion**: Built a REST API ingestion framework that pulls live data from the REST Countries API, parses nested JSON responses into flat Delta tables, and enriches the customer dimension with geographic metadata including region, population, currency, and language data.
- **Kafka Streaming**: Implemented near real-time data ingestion using Apache Kafka (Aiven) and Spark Structured Streaming — sales events are published to a Kafka topic and continuously consumed into Bronze Delta tables with fault-tolerant checkpointing.
- **Infrastructure-as-Code**: Migrated pipeline orchestration to Databricks Asset Bundles, defining Bronze, Silver, and Gold jobs as versioned YAML configuration across `dev` and `prod` environments.
- **CI/CD Pipeline**: Implemented a GitHub Actions workflow with two sequential stages — unit tests must pass before deployment is triggered, ensuring code quality is enforced on every push.
- **Unit Tests**: Built a pytest unit test suite with 15 tests covering Silver layer transformation logic including gender normalization, marital status encoding, date parsing, and null handling.

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
Gold Layer — Star schema (fact_sales, dim_customers, dim_products)
```

---

## CI/CD Pipeline

Every push to `lakehouse_v2` branch triggers:
```
Push to GitHub
      ↓
Run 15 unit tests (pytest)
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
| **PostgreSQL** | Operational source database (Render) |
| **Apache Kafka** | Real-time streaming via Aiven managed Kafka |
| **Spark Structured Streaming** | Continuous Kafka to Delta ingestion |
| **PySpark / Spark SQL** | Data transformations |
| **pytest** | Unit testing for transformation logic |
| **Databricks Asset Bundles** | Infrastructure-as-Code for job definitions |
| **GitHub Actions** | CI/CD pipeline automation |

---

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.
