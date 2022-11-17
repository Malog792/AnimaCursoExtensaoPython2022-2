#1º passo: importar a biblioteca sqlite3
import sqlite3

#2º passo: Vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3º passo: criar um objeto do tipo cursor
cursor = conexao.cursor()

#4º passo: Comando para inserir um herói/vilão 
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo)VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#5º passo: Executar o comando SQL no SQLlite (no cursor)
print(cursor.execute(sql))
