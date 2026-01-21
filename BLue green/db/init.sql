CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    version VARCHAR(10) NOT NULL,
    message VARCHAR(255) NOT NULL
);

INSERT INTO messages (version, message) VALUES ('blue', 'This is the blue version message!');
INSERT INTO messages (version, message) VALUES ('green', 'This is the green version message!');