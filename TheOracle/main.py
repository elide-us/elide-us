{
  "app_id": "",
  "client_secret": "",
  "tenant_id": "",
  "openai_key": ""
}

import msal
import requests
import openai

def get_graph_access_token():
  client_id = "YOUR_APP_ID"
  client_secret = "YOUR_CLIENT_SECRET"
  tenant_id = "YOUR_TENANT_ID"
  authority_url = f"https://login.microsoftonline.com/{tenant_id}"
  scopes = ['https://graph.microsoft.com/.default']
  app = msal.ConfidentialClientApplication(client_id, authority=authority_url, client_credential=client_secret)
  token_response = app.acquire_token_for_client(scopes=scopes)
  # access_token = token_response.get('access_token')
  return token_response.get('access_token')

def fetch_emails(access_token):
  graph_api_endpoint = "https://graph.microsoft.com/v1.0/me/messages"
  headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
  }
  response = requests.get(graph_api_endpoint, headers=headers)
  return response.json()

def summarize_email(email_content):
  openai.api_key ="YOUR_OPENAI_API_KEY"
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Summarize the following email: {email_content}",
    max_tokens=100
  )
  return response.choices[0].text.strip()

def main():
    access_token = get_graph_access_token()
    emails = fetch_emails(access_token)

    for email in emails['value']:
        subject = email['subject']
        body = email['body']['content']
        summary = summarize_email(body)
        printf(f"Subject: {subject}")
        printf(f"Summary: {summary}")
    #end for
#end def

if __name__ == "__main__":
    main()
  #end if

#end