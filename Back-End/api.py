from fastapi import FastAPI
import funcao
# python -m uvicorn api:app --reload

app= FastAPI(title="Gerenciador de Produtos e Estoques")

@app.get("/")
def home():
    return {"mensagem": " Seja bem vindo ao Gerenciador de Produtos e Estoques!"}

@app.post("/produtos")
def criar_produtos(nome:str, categoria: str, preco: float, quantidade: int):
    funcao.inserir_produtos(nome, categoria, preco, quantidade)
    return {"mensagem": " Produto adicionado com sucesso!"}

@app.get("/produtos")
def listar_produto():
    produtos = funcao.listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
    return {"produtos": lista}













