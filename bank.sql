-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2025 at 05:40 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `a_customer_info`
--

CREATE TABLE `a_customer_info` (
  `account_no` bigint(19) NOT NULL,
  `Cr` decimal(10,0) NOT NULL,
  `Dr` decimal(10,0) NOT NULL,
  `date_and_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `a_customer_info`
--

INSERT INTO `a_customer_info` (`account_no`, `Cr`, `Dr`, `date_and_time`) VALUES
(1, 0, 1212, '2025-04-09 16:45:30'),
(1, 0, 1212, '2025-04-09 16:45:51'),
(1, 0, 1212, '2025-04-10 02:28:58'),
(2, 12012, 0, '2025-04-10 02:29:40'),
(2, 12012, 400, '2025-04-10 02:30:11'),
(1, 0, 1212, '2025-04-10 02:50:51');

-- --------------------------------------------------------

--
-- Table structure for table `customer_info`
--

CREATE TABLE `customer_info` (
  `account_no` bigint(16) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `date_and_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `sex` char(1) DEFAULT NULL,
  `saving` decimal(10,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_info`
--

INSERT INTO `customer_info` (`account_no`, `name`, `address`, `contact`, `date_and_time`, `sex`, `saving`) VALUES
(1, 'sagarmanibishw', 'gaighat', '9898', '2025-04-05 03:10:37', NULL, 0.00),
(2, 'Navin', 'Bista', '333', '2025-04-05 03:17:02', NULL, 0.00),
(3, 'manish', 'Buddha chowk', '434343', '2025-04-05 03:30:16', NULL, 242300.00),
(4, 'Mahesh Katuwal', 'Buddha Chowk', '2147483647', '2025-04-05 04:09:52', 'M', 0.00),
(7, 'Navin Kumar Bista', 'Gaighat 12 Buddha Chowk', '9804753546', '2025-04-05 10:23:58', 'M', 0.00),
(8, 'Navin Kumar Bista', 'Buddha Chowk', '3434343434', '2025-04-05 10:26:50', 'M', 0.00);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `a_customer_info`
--
ALTER TABLE `a_customer_info`
  ADD KEY `fk_account_no` (`account_no`);

--
-- Indexes for table `customer_info`
--
ALTER TABLE `customer_info`
  ADD PRIMARY KEY (`account_no`),
  ADD UNIQUE KEY `contact` (`contact`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_info`
--
ALTER TABLE `customer_info`
  MODIFY `account_no` bigint(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `a_customer_info`
--
ALTER TABLE `a_customer_info`
  ADD CONSTRAINT `fk_account_no` FOREIGN KEY (`account_no`) REFERENCES `customer_info` (`account_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
