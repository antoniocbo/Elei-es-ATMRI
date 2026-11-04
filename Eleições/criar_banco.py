import sqlite3

# Cria ou abre o banco
conn = sqlite3.connect("votos.db")

cursor = conn.cursor()

# Cria a tabela de votos
cursor.execute("""
CREATE TABLE IF NOT EXISTS votos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidato TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")