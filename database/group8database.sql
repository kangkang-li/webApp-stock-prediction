

CREATE DATABASE stock; 

CREATE TABLE IF NOT EXISTS `historical_stock`(
   `h_id` INT UNSIGNED AUTO_INCREMENT,
   `symbol` VARCHAR(100) NOT NULL,
   `open` VARCHAR(40) NOT NULL,
   `date` DATE,
   `high` VARCHAR(40) NOT NULL,
      `low` VARCHAR(40) NOT NULL,
         `close` VARCHAR(40) NOT NULL,
	   `volume` VARCHAR(40) NOT NULL,
   PRIMARY KEY ( `h_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `realtime_stock`(
   `r_id` INT UNSIGNED AUTO_INCREMENT,
   `symbol` VARCHAR(100) NOT NULL,
   `open` VARCHAR(40) NOT NULL,
   `time` DATETIME,
   `high` VARCHAR(40) NOT NULL,
      `low` VARCHAR(40) NOT NULL,
         `close` VARCHAR(40) NOT NULL,
	   `volume` VARCHAR(40) NOT NULL,
   PRIMARY KEY ( `r_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `userinfo`(
   `fname` VARCHAR(100) NOT NULL,
      `lname` VARCHAR(100) NOT NULL,
	`email` VARCHAR(100) NOT NULL,
   `pwd` VARCHAR(40) NOT NULL,
   PRIMARY KEY ( `email` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
