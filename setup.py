import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.api_core import client_options

def create_service_account_key():
    # Create credentials
    credentials = service_account.Credentials.from_service_account_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/webmasters.readonly']
    )

    # Build the service
    service = build('searchconsole', 'v1', credentials=credentials)

    try:
        # Test the credentials by listing sites
        sites = service.sites().list().execute()
        print('Credentials are working! Found sites:', sites)
        return True
    except Exception as e:
        print('Error testing credentials:', str(e))
        return False

def main():
    if os.path.exists('credentials.json'):
        print('Testing existing credentials...')
        if create_service_account_key():
            print('Setup complete! You can now use these credentials with the MCP.')
        else:
            print('Credentials test failed. Please check your Google Cloud Console setup.')
    else:
        print('No credentials.json file found.')
        print('Please follow these steps:')
        print('1. Go to https://console.cloud.google.com')
        print('2. Create a new project or select an existing one')
        print('3. Enable the Search Console API')
        print('4. Go to IAM & Admin > Service Accounts')
        print('5. Create a new service account')
        print('6. Download the JSON key file')
        print('7. Rename it to credentials.json and place it in this directory')
        print('8. Run this script again')

if __name__ == '__main__':
    main()