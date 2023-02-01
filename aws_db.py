import boto3
import cx_Oracle

# Connect to secrets manager
client = boto3.client('secretsmanager')

# Get the oracle database details
secret = client.get_secret_value(SecretId='oracle_database_details')

# Extract the values
secret_value = secret['SecretString']
db_user = secret_value['user']
db_password = secret_value['password']
db_identifier = secret_value['dbidentifier']

# Connect to the oracle database
conn = cx_Oracle.connect(db_user, db_password, db_identifier)

# Execute a sample SQL query
cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
cursor.close()
conn.close()
