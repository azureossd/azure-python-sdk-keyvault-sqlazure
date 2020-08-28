# Steps

## Prerequisites:
> Update Az CLI using curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

1. az login
2. Create a Service Principal

```bash
  az ad sp create-for-rbac -n "<spname>" --skip-assignment
```
Sample output:
```log
  {                                                      
    "appId": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",     
    "displayName": "PythonAppLinux",                     
    "name": "http://PythonAppLinux",                     
    "password": "****************",    
    "tenant": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx"     
  }                                                      
```
2. Create policies:

```bash
  az keyvault set-policy --name "<policyname>" --spn <appId> --key-permissions decrypt sign
  az keyvault set-policy --name "<policyname>" --spn <appId> --secret-permissions get
```

3.Then go to your Azure Keyvault and add a secret named **AppSecret** with your Azure SQL db password.

  - To run this in Linux VM:
  > Follow this article https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#ubuntu17
  > 
  > Also install this one to build pyodbc: `sudo apt-get install python3-dev`

4. Set environment credentials:

    AZURE_CLIENT_ID

    AZURE_TENANT_ID

    AZURE_CLIENT_SECRET

5. Create virtual env.
6. Install requirements.txt with `pip install -r requirements.txt`
7. Run the app with `python index.py`
