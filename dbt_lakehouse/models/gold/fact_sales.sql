
{{ config(materialized='table') }}

SELECT
    sd.order_number,
    pr.product_key,
    cu.customer_key,
    sd.order_date,
    sd.ship_date,
    sd.due_date,
    sd.sales_amount,
    sd.quantity,
    sd.price
FROM {{ ref('stg_sales') }} sd
LEFT JOIN {{ ref('dim_products') }} pr
    ON sd.product_number = pr.product_number
LEFT JOIN {{ ref('dim_customers') }} cu
    ON sd.customer_id = cu.customer_id