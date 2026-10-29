from notes import connect, add_note, list_notes

def test_add_and_list():
    db = connect(':memory:')
    add_note(db, 'hello')
    assert list_notes(db) == ['hello']

