-- Criação das tabelas da Staging Area
-- As constraints e a Surrogate Key serão adicionadas no DW.


CREATE TABLE IF NOT EXISTS staging_area.st_country(
	country_id VARCHAR(5),
	currency VARCHAR(15),
	shoe_metric VARCHAR (5)
);



CREATE TABLE IF NOT EXISTS staging_area.st_shoes_dim(
	shoes_id VARCHAR(10),
	name VARCHAR(60),
	best_for_wear VARCHAR(20),
	gender VARCHAR(5),
	image_url VARCHAR(250),
	dominant_color VARCHAR(20),
	sub_color1 VARCHAR(20),
	sub_color2 VARCHAR(20)
);



CREATE TABLE IF NOT EXISTS staging_area.st_shoes_fact(
	serial_id INT,
	shoes_id VARCHAR(10),
	price DECIMAL(10, 2),
	category VARCHAR(15),
	size VARCHAR (10),
	stock INT,
	date INT,
	country_id VARCHAR(5)
);