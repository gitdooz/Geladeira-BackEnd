from gestao_produto import *

def diminuir_temperatura(temp_atual):
  if temp_atual < 30:
    temp_atual = 4
    return "Temperatura diminuida para 4°C."

def aumentar_temperatura(temp_atual):
  if temp_atual > 4:
    temp_atual = 4
    return "Temperatura aumentada para 4°C"