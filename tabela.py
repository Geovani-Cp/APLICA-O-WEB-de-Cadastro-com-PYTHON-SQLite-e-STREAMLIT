import sqlite3

conexao = sqlite3.connect("Cliente.db")

cursor = conexao.cursor()

cursor.execute(
   """
       CREATE TABLE Cliente(
         ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         Nome TEXT NOT NULL,
         Telefone TEXT NOT NULL,
         Endereco TEXT NOT NULL
        );
    """
)

cursor.close()
print("Tabela criada com sucesso")
