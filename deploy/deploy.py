# deploy.py

import PyInstaller.__main__


def main():
    # Caminho para o arquivo de configuração
    config_file = "delivery_labels.spec"

    # Executa o PyInstaller com base no arquivo de configuração
    PyInstaller.__main__.run([
        config_file,
        "-y"
    ])


if __name__ == "__main__":
    main()
