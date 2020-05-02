--create database , setup columns

CREATE DATABASE jiu_jitsu
CREATE TABLE users(
	user_id int, 
	first_name VARCHAR(100),
	last_name VARCHAR(100),
	email VARCHAR(255)
	);

--allows you to add, delete and drop rows,  tables or entire database
ALTER TABLE users ADD enc_password VARCHAR(1000)

ALTER TABLE users DROP COLUMN email;

DROP TABLE  users;

DROP DATABASE jiu_jitsu;


--3 databases users, movies, purchase  (movie_id and user_id are primary keys)
--users id,first, last, email, enc_password
--movies id, title, description, price
--purchases user id, movie id, datepurchase, pricepurchase


INSERT INTO movies(movie_id, title, description, price);
VALUES (1, 'Gattaca', 'Movie or documentary?', 4.99);

--check dATA USING SELECT*

SELECT * from movies;     returns table with all records
SELECT title from movies;
--returns all of the titles in one column 
SELECT title, prices from movies;
--returns two columns
SELECT title, price from movies ORDER BY price;
--returns two columns in order of price ASC or DESC  

--updating values using SET and verifying change
UPDATE movies SET price = 0.99 WHERE title = 'JAWS';
--verify
SELECT title, price from movies ORDER BY price;
--deleting and verifying
DELETE FROM movies WHERE title = 'Star Wars';
SELECT title, price from movies ORDER BY price;


SELECT title, price from movies ORDER BY price;
-----------------------------------------------------------------------------------------------------------------


-- if DATA is scattered across table we use joins to collect mathcing data and making a single table           joins
--this is called a view and collects matching data from multiple tables and makes it assessible as one table   views
-- index creation to improve time of searching huge databases with queries									   index
--transactions allow you to make sure data is safe during the processes                                        transactions

-------------------------------------------------------------------------------------------------