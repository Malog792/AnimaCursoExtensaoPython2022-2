# comando input(): quero permitir que o usuario digite algo

nome = input("Digite seu nome: \n")

idade = int(input("Digite a sua idade: \n"))
genero = input("Digite M para genero masculino e F para feminino: \n")
dobro= idade*2
# exiba a sua idade é ..
#idade = idade+40
print ("Seu nome é: "+nome)
print ("Seu Gênero é: "+genero)
print(f"A sua idade é:{idade} ")
print(f"O dobro da sua idade é: {dobro}")

# comando de saída..exibir na tela

#Estrutura condicional - o if
# Se a pessoa for maior de idade, mostre 
#"Você é maior de idade, ótimo"

if idade >= 18 and genero == "M" or "m":
  print ("Você é maior de idade, ótimo, pode beber ou dirigir \n")
 
  print("Você precisa/precisou prestar serviço militar obrigatório")

  
else:
  print("Fique em casa, você deveria estar estudando")
  
# E se eu quisesse perguntar o gênero (M = masculino e o F = feminino)
# Mostre (.. e você também precisa/precisou prestar o serviço militar obrigatório)


