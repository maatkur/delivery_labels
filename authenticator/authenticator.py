from typing import Optional

import bcrypt
from database.repositories.repository_manager import RepositoryManager


class Authenticator:

    @staticmethod
    def authenticate(user: dict) -> Optional[dict]:
        """
        Autentica um usuário com base no ID e na senha fornecida.

        :param user: Um dicionário com as chaves "user_id" e "password".
        :return: Um dicionário contendo credenciais e permissões se autenticado, senão levanta ValueError.
        """
        # Obtenha as credenciais do repositório
        credentials = RepositoryManager.users_repository().get_user_credential(user["user_id"])

        if not credentials:
            return {"status": "error", "credentials": None}

        # Verifique a senha
        incoming_password = user["password"].encode('utf-8')
        stored_password = credentials["password"].encode('utf-8')

        if not bcrypt.checkpw(incoming_password, stored_password):
            return {"status": "error", "credentials": None}
        else:
            # Obtenha as permissões do usuário
            permissions = RepositoryManager.users_permissions_repository().get_user_permissions(user["user_id"])
            credentials.pop("password", None)
            credentials["permissions"] = permissions
            return {"status": "success", "credentials": credentials}
