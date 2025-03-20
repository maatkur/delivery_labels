# deploy/deploy.py
import PyInstaller.__main__
import os

def main():
    # Caminho absoluto pro .spec a partir da raiz
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Raiz do projeto
    config_file = os.path.join(base_path, 'deploy', 'delivery_labels.spec')

    PyInstaller.__main__.run([
        config_file,
        "-y"
    ])

if __name__ == "__main__":
    main()