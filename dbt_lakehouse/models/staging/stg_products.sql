
{{ config(materialized='view') }}

SELECT
    pn.product_id,
    pn.product_number,
    pn.product_name,
    pn.category_id,
    pn.product_cost,
    pn.product_line,
    pn.start_date,
    pn.end_date,
    pc.category,
    pc.subcategory
FROM silver.crm_products pn
LEFT JOIN silver.erp_product_category pc
    ON pn.category_id = pc.category_id