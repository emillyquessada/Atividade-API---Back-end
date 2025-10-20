import streamlit as st
import requests

# python -m streamlit run app.py

api_url = "http://127.0.0.1:8000"

st.set_page_config(page_title= "Gerenciador de Produtos e Estoques", page_icon="📦")
st.title("Gerenciador de Produtos e Estoques 🚚")

menu = st.sidebar.radio("Menu de Ações", ["Lista de Produtos", "Adicionar", "Atualizar", "Deletar", "Buscar estoque"])

if menu == "Lista de Produtos":
    st.subheader("Catálogo de Produtos: ")
    response = requests.get(f"{api_url}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
    else:
        st.error("Erro ao acessar API")


elif menu == "Adicionar":
    st.subheader("➕ Adicionar Produtos")
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço do Produto")
    quantidade = st.number_input("Quantidade ")
    if st.button("Adicionar Produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{api_url}/produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionando com sucesso!")
        else:
            st.error("Erro ao adicionar o produto")

elif menu == "Atualizar":
    st.subheader("🔄 Atualizar produto")

    id_produto = st.number_input("ID do produto a ser atualizado", step=1)
    preco = st.number_input("Novo preço (opcional)", step=1)
    quantidade = st.number_input("Nova quantidade (opcional)", step=1)

    if st.button("Atualizar Produto"):
        dados = {}
        if preco:
            dados["preco"] = preco
        if quantidade:
            dados["quantidade"] = quantidade

        if not dados:
            st.warning("Preencha um campo para atualizar.")
        else:
            response = requests.put(f"{api_url}/Produtos/{id_produto}", params=dados)

            if response.status_code == 200:
                st.success("Produto atualizado com sucesso!")
            else:
                st.error("Erro ao atualizar o produto.")