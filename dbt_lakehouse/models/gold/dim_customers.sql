
{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY ci.customer_id) AS customer_key,
    ci.customer_id,
    ci.customer_number,
    ci.first_name,
    ci.last_name,
    ci.country,
    ci.marital_status,
    ci.gender,
    ci.created_date
FROM {{ ref('stg_customers') }} ci