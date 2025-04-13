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

def buscar_todos_eventos_do_dia(data):
    cursor.execute("SELECT nome, hora FROM eventos WHERE data = ?", (data,))
    return cursor.fetchall()

def editar_evento(nome_antigo, data, novo_nome, nova_data, nova_hora):
    cursor.execute("""
        UPDATE eventos
        SET nome = ?, data = ?, hora = ?
        WHERE nome = ? AND data = ?
    """, (novo_nome, nova_data, nova_hora, nome_antigo, data))
    conn.commit()

def ver_todos():
    cursor.execute("SELECT * FROM eventos")
    resultados = cursor.fetchall()
    return resultados

