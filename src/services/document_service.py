from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def analyze_document(blob_url):
    try:
        credential = AzureKeyCredential(Config.KEY)
        document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        request = AnalyzeDocumentRequest(
            url_source=blob_url,
        )
        result = document_client.begin_analyze_document("prebuilt-creditCard", request)
        
        result = result.result()

        print (result.content)
        for document in result.documents:
            fields = document.get('fields', {})
            return {
                "card_name": fields.get("CardholderName", {}).get("content"),
                "card_number": fields.get("CardNumber", {}).get("content"),
                "expiry_date": fields.get("ExpirationDate", {}).get("content"),    
                "bank_name": fields.get("IssuerName", {}).get("content"),
            }
        
    except Exception as ex:
        print(f"Erro ao analisar o documento: {ex}")
        return None

