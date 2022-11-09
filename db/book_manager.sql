DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name TEXT,
    bio TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    page_count INT,
    has_read BOOLEAN,
    author_id INT NOT NULL REFERENCES authors(id)
);

INSERT INTO authors (name, bio) VALUES ('Terry Pratchett', 'A very popular and prolific fantasy author');
INSERT INTO authors (name, bio) VALUES ('David Spiegelhalter', 'Statistics professor');
INSERT INTO authors (name, bio) VALUES ('Ian Stewart', 'Mathematics professor');
INSERT INTO authors (name, bio) VALUES ('Bill Bryson', 'Popular non-fiction and travel author');
INSERT INTO authors (name, bio) VALUES ('Primo Levi', 'Italian chemist and author');

INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('Equal Rites', 120, True, (SELECT id FROM authors WHERE name = 'Terry Pratchett'));
INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('Mort', 150, True, (SELECT id FROM authors WHERE name = 'Terry Pratchett'));
INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('Interesting Times', 140, True, (SELECT id FROM authors WHERE name = 'Terry Pratchett'));
INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('The Art Of Statistics', 300, False, (SELECT id FROM authors WHERE name = 'David Spiegelhalter'));
INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('Flatterland', 150, True, (SELECT id FROM authors WHERE name = 'Ian Stewart'));
INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('Galois Theory', 400, True, (SELECT id FROM authors WHERE name = 'Ian Stewart'));
INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('Mother Tongue: The English Language', 320, False, (SELECT id FROM authors WHERE name = 'Bill Bryson'));
INSERT INTO books (title, page_count, has_read, author_id)
    VALUES ('The Periodic Table', 210, False, (SELECT id FROM authors WHERE name = 'Primo Levi'));
