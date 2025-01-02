from typing import Optional

from database.config import RepositoryConfig
from database.models import User
from helpers.encrypt_helper import EncryptHelper


class UsersRepository(RepositoryConfig):
    def __init__(self):
        super().__init__(table_name="users")

    def create_user(self, user_data: dict) -> None:
        """
        Cria um novo usuário com os dados fornecidos.
        """
        new_user = User(
            id=user_data["id"],
            name=user_data["name"].title(),
            password=EncryptHelper.encrypt_password(user_data["password"])
        )
        self.execute_and_commit(new_user)

    def get_user_by_id(self, user_id: str) -> Optional[dict]:
        """
        Retorna as informações do usuário pelo ID, ou None se não encontrado.
        """
        result = self.search(User, {"id": user_id})
        return {
            "user_id": result[0].id,
            "name": result[0].name,
            "password": result[0].password
        } if result else None

    def update_user(self, user_data: dict) -> None:
        """
        Atualiza as informações de um usuário existente.
        """
        filters = {"id": user_data["id"]}
        self.update(User, filters, user_data)

    def create_user_if_not_exists(self, user_data: dict) -> bool:
        """
        Cria o usuário somente se ele não existir.
        Retorna True se o usuário foi criado, False se já existia.
        """
        if self.get_user_by_id(user_data["id"]):
            return False
        self.create_user(user_data)
        return True

