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

default_credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net", credential=default_credential)

inputfile_blob_client = blob_service_client.get_blob_client(container=AZURE_INPUT_CONTAINER, blob=AZURE_BLOB)

with open(AZURE_BLOB, "wb") as my_blob:
    download_stream = inputfile_blob_client.download_blob()
    my_blob.write(download_stream.readall())

# Open the file and rotate the image 90 degrees (counterclockwise), then save it using the new name
NEW_BLOB_NAME = "ROTATED-" + AZURE_BLOB
Image.open(AZURE_BLOB).rotate(90).save(NEW_BLOB_NAME)

print("Rotated image saved to: " + NEW_BLOB_NAME)

# Create a blob client using the local file name as the name for the blob
outputfile_blob_client = blob_service_client.get_blob_client(container=AZURE_OUTPUT_CONTAINER, blob=NEW_BLOB_NAME)

print("\nUploading to Azure Storage as blob:\n\t" + NEW_BLOB_NAME)

# Upload the created file
with open(NEW_BLOB_NAME, "rb") as data:
    outputfile_blob_client.upload_blob(data)

print("Upload of " + NEW_BLOB_NAME + " to Azure Storage complete.\n")
