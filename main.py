# comando input(): quero permitir que o usuario digite algo

nome = input("Digite seu nome: ")

idade = int(input("Digite a sua idade: "))
dobro= idade*2
# exiba a sua idade é ..
#idade = idade+40
print ("Seu nome é: "+nome)
print(f"A sua idade é:{idade} ")
print(f"O dobro da sua idade é: {dobro}")

# comando de saída..exibir na tela

#Estrutura condicional - o if
# Se a pessoa for maior de idade, mostre 
#"Você é maior de idade, ótimo"

if idade >= 18:
  print ("Você é maior de idade, ótimo, pode beber ou dirigir")
else:
  print("Fique em casa, você deveria estar estudando")
