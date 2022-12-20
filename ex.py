print(1+2)
3+4

print("hi!")

a = 1
b = 2.345

f"my number is {a} and I love it! I also love {b:.2f}"
from google.cloud import bigquery

client = bigquery.Client(project = project_id)
df = client.query(query).to_dataframe()