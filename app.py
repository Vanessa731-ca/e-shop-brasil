import streamlit as st
from pymongo import MongoClient
import os


# String de conexão
conn_str = "mongodb://mongo:27017/"


# Criando cliente do MongoDB
client = MongoClient(conn_str)
db = client["eshop_banco"]

st.title("E-Shop Brasil - Cadastro de Clientes")

# Formulário simples para cadastro
with st.form("cliente_form"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    enviar = st.form_submit_button("Cadastrar")

    if enviar:
        if nome and email:
            cliente = {"nome": nome, "email": email}
            db.clientes.insert_one(cliente)
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Preencha todos os campos!")
