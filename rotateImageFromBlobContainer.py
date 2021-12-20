# imageRotate.py
# Minimal example of rotating an image retrieved from a URL by 90 degrees

import os
import tempfile
from PIL import Image
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Set these environment variables in the container configuration
AZURE_STORAGE_ACCOUNT_NAME = os.environ['STORAGEACCOUNTNAME']   # the target storage account name
AZURE_INPUT_CONTAINER = os.environ['INPUTCONTAINERNAME']        # the name of the container to read from
AZURE_OUTPUT_CONTAINER = os.environ['OUTPUTCONTAINERNAME']      # the name of the container to write to

AZURE_BLOB='20200912_12251-cropped6.jpg'    # filename to read (for testing)

token_credential = DefaultAzureCredential()

# blob_service_client = BlobServiceClient.get_blob_client(
#     account_url="https://" + AZURE_STORAGE_ACCOUNT_NAME + ".blob.core.windows.net",
#     credential=token_credential
# )

blob_service_client = BlobServiceClient(account_url=self.oauth_url, credential=token_credential)

tempFile = tempfile.NamedTemporaryFile()

blob_client = blob_service_client.get_blob_client(container=AZURE_INPUT_CONTAINER, blob=AZURE_BLOB)
try:
    blob_data = blob_client.download_blob()
except ResourceNotFoundError:
    print("Blob not found.")

print(tempFile.name)
Image.open(tempFile.name).show()
