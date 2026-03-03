SELECT
    CAST(user_id AS INTEGER) AS user_id,
    name,
    email,
    country,
    CAST(signup_date AS DATE) AS signup_date
FROM raw_layer.users