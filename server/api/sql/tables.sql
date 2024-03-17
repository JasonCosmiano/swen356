DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Friends CASCADE;
DROP TABLE IF EXISTS Books CASCADE;
DROP TABLE IF EXISTS Reviews CASCADE;
DROP TABLE IF EXISTS BookList CASCADE;
DROP TABLE IF EXISTS Comments CASCADE;


-- Users table
-- CREATE TABLE IF NOT EXISTS Users (
	CREATE TABLE Users (
	user_id SERIAL NOT NULL,
	username VARCHAR(25) NOT NULL,
	password VARCHAR(25) NOT NULL,
	email VARCHAR(50) NOT NULL,
	currentBook INT NULL DEFAULT NULL,
	PRIMARY KEY (user_id)
	-- FOREIGN KEY (currentBook) REFERENCES Book(id)
) ;

INSERT INTO Users
	VALUES (1, 'Test', 'password', 'test@rit.edu', 1),
			(2, 'Test2', 'password', 'test@rit.edu', 2),
			(3, 'Test3', 'password', 'test@rit.edu', 2),
			(4, 'Test4', 'password', 'test@rit.edu', 2);

ALTER SEQUENCE Users_user_id_seq RESTART WITH 5;

----------------------------------------------------------------------------------
-- Friends table

-- CREATE TABLE IF NOT EXISTS Friends (
	CREATE TABLE Friends (
	user_id INT NOT NULL,
	friend_id INT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (friend_id) REFERENCES Users(user_id),
	PRIMARY KEY (user_id, friend_id)
);

INSERT INTO  Friends
	VALUES(1, 2),
		(2, 1);

--Books Table
CREATE TABLE Books(
	id					SERIAL NOT NULL, --isbn?
	title				VARCHAR(100),
	genre				VARCHAR(20),
	author				VARCHAR(50),
	page_count			INT,
	publisher			VARCHAR(20),
	value				MONEY,
	pub_date			DATE,
	PRIMARY KEY (id)
);

INSERT INTO Books (title, genre, author, page_count, value)
	VALUES ('Book A', 'Genre A', 'John Doe', 100, 99.99),
	('Book B', 'Genre B', 'Jane Doe', 200, 59.99),
	('Book C', 'Genre C', 'Sally Smith', 300, 16.49);

-------------------------------------------------------------------
-- Reviews Table

-- CREATE TABLE IF NOT EXISTS Reviews (
    CREATE TABLE Reviews (
        id SERIAL NOT NULL,
        userID INT NOT NULL,
        title VARCHAR(50) NOT NULL,
        bookID INT NOT NULL,
        content VARCHAR(500) NOT NULL,
        FOREIGN KEY (userID) REFERENCES Users(user_id),
        FOREIGN KEY (bookID) REFERENCES Books(id),
        PRIMARY KEY (id)
    );

    INSERT INTO Reviews
    VALUES (1, 1, 'Yucky', 1, 'HELLO WORLD'),
    (2, 1, 'What?', 2, 'Book review #2');

-------------------------------------------------------------------
-- BookList Table

-- CREATE TABLE IF NOT EXISTS BookList (
    CREATE TABLE BookList (
        id SERIAL NOT NULL,
        userID INT NOT NULL,
        bookID INT NOT NULL,
        FOREIGN KEY (userID) REFERENCES Users(user_id),
        FOREIGN KEY (bookID) REFERENCES Books(id),
        PRIMARY KEY (id)
    );

    INSERT INTO BookList
    VALUES (1,1,2),
    (2,1,3);

-------------------------------------------------------------------
-- Comments Table

-- CREATE TABLE IF NOT EXISTS Comments (
    CREATE TABLE Comments (
        id SERIAL NOT NULL,
        reviewID INT NOT NULL,
        userID INT NOT NULL,
        content VARCHAR(500) NOT NULL,
        FOREIGN KEY (reviewID) REFERENCES Reviews(id),
        PRIMARY KEY (id)
    );

    INSERT INTO Comments
    VALUES (1, 1, 2, 'asdopakdafa'),
    (2, 1, 3, 'gjfdiosgjdsfd');