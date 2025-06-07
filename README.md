
# E-Shop Brasil - Projeto de Big Data e Banco de Dados

# Contexto
A E-Shop Brasil é uma das maiores plataformas de comércio eletrônico do país, com mais de 5 milhões de clientes ativos e cerca de 100 mil pedidos processados por dia. Com esse volume, os desafios em relação à gestão de dados, personalização da experiência do cliente e otimização logística se tornam cada vez maiores.

Este projeto foi desenvolvido como aplicação prática para demonstrar como tecnologias como MongoDB, Streamlit, Docker e Big Data podem ajudar a resolver esses desafios.

# Objetivos do Projeto

- Garantir segurança e privacidade dos dados dos clientes, conforme a LGPD.
- Personalizar a navegação e recomendações usando dados de comportamento de usuários.
- Melhorar a eficiência logística e controle de estoques, especialmente em regiões remotas.
- Oferecer uma infraestrutura escalável, com tecnologias sustentáveis a longo prazo.

#Tecnologias Utilizadas

- `MongoDB` - Banco de dados NoSQL usado para armazenar dados estruturados e semi-estruturados.
- `Streamlit` - Framework para visualização e interação com os dados via interface web.
- `Docker` e `Docker Compose` - Para isolamento e padronização do ambiente de desenvolvimento.
- `Python` - Linguagem usada na construção da aplicação.
- `Faker` e/ou dados fictícios - Para simulação de cenários reais.

# Funcionalidades da Aplicação

A aplicação em `Streamlit` se conecta ao `MongoDB` e permite:

- Inserção de dados simulados no banco de dados.
- Manipulação de dados (edição e exclusão).
- Consulta e exibição dos dados cadastrados.
- Visualização por meio de interface gráfica amigável.
- Concatenação de dados de diferentes coleções.

# Como Rodar o Projeto

# Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

# Passo a Passo

1. Clone o repositório:

```bash
git clone https://github.com/Vanessa731-ca/e-shop-brasil.git
cd e-shop-brasil
```

2. Suba a infraestrutura:

```bash
docker-compose up --build
```

> Caso esteja utilizando `Dockerfile` individual:
```bash
docker build -t eshop-app .
docker run -p 8501:8501 eshop-app
```

3. Acesse a aplicação:

Abra seu navegador e vá até: `http://localhost:8501`

# Estrutura do Projeto

```
eshop-bigdata-project/
├── README.md
├── app.py
├── docker-compose.yml  (ou Dockerfile)
├── exemplos/
│   └── gifs-ou-prints-do-app.png
└── dados/
    └── dados_ficticios.json (ou .csv)
```

# Considerações Finais

Este projeto representa uma solução escalável e prática para empresas do setor de e-commerce que enfrentam os desafios do crescimento e da complexidade dos dados. Foi estruturado com foco em modularidade, reprodutibilidade e aplicação prática de conceitos aprendidos em aula.

---

Desenvolvido por: Vanessa  Ferreira- 3º semestre de T.I.
