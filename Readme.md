# Steps

## Prerequisites:
> Update Az CLI using curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

1. az login
2. Create a SP

```bash
  az ad sp create-for-rbac -n "PythonAppLinux" --skip-assignment
```

```log
  {                                                      
    "appId": "28d044ea-809b-4c0a-b8c8-5413e526a206",     
    "displayName": "PythonAppLinux",                     
    "name": "http://PythonAppLinux",                     
    "password": "*********i08TW0J4-~6",    
    "tenant": "*******-91ab-2d7cd011db47"     
  }                                                      
```
2. Create policies:

```bash
  az keyvault set-policy --name "edisga" --spn 28d044ea-809b-4c0a-b8c8-5413e526a206 --key-permissions decrypt sign
  az keyvault set-policy --name "edisga" --spn 28d044ea-809b-4c0a-b8c8-5413e526a206 --secret-permissions get
```

3.Then go to your Azure Keyvault and add a secret named **AppSecret** with your Azure SQL db password.

  - To run this in Linux VM:
  > Follow this article https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#ubuntu17
  > Also install this one to build pyodbc: `sudo apt-get install python3-dev`

4. Set environment credentials:

AZURE_CLIENT_ID
AZURE_TENANT_ID
AZURE_CLIENT_SECRET

5. Create virtual env
6. Install requirements.txt with `pip install -r requirements.txt`
7. Run the app with `python index.py`