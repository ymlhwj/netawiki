CREATE TABLE netawiki.t_neta (
	neta_name varchar(40) NOT NULL,
	neta_content TEXT NULL,
	author varchar(40) NULL,
	create_time TIMESTAMP NULL,
	editor varchar(40) NULL,
	update_time TIME NULL,
	version INT NULL,
	neta_id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (neta_id)
);

CREATE TABLE netawiki.t_comment (
	neta_name varchar(40) NOT NULL,
	content TEXT NULL,
	author varchar(40) NULL,
	create_time TIMESTAMP NULL,
  floor_num INT,
	comment_id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (comment_id)
);

CREATE TABLE netawiki.t_user (
	username varchar(40) NOT NULL,
	password varchar(40) NULL,
	create_time TIMESTAMP NULL,
  email varchar(60) NULL,
  role varchar(20) NULL,
	user_id INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (user_id)
);