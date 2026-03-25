
{{ config(materialized='view') }}

WITH ranked_customers AS (
    SELECT
        ci.customer_id,
        ci.customer_number,
        ci.first_name,
        ci.last_name,
        ci.marital_status,
        ci.gender,
        ci.created_date,
        la.country,
        ROW_NUMBER() OVER (
            PARTITION BY ci.customer_id
            ORDER BY ci.created_date DESC
        ) AS row_num
    FROM silver.crm_customers ci
    LEFT JOIN silver.erp_customer_location la
        ON ci.customer_number = la.customer_number
)

SELECT
    customer_id,
    customer_number,
    first_name,
    last_name,
    marital_status,
    gender,
    created_date,
    country
FROM ranked_customers
WHERE row_num = 1