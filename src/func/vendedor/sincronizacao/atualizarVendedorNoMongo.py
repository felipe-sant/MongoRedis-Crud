from src.model.vendedor import Vendedor
from src.utils.vendedorParaJson import vendedorParaJson
from src.data.mongo.func.atualizar import atualizarMongo
from src.menu.crudProdutos import crudProdutos

def atualizarVendedorNoMongo(id, vendedor: Vendedor, vendedorNovo: Vendedor):
    vendedorNovo.id = ""
    vendedor.atualizar(vendedorNovo)
    opcao = str(input("Deseja adicionar produtos? (s/n) "))
    if opcao == "s":
        crudProdutos(vendedor, True)
    vendedorJson = vendedorParaJson(vendedor, False)
    try:
        atualizarMongo("vendedor", vendedorJson, {"_id": id})
        return "Vendedor atualizado com sucesso!"
    except Exception as e:
        return f"Erro: {e}"