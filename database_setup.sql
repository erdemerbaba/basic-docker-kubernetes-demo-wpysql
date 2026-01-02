-- Drop the table if it exists to ensure a clean start
DROP TABLE IF EXISTS books;

-- Create the books table for our CRUD operations
CREATE TABLE books (
                      id SERIAL PRIMARY KEY,
                      title VARCHAR(255) NOT NULL,
                      author VARCHAR(255) NOT NULL,
                      year INTEGER NOT NULL
);

-- Insert some initial adta
INSERT INTO books (title, author, year) VALUES
                                            ('The Hitchikers Guide to the Galaxy', 'Douglas Adams', 1979),
                                            ('1984', 'George Orwell', 1949),
                                            ('Pride and Prejudice', 'Jane Austen', 1813);
