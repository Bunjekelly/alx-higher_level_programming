-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT
	state_id INT NOT NULL FOREIGN KEY(states_id) REFERENCES states(id)
	name VARCHAR(256) NOT NULL);
