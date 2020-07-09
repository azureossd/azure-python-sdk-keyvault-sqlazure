import pyodbc
import datetime
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

server = 'your_database.database.windows.net'
database = 'database_name'
username = 'username'

credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url="https://edisga.vault.azure.net", credential=credential)

secret = secret_client.get_secret("AppSecret")
password = secret.value

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
tsql = "SELECT * FROM YourTable"

with cursor.execute(tsql):
  for row in cursor:
    print ('Row:', str(row[0]))