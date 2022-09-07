-- script that creates table -> unique_id
-- Description: id default value 1 unique, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
