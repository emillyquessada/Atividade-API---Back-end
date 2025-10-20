import streamlit as st
import requests

# python -m streamlit run app.py

api_url = "http://127.0.0.1:8000"

st.set_page_config(page_title= "Gerenciador de Produtos e Estoques", page_icon="📦")
st.title("Gerenciador de Produtos e Estoques 🚚")

menu = st.sidebar.radio("Menu de Ações", ["Lista de Produtos", "Adicionar", "Atualizar", "Deletar", "Buscar Estoque"])

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

    id_produto = st.number_input("ID do produto a ser atualizado", min_value=1, step=1)
    preco = st.number_input("Novo preço (opcional)", step=0.01)
    quantidade = st.number_input("Nova quantidade (opcional)", step=1)

    if st.button("Atualizar Produto"):
        dados = {"id_produto": id_produto,"preco": preco, "quantidade": quantidade}
        url = f"{api_url}/atualizar"
        st.write(f"URL chamada: {url}")  # Debug para verificar URL
        response = requests.put(url, params=dados)

        st.write("Status Code:", response.status_code)
        st.write("Resposta da API:", response.text)

        if response.status_code == 200:
            st.success("Produto atualizado com sucesso!")
        else:
            st.error(f"Erro ao atualizar o produto. Detalhes: {response.text}")

elif menu == "Deletar":
    st.subheader("🗑️ Excluir produto")

    id_produto = st.number_input("Digite o ID do produto para ser excluído", min_value=1,  step=1)

    if st.button("Excluir Produto"):
        if id_produto > 0:
            dados = {"id_produto": id_produto}
            url = f"{api_url}/deletar"
            st.write(f"URL chamada: {url}")  # Debug para verificar URL
            response = requests.delete(url,params=dados)

            st.write("Status Code:", response.status_code)
            st.write("Resposta da API:", response.text)

            if response.status_code == 200:
                st.success("Produto excluído com sucesso!")
            else:
                st.error(f"Erro ao excluir o produto. Detalhes: {response.text}")
        else:
            st.warning("Informe um ID válido do produto.")

elif menu == "Buscar Estoque":
    st.subheader(" 🛒 Buscar no Estoque ")
    id_produto = st.number_input("Digite o ID do produto para busca-lo:", min_value=1, step=1)
    if st.button("Buscar produto"):
        if id_produto > 0:
            url = f"{api_url}/buscar"
            response = requests.get(url, params={"id_produto": id_produto})
            if response.status_code == 200:
                produto = response.json().get("produto")  
                if produto:
                    st.write("Produto encontrado:")
                    st.dataframe(produto)
                    st.success("Produto encontrado com sucesso!")
                else:
                    st.warning("Produto não encontrado.")
        else:
            st.error("Digite um ID de produto válido (maior que 0).")
