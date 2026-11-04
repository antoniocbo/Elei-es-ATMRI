import sqlite3
from flask import Flask

app = Flask(__name__)

def salvar_voto(candidato):

    conn = sqlite3.connect("votos.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO votos (candidato) VALUES (?)",
        (candidato,)
    )

    conn.commit()
    conn.close()

import sqlite3

conn = sqlite3.connect("votos.db")
cursor = conn.cursor()

cursor.execute("""
SELECT candidato, COUNT(*)
FROM votos
GROUP BY candidato
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()

@app.route("/")
def inicio():
    return """
    <h1>Eleições da ATMRI</h1>
    <a href='/admin'>Ver resultados</a>
    """

@app.route("/admin")
def admin():

    conn = sqlite3.connect("votos.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT candidato, COUNT(*)
    FROM votos
    GROUP BY candidato
    """)

    resultados = cursor.fetchall()

    conn.close()

    return str(resultados)

if __name__ == "__main__":
    app.run(debug=True)
