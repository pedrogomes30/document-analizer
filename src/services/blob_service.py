import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utils.config import Config

def upload_blob(file, file_name):
    try:        
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        
        blob_client = blob_service_client.get_blob_client(Config.CONTAINER_NAME, file_name)
        
        blob_client.upload_blob(file, overwrite=True)
        
        print('save into:',blob_client.url)
        return blob_client.url
    except Exception as ex:
        st.write(f"Erro ao enviar o arquivo {file_name} para o blob storage: {ex}")
        return None
    