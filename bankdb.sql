CREATE DATABASE bankdb;
USE bankdb;
CREATE TABLE account (
         userName VARCHAR(255) PRIMARY KEY,
         userPW VARCHAR(255),
         balance INT DEFAULT 0
     );
SELECT * FROM ACCOUNT;
