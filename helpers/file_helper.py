from os import system, remove, getenv


class FileHelper:
    users_file = "vendedor.dbf"
    orders_file = "pedidos.dbf"

    @staticmethod
    def copy_users_file():
        system(
            fr"copy {getenv('DBF_PATH')}\{FileHelper.users_file} {getenv('DBF_DESTINY_PATH')}\{FileHelper.users_file}")

    @staticmethod
    def delete_users_file():
        remove(fr".\resources\dbfs\{FileHelper.users_file}")

    @staticmethod
    def copy_orders_file():
        print(fr"{getenv('DBF_PATH')}\{FileHelper.orders_file} {getenv('DBF_DESTINY_PATH')}\{FileHelper.orders_file}")
        system(
            fr"copy {getenv('DBF_PATH')}\{FileHelper.orders_file} {getenv('DBF_DESTINY_PATH')}\{FileHelper.orders_file}")

    @staticmethod
    def delete_orders_file():
        remove(fr".\resources\dbfs\{FileHelper.orders_file}")
