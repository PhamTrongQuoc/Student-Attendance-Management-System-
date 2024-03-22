-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 29, 2023 at 04:55 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `phamtrongquoc_2080600990`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Account` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Account`, `Password`) VALUES
('admin', '123456'),
('trongquoc', '04032002');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `IdAuttendance` varchar(45) NOT NULL,
  `Student_id` int(11) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Class` varchar(45) DEFAULT NULL,
  `Time_in` time DEFAULT NULL,
  `Time_out` time DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Lesson_id` int(11) NOT NULL,
  `AttendanceStatus` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`IdAuttendance`, `Student_id`, `Name`, `Class`, `Time_in`, `Time_out`, `Date`, `Lesson_id`, `AttendanceStatus`) VALUES
('SV1291220232', 1, 'Pham Trong Quoc', 'Toan', '12:03:16', NULL, '29/12/2023', 2, 'Đi muộn3 phút'),
('SV1291220233', 1, 'Pham Trong Quoc', 'Toan', '13:47:53', '13:48:32', '29/12/2023', 3, 'Vắng');

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `Class` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`Class`, `Name`) VALUES
('Anh', 'Basic'),
('Toan', 'Kien thuc chuyen mon'),
('Van', 'Kien thuc chuyen mon');

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

CREATE TABLE `lesson` (
  `Lesson_id` int(11) NOT NULL,
  `Time_start` time DEFAULT NULL,
  `Time_end` time DEFAULT NULL,
  `Date` varchar(45) NOT NULL,
  `Class` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`Lesson_id`, `Time_start`, `Time_end`, `Date`, `Class`) VALUES
(1, '08:45:00', '09:45:00', '29/12/2023', 'Toan'),
(2, '12:00:00', '14:00:00', '29/12/2023', 'Toan'),
(3, '13:46:00', '18:00:00', '29/12/2023', 'Toan');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Student_id` int(11) NOT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Class` varchar(45) NOT NULL,
  `Roll` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Dob` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Student_id`, `Year`, `Semester`, `Name`, `Class`, `Roll`, `Gender`, `Dob`, `Email`, `Phone`, `Address`, `PhotoSample`) VALUES
(1, '2023', ' Kì 2(1-7)', 'Pham Trong Quoc', 'Toan', '22222222', 'Nam', '22/05/2022', 'sdsfsdf@gmail.com', '113131321321', 'BinhDinh', 'Yes'),
(2, '2023', 'Kì 1(9-1)', 'Tran Quang Vi', 'Van', '11513165416', 'Nam', '22/05/2022', 'sdfasdasd@gmail.com', '5166006510', '', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `Teacher_id` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `SecurityQ` varchar(45) NOT NULL,
  `SecurityA` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`Teacher_id`, `Name`, `Phone`, `Email`, `SecurityQ`, `SecurityA`, `Password`) VALUES
(1, 'Phạm Trọng Quốc ', '0913608840', 'phamtrongquoc@gmail.com', 'pizza', 'mèo', '123456'),
(2, 'Ba Quốc', '0913608840', 'quoc', 'pizza', 'mèo', '4322');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Account`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`IdAuttendance`),
  ADD KEY `Student_id` (`Student_id`) USING BTREE,
  ADD KEY `Lesson_id` (`Lesson_id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`Class`);

--
-- Indexes for table `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`Lesson_id`),
  ADD KEY `Class` (`Class`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Student_id`),
  ADD KEY `Class` (`Class`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`Teacher_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_3` FOREIGN KEY (`Student_id`) REFERENCES `student` (`Student_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `attendance_ibfk_4` FOREIGN KEY (`Lesson_id`) REFERENCES `lesson` (`Lesson_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `lesson`
--
ALTER TABLE `lesson`
  ADD CONSTRAINT `lesson_ibfk_1` FOREIGN KEY (`Class`) REFERENCES `class` (`Class`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`Class`) REFERENCES `class` (`Class`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
