DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE Users (
	"user_id" SERIAL NOT NULL,
	"username" VARCHAR(255) NOT NULL,
	"password" VARCHAR(255) NOT NULL,
	"email" VARCHAR(255) NOT NULL,
	"currentBook" VARCHAR(255) NULL DEFAULT NULL,
	"bookList" VARCHAR(255) NULL DEFAULT NULL,
	"friendList" VARCHAR(255) NULL DEFAULT NULL,
	"readingStats" VARCHAR(255) NULL DEFAULT NULL,
	PRIMARY KEY ("user_id")
) ;

INSERT INTO Users
	VALUES (1, 'Test', 'password', 'test@rit.edu', 'Tale of Deez', '7 billion books', 'no friends :(', '7 billion hours' ),
			(2, 'Test2', 'password', 'test@rit.edu', 'Tale of Nutz', '8 billion books', 'no friends :(', '8 billion hours' );