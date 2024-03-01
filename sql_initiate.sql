CREATE DATABASE Blood_bank_management; 
USE Blood_bank_management;

CREATE TABLE users (
  username VARCHAR(255) PRIMARY KEY,
  password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE blood_bank (
  blood_type VARCHAR(255) NOT NULL,
  donor_name VARCHAR(255),
  donor_age INT,
  donor_gender VARCHAR(255),
  donor_phone VARCHAR(255),
  date_received DATE,
  recipient_name VARCHAR(255),
  quantity INT NOT NULL
);

CREATE TABLE donors ( -- Optional, comment out if not needed
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  age INT,
  gender VARCHAR(255),
  phone_number VARCHAR(255),
  date_received DATE
);