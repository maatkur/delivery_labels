from os import path
from dbfread import DBF


class DbfRepository:

    def __init__(self, file) -> None:
        self.file = fr"./resources/dbfs/{file}"

        if type(self) == DbfRepository:
            raise NotImplementedError("DbfRepository class cannot be started directly, you must use it as inheritance")

    def _load(self) -> DBF:
        if path.exists(self.file):
            return DBF(fr"{self.file}", encoding="cp437", load=True)
        else:
            raise FileNotFoundError(f'Arquivo "{self.file}" não encontrado!')
