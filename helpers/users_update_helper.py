from database.repositories.repository_manager import RepositoryManager
from helpers.file_helper import FileHelper
from helpers.encrypt_helper import EncryptHelper
from components.dialog_window.dialog_window_manager import DialogWindowManager


class UserUpdateHelper:

    @staticmethod
    def update_users() -> None:
        from dbf_repositories.dbf_repository_manager import DbfRepositoryManager

        DialogWindowManager.dialog().start_users_update()

        FileHelper.copy("vendedor.dbf")
        user_source = DbfRepositoryManager.users_dbf_repository().get_users()

        for user in user_source:
            permissions = RepositoryManager.users_permissions_repository().retrieve_user_permissions(user["code"])

            encrypted_password = EncryptHelper.encrypt_password(user["password"])
            user["password"] = encrypted_password
            RepositoryManager.users_repository().insert(user)
            if not permissions:
                RepositoryManager.users_permissions_repository().insert({"code": user["code"]})

        FileHelper.delete()

        DialogWindowManager.dialog().finish_users_update()
