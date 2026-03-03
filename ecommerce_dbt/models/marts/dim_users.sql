{{ config(
    materialized='incremental',
    unique_key='user_id'
) }}

WITH source_data AS (

    SELECT
        user_id,
        name,
        email,
        country,
        signup_date
    FROM {{ ref('stg_users') }}

),

existing AS (

    SELECT *
    FROM {{ this }}

)

SELECT
    s.user_id,
    s.name,
    s.email,
    s.country,
    s.signup_date,
    CURRENT_TIMESTAMP AS effective_from,
    NULL AS effective_to,
    TRUE AS is_current

FROM source_data s

{% if is_incremental() %}

LEFT JOIN existing e
    ON s.user_id = e.user_id
    AND e.is_current = TRUE

WHERE
    e.user_id IS NULL
    OR s.country != e.country
    OR s.email != e.email

{% endif %}