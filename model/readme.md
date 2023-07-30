# table creation query:

CREATE TABLE `blood_donation`.`users` (`email` VARCHAR(35) NOT NULL , `password` VARCHAR(128) NOT NULL , `name` VARCHAR(32) NOT NULL , `blood_type` ENUM('A+','A-','B+','B-','O+','O-','AB+','AB-') NOT NULL , `location` VARCHAR(255) NOT NULL , `last_donation` DATE NULL , PRIMARY KEY (`email`)); 