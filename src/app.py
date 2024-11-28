import streamlit as st

def configure_interface():
    st.setTitle("upload de arquivos IA-102 python - azure")
    uploaded_file = st.uploader("Ecolha um arquivo",type=["png","jpeg","jpg"])

if __name__ == "__main__":
    configure_interface()
