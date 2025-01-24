SELECT
    {{ dbt_utils.generate_surrogate_key(['contributors']) }} AS id,
    contributors AS ta_type_name
FROM {{ ref('st_park_p') }}
GROUP BY contributors