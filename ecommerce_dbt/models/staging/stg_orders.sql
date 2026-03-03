SELECT
    CAST(order_id AS INTEGER) AS order_id,
    CAST(user_id AS INTEGER) AS user_id,
    CAST(product_id AS INTEGER) AS product_id,
    CAST(quantity AS INTEGER) AS quantity,
    CAST(order_timestamp AS TIMESTAMP) AS order_timestamp
FROM raw_layer.orders