from models.user_model import User


class UserManagement:

    _logged_user = None

    @staticmethod
    def logged_user():
        if UserManagement._logged_user is None:
            UserManagement._logged_user = User()
        return UserManagement._logged_user
