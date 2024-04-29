from os import system, path, remove, listdir
from .path_helper import PathHelper


class FileHelper:
    """
    Inicializa a classe FileHelper.

    Define os diretórios de origem dos arquivos e o diretório temporário para cópia.
    """
    source_file_directory = r"C:\users\mathe\desktop"  # Diretório de origem dos arquivos
    tmp_directory = path.abspath(fr'tmp')  # Diretório temporário para cópia dos arquivos

    print(tmp_directory)

    @staticmethod
    def file_exists(file_path: str) -> bool:
        """
        Verifica se um arquivo existe.

        Parâmetros:
        file_path (str): O caminho do arquivo a ser verificado.

        Retorna:
        bool: True se o arquivo existir, False caso contrário.
        """
        return path.exists(file_path)

    @staticmethod
    def copy(file: str) -> None:
        """
        Copia um arquivo da pasta de origem para o diretório temporário.

        Parâmetros:
        file (str): O nome do arquivo a ser copiado.
        """
        file_path = fr"{FileHelper.source_file_directory}\{file}"

        try:
            # Copia o arquivo
            system(fr"copy {file_path} {FileHelper.tmp_directory}\{file}")
            # Verifica se o arquivo foi copiado com sucesso
            if FileHelper.file_exists(fr"{FileHelper.tmp_directory}\{file}"):
                print(f"Arquivo {file} copiado para {FileHelper.tmp_directory}")
            else:
                print(f"Falha ao copiar o arquivo {file} para {FileHelper.tmp_directory}. Arquivo inexistente")
        except FileNotFoundError:
            print(f"Arquivo {file} não encontrado na pasta de origem.")
        except PermissionError:
            print(f"Sem permissão para copiar o arquivo {file} para {FileHelper.tmp_directory}.")

    @staticmethod
    def delete() -> None:
        """
        Exclui todos os arquivos presentes no diretório temporário.
        """
        files_list = [path.join(FileHelper.tmp_directory, file) for file in listdir(FileHelper.tmp_directory)]

        for file in files_list:
            try:
                remove(file)
                # Verifica se o arquivo foi excluído com sucesso
                if not FileHelper.file_exists(file):
                    print(f"Arquivo {file} excluído com sucesso.")
                else:
                    print(f"Falha ao excluir o arquivo {file} da pasta temporária.")
            except FileNotFoundError:
                print(f"Arquivo {file} não encontrado na pasta temporária.")
            except PermissionError:
                print(f"Sem permissão para excluir o arquivo {file} da pasta temporária.")
