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
        if key in self._session_data:
            del self._session_data[key]

    def clear(self):
        """Limpa todos os dados da sessão."""
        self._session_data.clear()
