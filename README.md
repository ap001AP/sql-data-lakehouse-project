# Data Lakehouse — Version 2 (In Progress)

> **Note**: This project is actively under development. This README will be updated as new features are completed.

---

## Overview

Version 2 of the Data Lakehouse project builds on top of [Data Lakehouse v1](#) by evolving the architecture from a manually operated pipeline into a **production-grade, automated data platform**.

---

## What's New in V2

### Completed
- **Live Database Ingestion**: Replaced manual CSV ingestion with a live PostgreSQL operational database connection using Python database connectors, enabling automated direct ingestion into Bronze Delta Lake tables.
- **Infrastructure-as-Code**: Migrated pipeline orchestration to Databricks Asset Bundles, defining Bronze, Silver, and Gold jobs as versioned YAML configuration across `dev` and `prod` environments.
- **CI/CD Pipeline**: Implemented GitHub Actions workflow that automatically validates and deploys the full Databricks bundle to the dev environment on every push, eliminating all manual deployment steps.

### 🔄 In Progress
- **REST APIs**: Exposing data layers via APIs for downstream consumption.
- **Kafka Integration**: Adding real-time streaming ingestion using Apache Kafka.
- **CI/CD Expansion**: Extending the pipeline to cover production deployments.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| **Databricks** | Unified analytics and pipeline platform |
| **Delta Lake** | Storage format for all Lakehouse layers |
| **Unity Catalog** | Data governance and schema management |
| **PostgreSQL** | Operational source database |
| **Python** | Database connectors and ingestion scripts |
| **PySpark / Spark SQL** | Data transformations |
| **Databricks Asset Bundles** | Infrastructure-as-Code for job definitions |
| **GitHub Actions** | CI/CD pipeline automation |
| **Apache Kafka** | Real-time streaming *(coming soon)* |

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.