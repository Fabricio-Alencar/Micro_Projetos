# /home/database/connection.py
import sqlite3
from pathlib import Path

# Caminho do banco — relativo ao diretório atual (/home)
DB_PATH = Path(__file__).resolve().parent.parent / "meusistema.db"
# ↑ sobe um nível (de /home/database → /home) e cria meusistema.db lá

# Garante que o diretório existe
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
