# 🧪 Automação de Testes Web

Projeto de automação de testes web desenvolvido com **Python, Selenium e Pytest**, utilizando o padrão **Page Object Model (POM)**.

O projeto realiza testes automatizados em uma aplicação web de demonstração, validando diferentes cenários de login, logout e utilização do carrinho de compras.

## 🚀 Tecnologias utilizadas

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git
- GitHub

## 📋 Cenários automatizados

Atualmente o projeto possui 5 testes:

- ✅ Login com usuário e senha válidos
- ✅ Login com senha incorreta
- ✅ Login com usuário inválido
- ✅ Logout
- ✅ Adição de produto ao carrinho

## 📂 Estrutura do projeto

```text
Projeto-02-Automacao-Testes/
│
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_login.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd Projeto-02-Automacao-Testes
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## ▶️ Executando os testes

Para executar todos os testes:

```bash
python -m pytest
```

Para executar com informações detalhadas:

```bash
python -m pytest -v
```

## 🧪 Resultado esperado

Todos os testes devem ser executados com sucesso:

```text
5 passed
```

## 🎯 Objetivo

Este projeto foi desenvolvido com o objetivo de praticar e demonstrar conhecimentos em:

- Automação de testes
- Testes funcionais
- Selenium WebDriver
- Pytest
- Page Object Model
- Fixtures
- WebDriverWait
- Localização de elementos
- Validação de resultados
- Organização de projetos de QA

## 🔮 Próximas melhorias

- Adicionar mais cenários de teste
- Automatizar o fluxo de checkout
- Gerar relatórios de execução
- Implementar integração com n8n
- Executar os testes automaticamente através de um pipeline
- Integrar o projeto a uma API de testes
