import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Sessão para controle de login
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# Credenciais do arquivo secrets.toml
usuario_correto = st.secrets["admin"]["username"]
senha_correta = st.secrets["admin"]["password"]

# Se ainda não está logado, mostra tela de login
if not st.session_state["logado"]:
    st.title("🔒 Área Administrativa - Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == usuario_correto and senha == senha_correta:
            st.session_state["logado"] = True
            st.success("✅ Login bem-sucedido!")
            st.rerun()
        else:
            st.error("❌ Usuário ou senha incorretos, tenta de novo com carinho 🥹")

# Se logado, mostra o sistema
else:
    st.sidebar.title("👩‍💼 Menu Administrativo")

    if st.sidebar.button("🔓 Sair"):
        st.session_state["logado"] = False
        st.rerun()

    # Menu lateral
    menu = st.sidebar.radio("Navegação", ["📋 Cadastrar", "📄 Visualizar Clientes", "📊 Dashboard"])

    # Conectar ao MongoDB
    conn_str = st.secrets["database"]["uri"]
    client = MongoClient(conn_str)
    db = client["eshop_banco"]
    colecao = db.clientes

    # --- Cadastrar cliente ---
    if menu == "📋 Cadastrar":
        st.title("📋 Cadastro de Clientes")
        with st.form("form_cliente"):
            nome = st.text_input("Nome")
            email = st.text_input("Email")
            enviar = st.form_submit_button("Cadastrar")

            if enviar:
                if nome and email:
                    cliente = {"nome": nome, "email": email}
                    colecao.insert_one(cliente)
                    st.success("🎉 Cliente cadastrado com sucesso!")
                else:
                    st.warning("⚠️ Preencha todos os campos.")

    # --- Visualizar clientes ---
    elif menu == "📄 Visualizar Clientes":
        st.title("📄 Lista de Clientes Cadastrados")
        dados = list(colecao.find({}, {"_id": 0}))

        if dados:
            df = pd.DataFrame(dados)
            st.dataframe(df)

            st.subheader("🔴 Excluir um Cliente")
            email_excluir = st.selectbox("Selecione o e-mail do cliente a excluir:", df["email"].unique())
            if st.button("Excluir Cliente"):
                colecao.delete_one({"email": email_excluir})
                st.success(f"Cliente com e-mail '{email_excluir}' foi excluído com sucesso! ✨")
                st.rerun()
        else:
            st.info("Nenhum cliente cadastrado ainda.")

    # --- Dashboard ---
    elif menu == "📊 Dashboard":
        st.title("📊 Dashboard de Clientes")
        dados = list(colecao.find({}, {"_id": 0}))
        if dados:
            df = pd.DataFrame(dados)
            df["dominio"] = df["email"].apply(lambda x: x.split("@")[-1])
            dominios = df["dominio"].value_counts()
            st.subheader("Clientes por domínio de e-mail:")
            st.bar_chart(dominios)
        else:
            st.info("Ainda não há dados suficientes para o gráfico.")
