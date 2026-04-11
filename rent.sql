CREATE DATABASE pg_rent_dbase;
USE pg_rent_dbase;


CREATE TABLE pg_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pg_name VARCHAR(100),
    location VARCHAR(50),
    rent INT,
    sharing_type VARCHAR(20),
    size_sqft INT,
    wifi INT,
    ac INT,
    food INT,
    parking INT,
    laundry INT,
    power_backup INT,
    security INT,
    housekeeping INT,
    attached_bathroom INT,
    geyser INT,
    gender VARCHAR(20),
    preferred_tenant VARCHAR(20),
    rating FLOAT
);

USE pg_rent_dbase;

CREATE TABLE Rent_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(50),
    sharing_type VARCHAR(20),
    predicted_rent INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


SELECT * FROM pg_data;
SELECT COUNT(*) FROM pg_data;