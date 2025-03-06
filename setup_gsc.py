from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import os

def create_credentials():
    # Configuration du projet
    project_config = {
        "type": "service_account",
        "project_id": "mcp-search-console",
        "private_key_id": "",
        "private_key": "",
        "client_email": "",
        "client_id": "",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": ""
    }

    # Sauvegarde de la configuration
    with open('credentials.json', 'w') as f:
        json.dump(project_config, f)

    print("Configuration de base créée dans credentials.json")
    print("\nÉtapes suivantes :")
    print("1. Allez sur https://console.cloud.google.com")
    print("2. Créez un nouveau projet ou sélectionnez un projet existant")
    print("3. Activez l'API Search Console")
    print("4. Créez un compte de service et téléchargez le fichier JSON")
    print("5. Copiez les valeurs du fichier JSON téléchargé dans credentials.json")
    print("6. Relancez ce script pour tester la configuration")

def test_credentials():
    try:
        credentials = service_account.Credentials.from_service_account_file(
            'credentials.json',
            scopes=['https://www.googleapis.com/auth/webmasters.readonly']
        )
        
        service = build('searchconsole', 'v1', credentials=credentials)
        sites = service.sites().list().execute()
        
        print("✅ Credentials configurés avec succès!")
        print("Sites disponibles:", sites)
        return True
    except Exception as e:
        print("❌ Erreur lors du test des credentials:", str(e))
        return False

def main():
    if not os.path.exists('credentials.json'):
        create_credentials()
    else:
        if test_credentials():
            print("\nVous pouvez maintenant utiliser ce fichier credentials.json dans la configuration du MCP.")
        else:
            print("\nVérifiez votre configuration et réessayez.")

if __name__ == '__main__':
    main()