from typing import Optional, Tuple
import bcrypt

from database.repositories.repository_manager import RepositoryManager
from domain.entities import UserEntity


class Authenticator:

    @staticmethod
    def authenticate(user_id: str, password: str) -> Tuple[dict, Optional[UserEntity]]:
        """
        Autentica um usuário com base no ID e senha fornecidos.

        :param user_id: ID do usuário.
        :param password: Senha em texto puro.
        :return: Tupla (status_dict, UserEntity | None)
        """
        # Obtem o repositório de usuários
        user_repo = RepositoryManager.users_repository()
        user_entity = user_repo.get_user_by_id(user_id)

        if not user_entity:
            return {"status": "error", "message": "Usuário não encontrado"}, None

        # Verifica a senha com bcrypt
        if not bcrypt.checkpw(password.encode('utf-8'), user_entity.password.encode('utf-8')):
            return {"status": "error", "message": "Senha incorreta"}, None

        # Busca permissões do usuário
        permissions_repo = RepositoryManager.users_permissions_repository()
        permissions = permissions_repo.get_user_permissions(user_id)

        # Atualiza a entidade com as permissões do domínio
        user_entity.permissions = permissions

        return {"status": "success"}, user_entity
