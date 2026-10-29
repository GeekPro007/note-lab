from notes import connect, add_note, list_notes

db = connect()
add_note(db, 'Learn about virtual environments')
print(list_notes(db))
