from example.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account key file
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

# Define the scopes required
SCOPES = ['https://www.example.com/auth/drive.metadata.readonly',
          'https://www.example.com/auth/drive.readonly']

# Authenticate and create the service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)
