# Atividade 3: ANALISTA DE VENDAS
import os
import pandas as pd
import numpy as np

os.system ("cls")


# 1- Carregando os dados da planilha
df_vendas = pd.read_excel('vendas_roupas.xlsx')

# 2- exibindo as 10 primeiras linhas do DataFrame
print (df_vendas.head(10))
print (100 * "=")

# 3- Operações
# # Somatório das quantidades vendidas
print( f"\n O total de unidades vendidas foi {df_vendas["Unidades Vendidas"].sum()}")
print (100 * "=")


# # Encontrar o valor médio dos preços por unidade
print (f"\nO valor médio dos preços por unidade é R$ {np.mean(df_vendas["Preço por Unidade (R$)"]):.2f}")
print (100 * "=")


# # O maior faturamento total entre os produtos
maior_faturamento = df_vendas["Faturamento Total (R$)"].max()
produto_maior_faturamento = df_vendas.loc[df_vendas["Faturamento Total (R$)"].idxmax(), "Produto"]

print (f'\nO produto com maior faturamento foi {produto_maior_faturamento} com valor de R$ {maior_faturamento:.2f}')
print (100 * "=")

# # Identificar o menor faturamento total entre os produtos
menor_faturamento = df_vendas["Faturamento Total (R$)"].min()
produto_menor_faturamento = df_vendas.loc[df_vendas["Faturamento Total (R$)"].idxmin(), "Produto"]

print (f'\nO produto com menor faturamento foi {produto_menor_faturamento} com valor de R$ {menor_faturamento:.2f}')
print (100 * "=")

# # Produtos com classificação de nível de satisfação baixo
print ("Produtos com baixo nível de Satisfação \n")
satisfacao = df_vendas[df_vendas["Satisfação"]== "Baixo"]
print (satisfacao[["Produto", "Satisfação"]])
print (100 * "=")