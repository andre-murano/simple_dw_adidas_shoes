import psycopg2

def criar_conexao():

    # Parâmetros 
    server_name = "projeto1"
    host = "localhost"
    port = "5432"
    maintenance_db = "postgres"
    username = "projeto1"
    password = "projeto1"

    try:
        
        print("Tentando conectar ao banco de dados...")

        # Conexão com o banco de dados PostgreSQL
        conn = psycopg2.connect(
            dbname=maintenance_db,
            user=username,
            password=password,
            host=host,
            port=port
        )

        # Executar as consultas
        cursor = conn.cursor()

        print("Conexão com o banco de dados estabelecida com sucesso!")

        return conn, cursor

    except Exception as e:
        # Imprime o erro detalhado
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None

# Teste da conexão
conn, cursor = criar_conexao()

# Verificação de sucesso
if conn is None or cursor is None:
    print("Falha na conexão com o banco de dados.")
else:
    print("Conexão bem-sucedida.")


