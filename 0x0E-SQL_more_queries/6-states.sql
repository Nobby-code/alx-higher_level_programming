-- create database hbtn_0d_usa, table states inside it
-- state description:
-- id INT unique, auto generated, can't be null and is a p key
-- name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id)
);
