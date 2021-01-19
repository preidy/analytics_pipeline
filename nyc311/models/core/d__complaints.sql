SELECT
  unique_key,
  agency_name,
  complaint_type,
  borough
FROM {{ref("stg__nyc_311")}}
