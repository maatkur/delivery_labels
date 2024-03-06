from database.repositories.repository_manager import RepositoryManager
from dbf_repositories.dbf_repository_manager import DbfRepositoryManager
from helpers.file_helper import FileHelper
from helpers.encrypt_helper import EncryptHelper


class UserUpdateHelper:

    @staticmethod
    def update_users() -> None:
        FileHelper.copy_users_file()
        user_source = DbfRepositoryManager.users_dbf_repository().get_users()

        for user in user_source:
            encrypted_password = EncryptHelper.encrypt_password(user["password"])
            user["password"] = encrypted_password
            RepositoryManager.users_repository().insert(user)
            RepositoryManager.users_permissions_repository().insert({"code": user["code"]})

        FileHelper.delete_users_file()
