# imageRotate.py
# Minimal example of rotating an image retrieved from a URL by 90 degrees

import os
import tempfile
from PIL import Image
from requests import get
from datetime import datetime, timedelta
from azure.storage import (
    AccessPolicy,
    ResourceTypes,
    AccountPermissions,
    CloudStorageAccount,
)
from azure.storage.blob import (
    BlockBlobService,
    ContainerPermissions,
    BlobPermissions,
    PublicAccess,
)

# Set these four environment variables in the container configuration
AZURE_ACC_NAME = os.environ['STORAGEACCOUNTNAME']           # the name of the storage account
AZURE_PRIMARY_KEY = os.environ['STORAGEACCOUNTKEY']         # the storage account's key
AZURE_INPUT_CONTAINER = os.environ['INPUTCONTAINERNAME']    # the name of the container to read from
AZURE_OUTPUT_CONTAINER = os.environ['OUTPUTCONTAINERNAME']  # the name of the container to write to

AZURE_BLOB='20200912_12251-cropped6.jpg'    # filename to read (for testing)

def generate_sas_readonly():
    block_blob_service = BlockBlobService(account_name=AZURE_ACC_NAME, account_key=AZURE_PRIMARY_KEY)    
    sas_url = block_blob_service.generate_blob_shared_access_signature(AZURE_INPUT_CONTAINER,AZURE_BLOB,BlobPermissions.READ,datetime.utcnow() + timedelta(hours=1))
    #print sas_url
    return ('https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_INPUT_CONTAINER+'/'+AZURE_BLOB+'?'+sas_url)

def generate_sas_create():
    block_blob_service = BlockBlobService(account_name=AZURE_ACC_NAME, account_key=AZURE_PRIMARY_KEY)    
    sas_url = block_blob_service.generate_blob_shared_access_signature(AZURE_OUTPUT_CONTAINER,AZURE_BLOB,BlobPermissions.CREATE,datetime.utcnow() + timedelta(hours=1))
    #print sas_url
    return ('https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_OUTPUT_CONTAINER+'/'+AZURE_BLOB+'?'+sas_url)

sasTokenRead = generate_sas_readonly()
print (sasTokenRead)
sasTokenWrite = generate_sas_create()
print (sasTokenWrite)

# tf = tempfile.NamedTemporaryFile(delete=False)

# URL = "https://github.com/hooverken/python-stuff/raw/main/20200912_12251-cropped6.jpg"
# URL = sasToken

# response = get(sasToken)
# tf.write(response.content)
# print(tf.name)
# Image.open(tf.name).rotate(90).show()
