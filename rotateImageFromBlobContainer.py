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
try:
    tempFile.write(inputfile_blob_client.download_blob().readall())
except ResourceNotFoundError:
    print("Blob not found.")

pieces = AZURE_BLOB.split('.')
pieceCount = len(pieces)
inputFileNameExtension = pieces[pieceCount-1]
tempFile = tempfile.NamedTemporaryFile(suffix=inputFileNameExtension)

print("Input file has type " + inputFileNameExtension)
Image.open(tempFile).rotate(90).save(tempFile)

print("Rotated image saved to: " + tempFile.name)

# Create a blob client using the local file name as the name for the blob
outputfile_blob_client = blob_service_client.get_blob_client(container=AZURE_OUTPUT_CONTAINER, blob=tempFile.name)

print("\nUploading to Azure Storage as blob:\n\t" + tempFile.name)

# Upload the created file
with open(tempFile, "rb") as data:
    outputfile_blob_client.upload_blob(data)

print("Upload of " + tempFile.name + " to Azure Storage complete.\n")
