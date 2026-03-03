{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

SELECT
    o.order_id,
    o.user_id,
    o.product_id,
    o.quantity,
    o.order_timestamp,
    p.price,
    o.quantity * p.price AS total_amount
FROM {{ ref('stg_orders') }} o
LEFT JOIN {{ ref('stg_products') }} p
    ON o.product_id = p.product_id

{% if is_incremental() %}
WHERE o.order_timestamp > (SELECT MAX(order_timestamp) FROM {{ this }})
{% endif %}