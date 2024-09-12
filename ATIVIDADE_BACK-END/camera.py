status_produto = None

def tirar_foto():
  if status_produto == True:
    return "Produto encontrado."
  else:
    status_produto = False
    return "Produto não encontrado."

