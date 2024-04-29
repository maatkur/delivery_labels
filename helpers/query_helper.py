import json
import os


class QueryHelper:

    _query_file = fr'{os.getenv("USERPROFILE")}\consulta.json'

    @staticmethod
    def verify_return() -> bool:
        return os.path.exists(QueryHelper._query_file)

    @staticmethod
    def load_data() -> dict:
        with open(QueryHelper._query_file, "r") as file:
            return json.load(file)

    @staticmethod
    def verify_and_load() -> dict or bool:
        if QueryHelper.verify_return():
            if QueryHelper.load_data().get("cliente"):
                return QueryHelper.load_data()
            else:
                return False
        else:
            return False
