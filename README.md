# Delivery Labels

Este projeto em Python com PySide6 serve para gerenciar usuários e permissões em um sistema de etiquetas. A interface usa uma `QTableWidget` para listar usuários e suas permissões, com acesso restrito para não-administradores.

## Objetivo

Gerenciar usuários e permissões para um sistema de etiquetas, oferecendo uma interface gráfica simples e funcional com PySide6.

## Pré-requisitos

- **Python**: 3.8 ou superior
- **Dependências**: Listadas no `requirements.txt`:
  - PySide6
  - SQLAlchemy
  - Alembic
  - bcrypt
- **SQLite**: Banco de dados leve (usado via `delivery_labels.db`, gerado automaticamente).

## Instalação

1. Clone o repositório (se estiver num Git):
   ```bash
   git clone <url-do-repositorio>
   cd delivery_labels

2. Criar um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux
   .\venv\Scripts\Activate # Windows

3. Instalar as dependências:
   ```bash
    pip install -r "requirements.txt"

4. Configurar o banco de dados:
   ```bash
   alembic upgrade head
   # Isso cria o arquivo delivery_labels.db com as tabelas e o usuário admin padrão.

5. Executar o arquivo principal:
   
    ```bash
    delivery_labels.py na pasta principal do projeto
   
## Funcionalidades

**Restrição de acesso**: 
 - Usuários não-admin (ID ≠ 999) veem apenas as 3 primeiras colunas (Código, Nome, Reimpressão). O admin vê todas.
 - Usuário padrão: ID: 999 Nome: "admin" Senha:(123456) Hasheada com bcrypt (criada na migration inicial).