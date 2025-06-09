
-- Create the 'airlines' database if it doesn't exist
CREATE DATABASE IF NOT EXISTS airlines;
USE airlines;

-- Create table for storing passenger information
CREATE TABLE IF NOT EXISTS passengers (
    Srno INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Passport_Number VARCHAR(20),
    Age INT,
    Gender VARCHAR(10)
);

-- Create table for storing destination details
CREATE TABLE IF NOT EXISTS Destination (
    srno INT PRIMARY KEY,
    Departure VARCHAR(100),
    Arrival VARCHAR(100),
    Date DATE
);
