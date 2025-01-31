import psycopg2
from db_connector import criar_conexao
from data_csv import carregar_csvs  # Importe a função de carregar CSVs

def carregar_dados_para_postgres(dataframes):
    # Estabelece a conexão com o banco
    conn, cursor = criar_conexao()

    if conn is None or cursor is None:
        print("Falha na conexão com o banco de dados.")
        return

    # Dicionário de tabelas e suas colunas (com o schema 'staging_area' adicionado)
    tabelas = {
        "staging_area.st_country": ["country_id", "currency", "shoe_metric"],
        "staging_area.st_shoes_dim": ["shoes_id", "name", "best_for_wear", "gender", "image_url", "dominant_color", "sub_color1", "sub_color2"],
        "staging_area.st_shoes_fact": ["serial_id", "shoes_id", "price", "category", "size", "stock", "date", "country_id"]
    }

    # Processar os DataFrames para cada tabela
    for tabela, colunas in tabelas.items():
        try:
            # Encontra o DataFrame correspondente à tabela
            if tabela == "staging_area.st_country":
                df = dataframes[0]  # O primeiro DataFrame será associado à tabela st_country
            elif tabela == "staging_area.st_shoes_dim":
                df = dataframes[1]  # O segundo DataFrame será associado à tabela st_shoes_dim
            elif tabela == "staging_area.st_shoes_fact":
                df = dataframes[2]  # O terceiro DataFrame será associado à tabela st_shoes_fact
            
            # Ignorar o cabeçalho (caso o DataFrame ainda tenha o cabeçalho)
            df.columns = colunas

            # Insere os dados na tabela do PostgreSQL
            for index, row in df.iterrows():
                query = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['%s'] * len(colunas))})"
                cursor.execute(query, tuple(row))
            
            # Commit das transações
            conn.commit()
            print(f"Dados carregados com sucesso na tabela {tabela}.")

        except Exception as e:
            print(f"Erro ao carregar dados na tabela {tabela}: {e}")
            conn.rollback()  # Rollback em caso de erro

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()
    print("Conexão com o banco de dados fechada.")

# Carrega os arquivos CSV como DataFrames
diretorio_csv = r"C:\Users\andre\Desktop\Projetos\projeto1\data\dataset"
dataframes = carregar_csvs(diretorio_csv)

# Chama a função de carregamento
carregar_dados_para_postgres(dataframes)


