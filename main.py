#criação de funções

preco = 1999.90

#calcular 5% de imposto. guadar na variavel imposto e exibir na tela

imposto = preco*0.05
preco = imposto + preco
print(imposto)
print(f"{preco}\n")

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

# Aqui é o uso ... aqui é imposto a calcular..
preco = 299
imposto = calcular_imposto(preco)
print(imposto)


valores = [1.99, 24.50, 78.27, 1515.5] 
# Se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de .... é ..."(1º preço, 2º. imposto)

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")