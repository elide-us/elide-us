# app_id = 
# client_secret = 
# tenant_id = 

import msal
import requests
import openai

client_id = "YOUR_APP_ID"
client_secret = "YOUR_CLIENT_SECRET"
tenant_id = "YOUR_TENANT_ID"

authority_url = f"https://login.microsoftonline.com/{tenant_id}"
scopes = ['https://graph.microsoft.com/.default']

app = msal.ConfidentialClientApplication(client_id, authority=authority_url, client_credential=client_secret)

token_response = app.acquire_token_for_client(scopes=scopes)
access_token = token_response.get('access_token')

def fetch_emails(access_token)
  graph_api_endpoint = "https://graph.microsoft.com/v1.0/me/messages"
  headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
  }
  response = requests.get(graph_api_endpoint, headers=headers)
  return response.json()

