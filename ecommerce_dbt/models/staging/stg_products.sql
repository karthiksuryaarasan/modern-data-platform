SELECT
    CAST(product_id AS INTEGER) AS product_id,
    product_name,
    category,
    CAST(price AS DOUBLE) AS price
FROM raw_layer.products