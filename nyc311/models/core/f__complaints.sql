SELECT
  unique_key,
  created_date,
  closed_date,
  TIMESTAMP_DIFF(closed_date, created_date, HOUR) as total_time
FROM {{ref("stg__nyc_311")}}
