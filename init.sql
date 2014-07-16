/******************************************/
/*   init.sql - Initialize the database   */
/* DO NOT RUN ON PRODUCTION SERVER UNLESS */
/*     YOU KNOW WHAT YOU ARE DOING!!!     */
/******************************************/

DROP TABLE IF EXISTS meetings;

CREATE TABLE meetings (
	id SERIAL,
	meeting INT NOT NULL,
	time_started TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	time_finished TIMESTAMP,
	PRIMARY KEY (id));
