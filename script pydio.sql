CREATE USER 'pydio'@'localhost' IDENTIFIED BY 'GWN6phWMeHW2VTnQ';
GRANT ALL PRIVILEGES ON * . * TO 'pydio'@'localhost';
FLUSH PRIVILEGES;


CREATE DATABASE IF NOT EXISTS pydio;
