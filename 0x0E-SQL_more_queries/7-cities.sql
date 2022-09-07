-- script that creates database hbtn_0d_usa and table cities
-- cities description:
-- id INT unique auto generated can't be null and is p key
-- state_id INT, can't be null and must be a FOREIGn KEY
--          references id of state table
-- name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE  hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
