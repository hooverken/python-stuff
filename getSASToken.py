import time
import uuid
import hmac
import base64
import hashlib
import urllib
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

AZURE_ACC_NAME = '<account_name>'
AZURE_PRIMARY_KEY = '<account_key>'
AZURE_CONTAINER = '<container_name>'
AZURE_BLOB='<blob_name>'

def generate_sas_with_sdk():
    block_blob_service = BlockBlobService(account_name=AZURE_ACC_NAME, account_key=AZURE_PRIMARY_KEY)    
    sas_url = block_blob_service.generate_blob_shared_access_signature(AZURE_CONTAINER,AZURE_BLOB,BlobPermissions.READ,datetime.utcnow() + timedelta(hours=1))
    #print sas_url
    print 'https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_CONTAINER+'/'+AZURE_BLOB+'?'+sas_url

generate_sas_with_sdk()