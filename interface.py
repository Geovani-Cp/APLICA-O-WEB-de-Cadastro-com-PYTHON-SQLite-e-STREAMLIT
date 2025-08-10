import streamlit 
import pandas as pd
import funcoes

st.title("Cadastro de clientes")
nome = st.text_input("Digite seu nome: ")
telefone = st.text_input("Digite seu telefone: ")
endereco = st.time_input("Digete seu endereco: ")

if st.button("Adicionar cliente"):
    funcoes.insereDados(nome, telefone, endereco)
    st.sucess("Cliente Adicionado")

if st.button("Listar Clientes"):
    dados = funcoes.listarDados()
    td = pd.DataFrame(dados, columns=["ID", "Nome", "telefone", "Endereco"])
    st.header("Lista de Clientes")
    st.table(tb)

