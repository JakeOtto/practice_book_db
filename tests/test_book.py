#testing book
from lib.book import*

def test_book_added_successfully():
    
    new_book = Book(1,"Nineteen Eighty-Four",'George Orwell')
    assert new_book.id == 1
    assert new_book.title == "Nineteen Eighty-Four"
    assert new_book.author_name == "George Orwell"






#assert book 1 - assert id , title and author

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
# INSERT INTO books (title, author_name) VALUES ('The Age of Innocence', 'Edith Wharton'#