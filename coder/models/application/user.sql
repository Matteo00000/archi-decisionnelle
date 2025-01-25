SELECT 
    id AS user_id,
    avatar_url AS avatar
FROM {{ ref('contributors') }} 
    JOIN {{ ref('user_view_type') }} ON user_view_type = user_view_type_name