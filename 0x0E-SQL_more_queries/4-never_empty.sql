-- script that creates a table -> id_not_null
-- id with default INT value, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
