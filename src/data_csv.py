import os
import pandas as pd

def carregar_csvs(caminho_diretorio):    # Carrega todos os arquivos .csv no diretório especificado e retorna como DataFrames.

    arquivos = os.listdir(caminho_diretorio)
    csv_files = [f for f in arquivos if f.endswith('.csv')]  # Filtra os arquivos CSV

    
    dataframes = []
    for csv_file in csv_files:
        caminho_csv = os.path.join(caminho_diretorio, csv_file)  # Caminho completo do CSV - Plataforma independente (windows/mac/linux)
        df = pd.read_csv(caminho_csv)  # Carrega o CSV como DataFrame
        dataframes.append(df)  # Adiciona o DataFrame à lista

    return dataframes

diretorio_csv = r"C:\Users\andre\Desktop\Projetos\projeto1\data\dataset"

dataframes = carregar_csvs(diretorio_csv)


#Teste

if dataframes:
    print(dataframes[0].head())


