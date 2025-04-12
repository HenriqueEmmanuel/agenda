import sqlite3
import os

DB_PATH = os.path.join("data", "agenda.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data TEXT NOT NULL,
    hora TEXT NOT NULL
)
""")
conn.commit()

def adicionar_evento(nome, data, hora):
    cursor.execute("INSERT INTO eventos (nome, data, hora) VALUES (?, ?, ?)", (nome, data, hora))
    conn.commit()

def buscar_eventos_do_dia(data):
    cursor.execute("SELECT nome, hora FROM eventos WHERE data = ?", (data,))
    return cursor.fetchall()

def fechar_conexao():
    conn.close()
