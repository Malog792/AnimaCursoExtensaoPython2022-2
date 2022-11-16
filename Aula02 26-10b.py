# Pede o nome do aluno e a sua nota ( de 0 a 10) e, se ele tirou nota 10, mostra "Você é brabo"

nome = input("Insira o seu Nome: \n")
nota = float(input("Digite a sua nota: \n"))

if nota == 10:
  print ("Você é brabo")
elif (nota >=6 and nota < 10):
  print (f"{nome}, bom trabalho, tava ruim mas podia ser pior")
else:
  print ("Tente um pouco mais na proxima {}".format(nome))
  
