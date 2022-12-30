
from google.cloud import bigquery

query = "SELECT * FROM `bigquery-public-data.new_york_mv_collisions.nypd_mv_collisions`WHERE borough IS NOT null"
client = bigquery.Client(project = project_id)
df = client.query(query).to_dataframe()