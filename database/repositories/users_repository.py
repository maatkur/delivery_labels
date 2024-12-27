from typing import Optional

from database.config import RepositoryConfig
from database.models import User  # Importe o modelo User
from helpers.encrypt_helper import EncryptHelper


class UsersRepository(RepositoryConfig):

    def __init__(self):
        super().__init__(table_name="users")

    def create_user(self, user_data: dict) -> None:
        # Cria uma instância do modelo User com os parâmetros
        new_user = User(
                        id=user_data["id"],
                        name=user_data["name"],
                        password=EncryptHelper.encrypt_password(user_data["password"])
        )

        # Agora adiciona essa instância ao banco
        self.execute_and_commit(new_user)

    def get_user_credential(self, user_code: str) -> Optional[dict]:
        """
        Obtém as credenciais do usuário com base no ID.
        """
        # Usando ORM para fazer a consulta
        result = self.search(User, {"id": user_code})

        if result:
            user = result[0]
            return {
                "user_id": user.id,
                "name": user.name,
                "password": user.password
            }
        return None

    def update_user(self, user_data: dict) -> None:
        """
        Atualiza as informações de um usuário.
        """
        # Usando o método update do RepositoryConfig
        filters = {"id": user_data["id"]}
        self.update(User, filters, user_data)