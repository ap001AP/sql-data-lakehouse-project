
{{ config(materialized='view') }}

SELECT
    order_number,
    product_number,
    customer_id,
    order_date,
    ship_date,
    due_date,
    COALESCE(sales_amount, quantity * price) AS sales_amount,
    quantity,
    price
FROM silver.crm_sales