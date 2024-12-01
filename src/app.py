import streamlit as st
from services.blob_service import upload_blob
from services.document_service import analyze_document

def configure_interface():
    st.title("upload de arquivos IA-102 python - azure")
    uploaded_file = st.file_uploader("Ecolha um arquivo", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        # enviar apra o blob storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url is not None:
            st.write(f"Arquivo {fileName} enviado com sucesso para o blob storage")
            credit_cart_info = analyze_document(blob_url)
            show_image_and_validation(blob_url, credit_cart_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o blob storage")

def show_image_and_validation(blob_url, credit_cart_info):
    st.image(blob_url, use_container_width=True, caption="Imagem enviada")
    st.write("Resultado da validação:")
    if credit_cart_info is not None:
        st.markdown(f"<h1 style='color: green;'>Cartão de crédito válido</h1>", unsafe_allow_html=True)
        st.markdown(f"Nome do titular: {credit_cart_info['card_name']}")
        st.markdown(f"Banco emissor: {credit_cart_info['bank_name']}")
        st.markdown(f"data de validade: {credit_cart_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão de crédito inválido</h1>", unsafe_allow_html=True)
        st.write("Não foi possível validar o cartão de crédito")
        

if __name__ == "__main__":
    configure_interface()
