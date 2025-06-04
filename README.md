
# E-Shop Brasil: Aplicação de Big Data e Banco de Dados em E-commerce

Este é um projeto acadêmico desenvolvido como parte do curso de Tecnologia da Informação na UNIFecaf. O estudo de caso propõe a criação de uma aplicação completa para gerenciar dados de clientes em uma empresa fictícia de comércio eletrônico chamada **E-Shop Brasil**, utilizando tecnologias modernas de banco de dados e big data.

## 👨‍💻 Tecnologias Utilizadas

- `MongoDB` (banco de dados NoSQL)
- `Docker` (containerização do ambiente)
- `Streamlit` (aplicação web com interface interativa)
- `Python` (lógica de programação)
- `Pymongo` (conexão entre Python e MongoDB)

## ⚙️ Funcionalidades da Aplicação

- Cadastro de clientes
- Busca de clientes por nome ou e-mail
- Exclusão de clientes
- Dashboard com gráficos de dados
- Login de administrador 
- Interface amigável via Streamlit
- Publicação da aplicação na web

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Docker instalado na máquina
- Git instalado

### Passo a passo

1. Clone este repositório:

```bash
git clone https://github.com/Vanessa731-ca/e-shop-brasil
```

2. Navegue até a pasta do projeto:

```bash
cd e-shop-brasil
```

3. Suba o container com Docker Compose:

```bash
docker-compose up --build
```

4. Acesse o app no navegador:

Depois que o Docker subir tudo, acesse no navegador o endereço:

```
http://localhost:8501
```

## 📁 Estrutura do Projeto

```plaintext
📂 e-shop-brasil
├── app.py               # Código principal da aplicação Streamlit
├── Dockerfile           # Imagem Docker da aplicação
├── docker-compose.yml   # Orquestração dos containers
├── requirements.txt     # Dependências da aplicação
├── .env                 # Variáveis de ambiente
└── README.md            # Este arquivo
```

## 📝 Objetivo do Projeto

O projeto foi desenvolvido com o objetivo de aplicar os conhecimentos de Banco de Dados, Big Data e Desenvolvimento Web adquiridos no curso de **Tecnologia da Informação da UNIFecaf**.

Ele simula uma solução real para uma empresa de e-commerce fictícia, mostrando como é possível integrar tecnologias modernas para gestão de dados, segurança, personalização da experiência do cliente e otimização logística.

## 👩‍🏫 Informações Acadêmicas

- Aluna: **Vanessa de Souza Ferreira**  
- Faculdade: **UNIFecaf**  
- Tutor: **Vitor Jansen**

## 🌐 Link do Repositório

🔗 [https://github.com/Vanessa731-ca/e-shop-brasil](https://github.com/Vanessa731-ca/e-shop-brasil)
