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

## Instalação e Execução

1. Clone o repositório (se estiver num Git):
   ```bash
   git clone https://github.com/maatkur/delivery_labels.git
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
   # Isso cria o arquivo delivery_labels.db com as tabelas e o usuário admin padrão
   # user admin -> ID: 999 Senha padrão: 123456.
   # Recomendo alterar a senha do usuário admin após o primeiro login.

5. Executar o arquivo:
   
    ```bash
    delivery_labels.py na pasta principal raiz do projeto
   
## Deploy
Para distribuir o aplicativo:

1. Configure o path do db nos arquivos `alembic.ini` e `./database/config`:
   ```python
   # database.py
   DATABASE_URL = "sqlite:///caminho_do_db/delivery_labels.db"
   
   # alembic.ini
   sqlalchemy.url = sqlite:///caminho_do_db/delivery_labels.db

2. Atualize o banco de dados com o Alembic:
   ```bash
   alembic upgrade head

3. Criar um executável com o PyInstaller via invoke:
   ```bash
    invoke deploy
   # O executável será gerado em ./dist/delivery_labels/ e a pasta dist/ será aberta automaticamente.
   
   
## Funcionalidades

**Tela de Login**
  - Verifica usuário e senha (hasheada com bcrypt) no banco.
  - Admin (ID: 999) tem acesso total; outros usuários têm acesso limitado.

**Tela Principal**

  - Busca de Pedidos: Campo (order_entry) e botão (search_button) ou Enter pra consultar e preencher dados (cliente, loja, data).
  - Impressão: Ajusta volumes (1-36) com botões (increment_button, decrement_button), imprime etiquetas com print_button e salva logs no SQLite.
  - Reimpressão: Quadro (reprint_frame) com motivos pra reimprimir, só com permissão "REPRINT LABELS".
  - Acesso: Menu (drawer) com botões pra gerenciar usuários (users_menu_button, permissão "MANAGE USERS"), relatórios (reports_button, permissão "REPORT") e trocar senha (change_password_button).
  - Interface: Campos/botões dinâmicos e usuário logado exibido como "ID-Nome".
  - Admin: ID 999 ("admin") com todas as permissões.

**Tela de Gerenciamento de Usuários**
 - Listagem: Tabela (QTableWidget) com Código, Nome e checkboxes pra permissões (Reimpressão, Relatórios, Usuários), atualizadas em tempo real.
 - Filtro: Campo (user_code_entry) e botão (search_button) ou Enter pra filtrar por ID; clear_button recarrega tudo.
 - Adição: Botão (add_user_button) abre formulário (ID, Nome, Senha), cria usuários com validação e feedback por diálogos.
 - Restrição: Não-admin (ID ≠ 999) vê janela limitada (402x389), admin vê tudo.
 - Interface: Navegação com Enter e ajustes dinâmicos nos campos/botões.
