from models.user_model import User


class LoggedUserHelper:

    _logged_user = None

    @staticmethod
    def logged_user():
        if LoggedUserHelper._logged_user is None:
            LoggedUserHelper._logged_user = User()
        return LoggedUserHelper._logged_user
