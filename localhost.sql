-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 30, 2024 at 01:02 AM
-- Server version: 10.5.20-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `id22079711_database`
--
CREATE DATABASE IF NOT EXISTS `id22079711_database` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `id22079711_database`;

-- --------------------------------------------------------

--
-- Table structure for table `Airline_flght`
--

CREATE TABLE `Airline_flght` (
  `Flight_ID` varchar(8) NOT NULL,
  `Airline_Name` varchar(20) NOT NULL,
  `Flight_Number` int(10) NOT NULL,
  `Departure_Airport` varchar(20) NOT NULL,
  `Destination_Airport` varchar(20) NOT NULL,
  `Departure_Time` datetime(6) NOT NULL,
  `Arrival_Time` datetime(6) NOT NULL,
  `Duration` time(6) NOT NULL,
  `Price` int(10) NOT NULL,
  `Tourist_id` varchar(8) NOT NULL,
  `Agent_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Booking`
--

CREATE TABLE `Booking` (
  `Booking_id` varchar(8) NOT NULL,
  `Date` date NOT NULL,
  `price` int(11) NOT NULL,
  `trips` text NOT NULL,
  `discount_percentage` int(4) NOT NULL,
  `Agent_id` varchar(8) NOT NULL,
  `Tourist_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Booking_Package`
--

CREATE TABLE `Booking_Package` (
  `Booking_id` varchar(8) NOT NULL,
  `Package_id` varchar(8) NOT NULL,
  `date` date NOT NULL,
  `Discount_percentage` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Car_rental`
--

CREATE TABLE `Car_rental` (
  `Rental_ID` varchar(8) NOT NULL,
  `Car_number` varchar(7) NOT NULL,
  `Pickup_Date` date NOT NULL,
  `Rental_Duration` datetime NOT NULL,
  `Total_cost` int(8) NOT NULL,
  `Status` text NOT NULL,
  `Tourist_id` varchar(8) NOT NULL,
  `Agent_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Hotel_accomedation`
--

CREATE TABLE `Hotel_accomedation` (
  `Hotel ID` varchar(8) NOT NULL,
  `Hotel Name` varchar(20) NOT NULL,
  `Address` varchar(20) NOT NULL,
  `Rating` int(3) NOT NULL,
  `Room_Types` text NOT NULL,
  `Price_Range` int(10) NOT NULL,
  `Amenities` text NOT NULL,
  `Check-In Time` time(6) NOT NULL,
  `Check-Out Time` time(6) NOT NULL,
  `Reviews` text NOT NULL,
  `Tourist_id` varchar(8) NOT NULL,
  `Agent_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Loyalty_programe`
--

CREATE TABLE `Loyalty_programe` (
  `Programe_id` varchar(8) NOT NULL,
  `Programe_name` varchar(20) NOT NULL,
  `points` int(11) NOT NULL,
  `description` text NOT NULL,
  `discounts` int(11) NOT NULL,
  `Level_of_contributions` text NOT NULL DEFAULT 'Bronze, Silver, Gold, Platinum, Diamond',
  `Tourist_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Package`
--

CREATE TABLE `Package` (
  `Package_id` varchar(8) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `description` text NOT NULL,
  `services` text NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Tourist`
--

CREATE TABLE `Tourist` (
  `Tourist_id` varchar(8) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Age` int(2) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Points` int(11) DEFAULT NULL,
  `Favorites` text DEFAULT NULL,
  `Prefrences` text DEFAULT NULL,
  `Booking_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Travel_Agent`
--

CREATE TABLE `Travel_Agent` (
  `Agent_id` varchar(8) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(30) NOT NULL DEFAULT 'should contain @ and .com',
  `Password` varchar(20) NOT NULL,
  `Current_fund` int(11) NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Airline_flght`
--
ALTER TABLE `Airline_flght`
  ADD PRIMARY KEY (`Flight_ID`),
  ADD KEY `test10` (`Agent_id`),
  ADD KEY `test11` (`Tourist_id`);

--
-- Indexes for table `Booking`
--
ALTER TABLE `Booking`
  ADD PRIMARY KEY (`Booking_id`),
  ADD UNIQUE KEY `Tourist_id` (`Tourist_id`),
  ADD KEY `test2` (`Agent_id`);

--
-- Indexes for table `Booking_Package`
--
ALTER TABLE `Booking_Package`
  ADD KEY `Booking_id` (`Booking_id`),
  ADD KEY `Package_id` (`Package_id`);

--
-- Indexes for table `Car_rental`
--
ALTER TABLE `Car_rental`
  ADD PRIMARY KEY (`Rental_ID`),
  ADD UNIQUE KEY `Tourist_id` (`Tourist_id`,`Agent_id`),
  ADD KEY `test6` (`Agent_id`);

--
-- Indexes for table `Hotel_accomedation`
--
ALTER TABLE `Hotel_accomedation`
  ADD PRIMARY KEY (`Hotel ID`),
  ADD UNIQUE KEY `Tourist_id` (`Tourist_id`,`Agent_id`),
  ADD KEY `test8` (`Agent_id`);

--
-- Indexes for table `Loyalty_programe`
--
ALTER TABLE `Loyalty_programe`
  ADD PRIMARY KEY (`Programe_id`),
  ADD UNIQUE KEY `Tourist_id` (`Tourist_id`);

--
-- Indexes for table `Package`
--
ALTER TABLE `Package`
  ADD PRIMARY KEY (`Package_id`);

--
-- Indexes for table `Tourist`
--
ALTER TABLE `Tourist`
  ADD PRIMARY KEY (`Tourist_id`),
  ADD UNIQUE KEY `Booking_id` (`Booking_id`),
  ADD KEY `Programe_id` (`Booking_id`);

--
-- Indexes for table `Travel_Agent`
--
ALTER TABLE `Travel_Agent`
  ADD PRIMARY KEY (`Agent_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Airline_flght`
--
ALTER TABLE `Airline_flght`
  ADD CONSTRAINT `test10` FOREIGN KEY (`Agent_id`) REFERENCES `Travel_Agent` (`Agent_id`),
  ADD CONSTRAINT `test11` FOREIGN KEY (`Tourist_id`) REFERENCES `Tourist` (`Tourist_id`);

--
-- Constraints for table `Booking`
--
ALTER TABLE `Booking`
  ADD CONSTRAINT `Booking_ibfk_1` FOREIGN KEY (`Booking_id`) REFERENCES `Booking_Package` (`Booking_id`),
  ADD CONSTRAINT `test` FOREIGN KEY (`Agent_id`) REFERENCES `Travel_Agent` (`Agent_id`),
  ADD CONSTRAINT `test2` FOREIGN KEY (`Agent_id`) REFERENCES `Travel_Agent` (`Agent_id`),
  ADD CONSTRAINT `test3` FOREIGN KEY (`Tourist_id`) REFERENCES `Tourist` (`Tourist_id`);

--
-- Constraints for table `Car_rental`
--
ALTER TABLE `Car_rental`
  ADD CONSTRAINT `test6` FOREIGN KEY (`Agent_id`) REFERENCES `Travel_Agent` (`Agent_id`),
  ADD CONSTRAINT `test7` FOREIGN KEY (`Tourist_id`) REFERENCES `Tourist` (`Tourist_id`);

--
-- Constraints for table `Hotel_accomedation`
--
ALTER TABLE `Hotel_accomedation`
  ADD CONSTRAINT `test8` FOREIGN KEY (`Agent_id`) REFERENCES `Travel_Agent` (`Agent_id`),
  ADD CONSTRAINT `test9` FOREIGN KEY (`Tourist_id`) REFERENCES `Tourist` (`Tourist_id`);

--
-- Constraints for table `Loyalty_programe`
--
ALTER TABLE `Loyalty_programe`
  ADD CONSTRAINT `test4` FOREIGN KEY (`Tourist_id`) REFERENCES `Tourist` (`Tourist_id`);

--
-- Constraints for table `Package`
--
ALTER TABLE `Package`
  ADD CONSTRAINT `Package_ibfk_1` FOREIGN KEY (`Package_id`) REFERENCES `Booking_Package` (`Package_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
