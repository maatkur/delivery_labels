

class User:
    _code = None
    _name = None
    _store = None
    _permissions = None

    def set_data(self, logged_user: dict) -> None:
        self._code = logged_user["code"]
        self._name = logged_user["name"]
        self._store = logged_user["store"]
        self._permissions = logged_user["permissions"]

    def clear_data(self):
        self._code = None
        self._name = None
        self._store = None
        self._permissions = None

    def get(self) -> dict:
        return {
            "code": self._code,
            "name": self._name,
            "store": self._store,
            "permissions": self._permissions
        }
