import sqlite3

def conectaBD():
    conexao = sqlite3.connect("Cliente.db")
    return conexao

def insereDados(nome, telefone, endereco):
    conexao = conectaBD
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO CLIENTE(nome, telefone, endereço)Value (?, ?, ?, ?)",(nome, telefone, endereco))
    conexao.commit()
    conexao.close()

def listarDados():
    conexao = conectaBD
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cliente")
    dados = cursor.fetchal()
    cursor.close()
    return dados 


    
