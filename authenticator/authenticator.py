import bcrypt
from database.repositories.repository_manager import RepositoryManager


class Authenticator:

    @staticmethod
    def authenticate(user) -> dict or bool:

        credentials = RepositoryManager.users_repository().get_user_credential(user["code"])

        if credentials:
            incoming_password = user["password"].encode('utf-8')  # Converta a senha em bytes
            stored_password = credentials["password"]
            if bcrypt.checkpw(incoming_password, stored_password):
                return credentials
        return False
