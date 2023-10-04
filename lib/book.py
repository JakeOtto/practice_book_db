#book class
class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

    def __eq__(self,other):
        
        return self.__dict__ == other.__dict__

    def __repr__(self):
        
        return f"Book({self.id},{self.title},{self.author_name})"


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
