SELECT 
    count(*) as complaints_per_week,
    TIMESTAMP_TRUNC(created_date, WEEK) as week
FROM {{ ref("f__complaints") }}
GROUP BY 2
