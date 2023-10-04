#Book repository class
from lib.book import*

class BookRepository:

    def __init__(self,connection):
        self._connection = connection
        



    def all(self):
        result = self._connection.execute("SELECT * FROM books")
        books_list = []
        for field in result:
            book = Book (field["id"],field ["title"],field ["author_name"])
            books_list.append(book)
        return books_list




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
