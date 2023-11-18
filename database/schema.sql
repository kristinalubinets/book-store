CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_first_name VARCHAR(50) NOT NULL,
    author_last_name VARCHAR(50) NOT NULL,
    genre VARCHAR(50) NOT NULL,
    publication_year INT,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO books (title, author_first_name, author_last_name, genre, publication_year, price)
VALUES
    ('The Raven', 'Edgar Allan', 'Poe', 'Poetry', 1845, 9.99),
    ('The Tell-Tale Heart', 'Edgar Allan', 'Poe', 'Horror', 1843, 11.99),
    ('The Fall of the House of Usher', 'Edgar Allan', 'Poe', 'Gothic', 1839, 14.99),
    ('1984', 'George', 'Orwell', 'Dystopian', 1949, 14.99),
    ('The Great Gatsby', 'F. Scott', 'Fitzgerald', 'Classic', 1925, 12.99),
    ('The Hobbit', 'J.R.R.', 'Tolkien', 'Fantasy', 1937, 22.99),
    ('Pride and Prejudice', 'Jane', 'Austen', 'Classic', 1813, 15.99);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(15)
);

INSERT INTO customers (first_name, last_name, email, address, phone_number)
VALUES
    ('John', 'Doe', 'john.doe@email.com', '123 Main St', '555-1234'),
    ('Jane', 'Smith', 'jane.smith@email.com', '456 Oak St', '555-5678');

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    book_id INT REFERENCES books(book_id),
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
 
INSERT INTO orders (customer_id, order_date, total_amount, book_id, quantity, price)
VALUES
    (1, '2023-11-15'::DATE, 21.98, 1, 2, 9.99),  -- Order for 'The Raven' for Customer John Doe
    (2, '2023-11-15'::DATE, 46.97, 4, 3, 11.99);  -- Order for '1984' for Customer Jane Smith
   