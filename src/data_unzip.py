import zipfile
import os

def descompactar_arquivo(zip_path):

    destino = os.path.dirname(zip_path)  # Retorna o destino da pasta, sem referenciar o arquivo archive.zip
                                         # Output: C:\Users\andre\Desktop\Projetos\projeto1\data\dataset

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destino)
        print(f"Arquivo descompactado em: {destino}")
    except zipfile.BadZipFile:
        print("Erro: O arquivo ZIP está corrompido ou inválido.")
    except FileNotFoundError:
        print("Erro: Arquivo ZIP não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Caminho do arquivo ZIP
zip_file = r"C:\Users\andre\Desktop\Projetos\projeto1\data\dataset\archive.zip"

# Chamando a função
descompactar_arquivo(zip_file)
        

