import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS actiuni (id INTEGER PRIMARY KEY, simbol TEXT, cantitate INTEGER)')
    conn.commit()
    conn.close()
    
def add_actiune(simbol, cantitate):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO actiuni(simbol, cantitate) VALUES(?, ?)',(simbol,cantitate))
    conn.commit()
    conn.close()

def get_actiuni():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM actiuni')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_actiune(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM actiuni WHERE id = ?', (id,))
    conn.commit()
    conn.close()