#testing reository
from lib.book_repository import *
from lib.book import* 

def test_retrive_all_books(db_connection):
        db_connection.seed("seeds/book_store.sql")
        repository = BookRepository(db_connection)
        result = repository.all()
        assert result == [
                Book(1,'Nineteen Eighty-Four', 'George Orwell'),
                Book(2,'Mrs Dalloway', 'Virginia Woolf'),
                Book(3,'Emma', 'Jane Austen'),
                Book(4,'Dracula', 'Bram Stoker'),
                Book(5,'The Age of Innocence', 'Edith Wharton')
        ]
                
        





# -- Then, we recreate them
# CREATE SEQUENCE IF NOT EXISTS books_id_seq;
# CREATE TABLE books (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(255),
#     author_name VARCHAR(255)
# );

# -- Finally, we add any records that are needed for the tests to run
# INSERT INTO books (title, author_name) VALUES ('Nineteen Eighty-Four', 'George Orwell');
# INSERT INTO books (title, author_name) VALUES ('Mrs Dalloway', 'Virginia Woolf');
# INSERT INTO books (title, author_name) VALUES ('Emma', 'Jane Austen');
# INSERT INTO books (title, author_name) VALUES ('Dracula', 'Bram Stoker');
# INSERT INTO books (title, author_name) VALUES ('The Age of Innocence', 'Edith Wharton');
