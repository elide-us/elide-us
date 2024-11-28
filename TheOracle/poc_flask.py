import json
import msal
import requests

from openai import OpenAI

from datetime import datetime, timedelta

from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

def load_config():
    with open("config.json", "r") as file:
        config = json.load(file)
    print(f"Loaded config.json")
    print(f"Config contains {len(config)} values")
    return config

@app.route('/')
def index():
    config = load_config()
    client_id = config["app_id"]
    client_secret = config["client_secret"]
    tenant_id = config["tenant_id"]
    redirect_uri = config["redirect_uri"]
    authority_url = f"https://login.microsoftonline.com/{tenant_id}"
    scopes = ['https://graph.microsoft.com/Mail.Read']

    # Create a confidential client application
    app = msal.ConfidentialClientApplication(
        client_id,
        authority=authority_url,
        client_credential=client_secret
    )

    # Generate the authorization URL
    auth_url = app.get_authorization_request_url(scopes, redirect_uri=redirect_uri)
    return redirect(auth_url)

@app.route('/getAToken')
def get_a_token():
    config = load_config()
    client_id = config["app_id"]
    client_secret = config["client_secret"]
    tenant_id = config["tenant_id"]
    redirect_uri = config["redirect_uri"]
    authority_url = f"https://login.microsoftonline.com/{tenant_id}"
    scopes = ['https://graph.microsoft.com/Mail.Read']

    # Create a confidential client application
    app = msal.ConfidentialClientApplication(
        client_id,
        authority=authority_url,
        client_credential=client_secret
    )

    # Get the authorization code from the redirect URI
    code = request.args.get('code')

    # Exchange the authorization code for an access token
    token_response = app.acquire_token_by_authorization_code(code, scopes=scopes, redirect_uri=redirect_uri)

    if "access_token" in token_response:
        access_token = token_response['access_token']
        email_json = fetch_emails_last_48_hours(access_token)
        if email_json:
            summary = summarize_email(email_json, config)
            return jsonify({"summary": summary})
        else:
            return "Error fetching emails"
    else:
        return "Error obtaining access token"

def fetch_emails_last_48_hours(access_token):
    print("Getting emails from the last 48 hours from v1.0/me/messages")
    graph_api_endpoint = "https://graph.microsoft.com/v1.0/me/messages"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Calculate the date and time for 48 hours ago
    time_48_hours_ago = datetime.utcnow() - timedelta(hours=48)
    time_48_hours_ago_str = time_48_hours_ago.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    params = {
        '$filter': f"receivedDateTime ge {time_48_hours_ago_str}",
        '$orderby': 'receivedDateTime desc'
    }
    
    response = requests.get(graph_api_endpoint, headers=headers, params=params)
    
    # Diagnostic information
    print(f"HTTP Status Code: {response.status_code}")
    if response.status_code == 200:
        print("API call successful")
        emails = response.json()
        print(f"Number of emails retrieved: {len(emails.get('value', []))}")
        
        # Create a list to store the email details
        email_list = []
        
        # Process each email
        for email in emails.get('value', []):
            subject = email.get('subject', 'No Subject')
            from_name = email.get('from', {}).get('emailAddress', {}).get('name', 'No Name')
            from_address = email.get('from', {}).get('emailAddress', {}).get('address', 'No Address')
            body_preview = email.get('bodyPreview', 'No Preview')
            
            email_details = {
                'subject': subject,
                'from': {
                    'name': from_name,
                    'address': from_address
                },
                'bodyPreview': body_preview
            }
            
            email_list.append(email_details)
        
        # Convert the list to a JSON object
        email_json = json.dumps(email_list, indent=2)
        print(email_json)
        
        return email_json
    else:
        print("API call failed")
        print(f"Response: {response.text}")
    
    return None

def fetch_last_email(access_token):
    print("Getting the last email from v1.0/me/messages")
    graph_api_endpoint = "https://graph.microsoft.com/v1.0/me/messages"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        '$orderby': 'receivedDateTime desc',
        '$top': 1
    }
    
    response = requests.get(graph_api_endpoint, headers=headers, params=params)
    
    # Diagnostic information
    print(f"HTTP Status Code: {response.status_code}")
    if response.status_code == 200:
        print("API call successful")
        emails = response.json()
        print(f"Number of emails retrieved: {len(emails.get('value', []))}")
        
        # Process the last email
        if emails.get('value'):
            email = emails['value'][0]
            subject = email.get('subject', 'No Subject')
            from_name = email.get('from', {}).get('emailAddress', {}).get('name', 'No Name')
            from_address = email.get('from', {}).get('emailAddress', {}).get('address', 'No Address')
            body_preview = email.get('bodyPreview', 'No Preview')
    
            print(f"Subject: {subject}")
            print(f"From: {from_name} <{from_address}>")
            print(f"Body Preview: {body_preview}")
            print("-" * 40)
        else:
            print("No emails found.")
    else:
        print("API call failed")
        print(f"Response: {response.text}")
    
    return response.json()

def summarize_email(email_json, config):
    client = OpenAI(api_key=config["openai_secret"])
    prompt = f"Summarize the following emails from the last two days as a brief podcast:\n\n{email_json}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an entertaining and humorous podcaster."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()



if __name__ == "__main__":
  app.run(debug=True)

