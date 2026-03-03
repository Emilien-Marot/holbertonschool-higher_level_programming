-- comment
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_1'@'localhost';
