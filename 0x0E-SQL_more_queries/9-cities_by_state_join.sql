-- displays all cities in the database hbtn_0d_usa
-- each record should displaY cities.id - cities.name states.name
-- reuslts sorted in ascending order
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
