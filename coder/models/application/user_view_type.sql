SELECT
    {{ dbt_utils.generate_surrogate_key(['user_view_type']) }} AS user_view_type_id,
    user_view_type AS user_view_type_name
FROM {{ ref('contributors') }}
GROUP BY user_view_type