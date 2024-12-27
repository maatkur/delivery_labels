import json
import os
from typing import Union


class QueryHelper:
    _exe_path = r"f:\esmcun\etiqmat.exe"

    @staticmethod
    def _get_query_file_path() -> str:
        """Retorna o caminho do arquivo de consulta."""
        return os.path.join(os.getenv("USERPROFILE"), "etiq.json")

    @staticmethod
    def file_exists() -> bool:
        """Verifica se o arquivo de consulta existe."""
        return os.path.exists(QueryHelper._get_query_file_path())

    @staticmethod
    def delete_file() -> None:
        """Deleta o arquivo de consulta, se existir."""
        if QueryHelper.file_exists():
            os.remove(QueryHelper._get_query_file_path())

    @staticmethod
    def load_query_json() -> Union[dict, None]:
        """
        Carrega o conteúdo do arquivo JSON de consulta.
        Retorna None caso o arquivo não exista ou esteja corrompido.
        """
        try:
            with open(QueryHelper._get_query_file_path(), "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    @staticmethod
    def is_valid_response(query_data: dict) -> bool:
        """
        Verifica se a resposta é válida com base no conteúdo do JSON.
        Retorna True se o valor de 'nome' for diferente de 'NAO LOCALIZADO' e não contiver 'CONSUMIDOR'.
        """
        nome = query_data.get("nome", "").upper()  # Garantir que o valor de nome seja sempre uma string
        return nome != "NAO LOCALIZADO" and "CONSUMIDOR" not in nome

    @staticmethod
    def manage_response() -> Union[dict, bool]:
        """
        Gerencia a resposta retornada pelo arquivo JSON.
        Retorna o dicionário completo se a resposta for válida,
        ou False caso contrário.
        """
        query_data = QueryHelper.load_query_json()
        if query_data and QueryHelper.is_valid_response(query_data):
            return query_data
        return False

    @staticmethod
    def query_request(query: str) -> None:
        """
        Faz uma requisição executando o comando externo,
        limpando o arquivo anterior antes de enviar.
        """
        QueryHelper.delete_file()
        try:
            result = os.system(f'"{QueryHelper._exe_path}" {query}')
            if result != 0:
                raise RuntimeError(f"Erro ao executar o comando: {query}")
        except Exception as e:
            print(f"Erro ao executar a query: {e}")

    @staticmethod
    def query_response(query: str) -> Union[dict, bool]:
        """
        Envia uma requisição e gerencia a resposta.
        Retorna o dicionário completo se a resposta for válida,
        ou False caso contrário.
        """
        QueryHelper.query_request(query)
        return QueryHelper.manage_response()

