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

blob_service_client = BlobServiceClient.get_blob_client(
    account_url="https://" + AZURE_STORAGE_ACCOUNT_NAME + ".blob.core.windows.net",
    credential=token_credential
)

# blob_service_client = BlobServiceClient.from_blob_url(blob_url=BlobServiceClient.url, container_name = AZURE_INPUT_CONTAINER, blob_name = AZURE_BLOB, credential = token_credential)

tempFile = tempfile.NamedTemporaryFile()

with open(tempFile.name, "wb") as my_blob:
    blob_data = blob_service_client.download_blob(my_blob)
    blob_data.readinto(my_blob)

print(tempFile.name)
print(my_blob.name)