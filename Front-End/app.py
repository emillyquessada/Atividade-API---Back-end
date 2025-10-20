import streamlit as st
import requests

# python -m streamlit run app.py

api_url = "http://127.0.0.1:8000"

st.set_page_config(page_title= "Gerenciador de Produtos e Estoques", page_icon="📦")
st.title("Gerenciador de Produtos e Estoques 🚚")

menu = st.sidebar.radio("Menu de Ações", ["Lista de Produtos", "Adicionar", "Atualizar", "Deletar", "Buscar estoque"])






