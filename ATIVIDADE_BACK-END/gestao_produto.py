import camera
id_produto = int
nome_produto = str
valor_produto = float
quant_produto = int
status_produto = False

def entrada_produto(nome_produto, valor_produto):
  if status_produto:
    id_produto +=1
    quant_produto +=1
    nome_produto += nome_produto
    valor_produto += valor_produto
    status_produto = True
    return "Produto cadastrado."

def saida_produto(id_produto, nome_produto, status_produto):
  if id_produto != id_produto and nome_produto != nome_produto:
    if status_produto:
      return "Produto não cadastrado."
    else:
      quant_produto -=1
      return "Produto retirado."

def prazo_validade(data_atual, data_produto):
  if data_atual >= data_produto:
    if data_atual > data_produto:
      return "Produto passou do prazo de validade."
    return "Produto está prestes a vencer."
  else:
    return "Prazo de validade do produto está ok."
  
#def debitar_creditar():
#  total += valor_produto