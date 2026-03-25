
{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY pn.start_date, pn.product_number) AS product_key,
    pn.product_id,
    pn.product_number,
    pn.product_name,
    pn.category_id,
    pn.category,
    pn.subcategory,
    pn.product_line,
    pn.start_date
FROM {{ ref('stg_products') }} pn