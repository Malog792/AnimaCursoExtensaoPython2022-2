print("Início da aula 3")
contador = 1

# Exibir de 1 a 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1


#Laço for (python for= for each)
fruta = "Morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#Lista
frutas = ["morango","laranja","pêra"]

#mostra todas
print(frutas)

#quero exibir apenas a 3ªfruta(pêra)
print(frutas[2])

#Quantas frutas tem na minha lista?
print(len(frutas)) # length = tamanho

#Quero incluir uma fruta nova
frutas.append("manga")
frutas.append("Banana")

print(len(frutas))
print(frutas)

i=0
while(i<len(frutas)):
  print(frutas[i])
  i= i + 1

print("Exemplo das frutas com FOR:\n")

for fruta in frutas:#Aqui não pode ter parênteses
  print(fruta)