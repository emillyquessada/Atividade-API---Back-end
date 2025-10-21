from fastapi import FastAPI
import funcao
# python -m uvicorn api:app --reload

app= FastAPI(title="Gerenciador de Produtos e Estoques")

@app.get("/")
def home():
    return {"mensagem": "Seja bem vindo ao Gerenciador de Produtos e Estoques!"}

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

@app.put("/atualizar")
def atualizar_produto(id_produto: int, preco:float, quantidade: int):
    atualizar = funcao.buscar_quantidade(id_produto)
    if atualizar:
        funcao.atualizar_produtos(id_produto, preco, quantidade)
        return {"mensagem": "Preço/Quantidade atualizada com sucesso!"}
    else:
        return{"erro": " Não foi possível atualizar o produto"}

@app.delete("/deletar")
def deletar_produto(id_produto):
    deletar = funcao.deletar_produtos(id_produto)
    if deletar:
        return {"mensagem": " Produto deletado com sucesso!"}
    else:
        return {"erro": "Não foi possível deletar o produto"}

@app.get("/buscar")
def buscar_quantidade(id_produto: int):
    produto = funcao.buscar_quantidade(id_produto)
    if produto:
        return {
            "produto": {
                "nome": produto[0],
                "quantidade": produto[1]
            }
        }








