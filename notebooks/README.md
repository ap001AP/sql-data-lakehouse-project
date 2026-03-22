# Databricks Notebooks

These notebooks are deployed to Databricks via the Asset Bundle job defined in `lakehouse_v2/resources/lakehouse_v2_job.yml`.

| Notebook | Purpose |
|---|---|
| `bronze_jdbc_ingestion` | Ingests 6 ERP/CRM tables from PostgreSQL into Bronze Delta tables |
| `bronze_api_ingestion` | Pulls REST Countries API data into Bronze Delta tables |
| `bronze_kafka_streaming` | Consumes Kafka sales events into Bronze Delta tables via Structured Streaming |
| `kafka_producer` | Publishes fake sales events to Kafka topic for testing |