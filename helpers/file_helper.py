from os import system, remove, getenv


class FileHelper:

    @staticmethod
    def copy(file):
        system(fr"copy {getenv('DBF_PATH')}\{file} {getenv('DBF_DESTINY_PATH')}\{file}")
        print(fr"copy {getenv('DBF_PATH')}\{file} {getenv('DBF_DESTINY_PATH')}\{file}")

    @staticmethod
    def delete(file):
        remove(fr".\resources\dbfs\{file}")
