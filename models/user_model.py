class User:
    _code = None
    _name = None
    _store = None
    _admin = None

    def set_data(self, logged_user: dict) -> None:
        self._code = logged_user["code"]
        self._name = logged_user["name"]
        self._store = logged_user["store"]
        self._admin = logged_user["admin"]

    def clear_data(self):
        self._code = None
        self._name = None
        self._store = None
        self._admin = None

    def get_data(self) -> dict:
        return {
           "code": self._code,
           "name": self._name,
           "store": self._store,
           "admin": self._admin,
        }
