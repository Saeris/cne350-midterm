-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Mar 21, 2024 at 03:34 AM
-- Server version: 11.3.2-MariaDB-1:11.3.2+maria~ubu2204
-- PHP Version: 8.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `states`
--
CREATE DATABASE IF NOT EXISTS `states` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `states`;

-- --------------------------------------------------------

--
-- Table structure for table `states`
--
DROP TABLE IF EXISTS `states`;
CREATE TABLE `states` (
  `State` varchar(20) DEFAULT NULL,
  `Population` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `states`
--

INSERT INTO `states` (`State`, `Population`) VALUES
('California', '39613500'),
('Texas', '29730300'),
('Florida', '21944600'),
('New York', '19300000'),
('Pennsylvania', '12804100'),
('Illinois', '12569300'),
('Ohio', '11714600'),
('Georgia', '10830000'),
('North Carolina', '10701000'),
('Michigan', '9992430'),
('New Jersey', '8874520'),
('Virginia', '8603980'),
('Washington', '7796940'),
('Arizona', '7520100'),
('Tennessee', '6944260'),
('Massachusetts', '6912240'),
('Indiana', '6805660'),
('Missouri', '6169040'),
('Maryland', '6065440'),
('Colorado', '5893630'),
('Wisconsin', '5852490'),
('Minnesota', '5706400'),
('South Carolina', '5277830'),
('Alabama', '4934190'),
('Louisiana', '4627000'),
('Kentucky', '4480710'),
('Oregon', '4289440'),
('Oklahoma', '3990440'),
('Connecticut', '3552820'),
('Utah', '3310770'),
('Puerto Rico', '3194370'),
('Nevada', '3185790'),
('Iowa', '3167970'),
('Arkansas', '3033950'),
('Mississippi', '2966410'),
('Kansas', '2917220'),
('New Mexico', '2105000'),
('Nebraska', '1952000'),
('Idaho', '1860120'),
('West Virginia', '1767860'),
('Hawaii', '1406430'),
('New Hampshire', '1372200'),
('Maine', '1354520'),
('Montana', '1085000'),
('Rhode Island', '1061510'),
('Delaware', '990334'),
('South Dakota', '896581'),
('North Dakota', '770026'),
('Alaska', '724357'),
('District of Columbia', '714153'),
('Vermont', '623251'),
('Wyoming', '581075');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
