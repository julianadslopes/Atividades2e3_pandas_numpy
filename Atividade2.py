# Atividade 2: ASSISTENTE DE COMPRAS

import os
import pandas as pd

os.system ("cls")

# 1 - série com as quantidades em estoque, para os seguintes produtos: Camiseta, Calça, Jaqueta, Vestido e Boné.

produtos = ["camiseta", "calça", "jaqueta", "vestido", "boné"]
quantidade = [50, 30, 15, 10, 25]

estoque = pd.Series(quantidade, index = produtos)

print ("ESTOQUE \n")
print (estoque)
print (30 * "=", "\n")

# 2- Adicione uma nova peça de roupa à série  e defina o valor como None
estoque.loc ["blusa"] = None 

print ("ESTOQUE ATUALIZADO")
print (estoque)
print (30 * "=", "\n")

# 3- produtos que possuem mais de 20 unidades em estoque 
print ("PRODUTOS COM MAIS DE 20 UNIDADES: ")
print (estoque[estoque >20])
print (30 * "=", "\n")

# 4- preços
df_estoque = pd.DataFrame(estoque, columns=['quantidade']) # transformando a série em dataframe
preco = pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)
df_estoque['preco'] = preco 
print ("ESTOQUE COM PREÇO")
print (df_estoque)
print (30 * "=", "\n")

# 5- Calcule o valor total do estoque e exiba esse valor

print ("VALOR TOTAL DO ESTOQUE POR PRODUTO")
valor_estoque = preco*quantidade
print(valor_estoque)

print("\nVALOR TOTAL DO ESTOQUE")
valor_total = valor_total = valor_estoque.sum()
print(valor_total)