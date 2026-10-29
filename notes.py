import sqlite3

def connect(path='notes.db'):
    db = sqlite3.connect(path)
    db.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)')
    return db

def add_note(db, text):
    db.execute('INSERT INTO notes (text) VALUES (?)', (text,))
    db.commit()

def list_notes(db):
    return [row[0] for row in db.execute('SELECT text FROM notes')]
