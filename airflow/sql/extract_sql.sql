SELECT 
  *
FROM `bigquery-public-data.new_york_311.311_service_requests` 
WHERE created_date > '2020-12-01' and created_date < '2021-01-01'
