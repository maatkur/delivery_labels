from os import path
from dbfread import DBF


class DbfRepository:

    def __init__(self, file) -> None:
        self.file = fr"C:\Users\mathe\PycharmProjects\delivery_labels\tmp\{file}"

        if type(self) is DbfRepository:
            raise NotImplementedError("DbfRepository class cannot be started directly, you must use it as inheritance")

    def _load(self) -> DBF:
        if path.exists(self.file):
            return DBF(fr"{self.file}", encoding="cp437", load=False)
        else:
            raise FileNotFoundError(f'Arquivo "{self.file}" não encontrado!')
