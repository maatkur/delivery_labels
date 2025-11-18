class SessionHelper:
    _instance = None
    _session_data = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SessionHelper, cls).__new__(cls)
        return cls._instance

    def set(self, key: str, value):
        """Armazena dados na sessão."""
        self._session_data[key] = value

    def get(self, key: str):
        """Recupera dados da sessão."""
        return self._session_data.get(key)

    def remove(self, key: str):
        """Remove uma chave específica da sessão."""
        self._session_data.pop(key, None)

    def clear(self):
        """Limpa todos os dados da sessão."""
        self._session_data.clear()

    def set_current_user(self, user_entity):
        """Define o usuário atual na sessão."""
        self.set("user", user_entity)

    def get_current_user(self):
        """Retorna o usuário atual (UserEntity) ou None."""
        return self.get("user")

    def is_logged_in(self) -> bool:
        """Retorna True se há um usuário logado."""
        return self.get("user") is not None
