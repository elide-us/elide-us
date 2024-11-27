import msal
from azure.storage.blob import BlobServiceClient
import os

class AzureStorageAccess:
    def __init__(self, client_id, client_secret, tenant_id, account_name, container_name):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.account_name = account_name
        self.container_name = container_name
        self.access_token = self.get_access_token()
        self.blob_service_client = self.get_blob_service_client()

    def get_access_token(self):
        authority = f"https://login.microsoftonline.com/{self.tenant_id}"
        app = msal.ConfidentialClientApplication(
            self.client_id,
            client_credential=self.client_secret,
            authority=authority
        )

        scopes = [f"https://{self.account_name}.blob.core.windows.net/.default"]
        result = app.acquire_token_silent(scopes, account=None)

        if not result:
            result = app.acquire_token_for_client(scopes=scopes)

        if "access_token" in result:
            print("Access token acquired")
            return result["access_token"]
        else:
            print("Error acquiring token:", result.get("error"), result.get("error_description"))
            raise Exception("Could not acquire access token.")

    def get_blob_service_client(self):
        # Build the BlobServiceClient with the token
        credential = {
            "account_name": self.account_name,
            "credential": self.access_token
        }
        return BlobServiceClient(account_url=f"https://{self.account_name}.blob.core.windows.net", credential=self.access_token)

    def list_blobs(self):
        container_client = self.blob_service_client.get_container_client(self.container_name)
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            print("Blob name:", blob.name)

    # Placeholder for additional functionality, such as uploading files
    def upload_blob(self, blob_name, data):
        container_client = self.blob_service_client.get_container_client(self.container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data)
        print(f"Uploaded blob {blob_name}")

# Usage
client_id = "a31f643e-0f62-4075-8e2a-da99a1d593fc"
client_secret = ""
tenant_id = "ae3b0eca-5daf-434e-87aa-75de4db416bc"
account_name = "theoraclesa"
container_name = "lumaai"

azure_storage = AzureStorageAccess(client_id, client_secret, tenant_id, account_name, container_name)
azure_storage.list_blobs()

# To upload a blob, you can call the upload_blob method
# azure_storage.upload_blob("new_blob_name.txt", "Data to upload")
