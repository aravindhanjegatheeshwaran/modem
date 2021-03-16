-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 10, 2021 at 07:52 AM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `modem`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add csv', 1, 'add_csv'),
(2, 'Can change csv', 1, 'change_csv'),
(3, 'Can delete csv', 1, 'delete_csv'),
(4, 'Can view csv', 1, 'view_csv'),
(5, 'Can add device', 2, 'add_device'),
(6, 'Can change device', 2, 'change_device'),
(7, 'Can delete device', 2, 'delete_device'),
(8, 'Can view device', 2, 'view_device'),
(9, 'Can add num', 3, 'add_num'),
(10, 'Can change num', 3, 'change_num'),
(11, 'Can delete num', 3, 'delete_num'),
(12, 'Can view num', 3, 'view_num'),
(13, 'Can add numupdate', 4, 'add_numupdate'),
(14, 'Can change numupdate', 4, 'change_numupdate'),
(15, 'Can delete numupdate', 4, 'delete_numupdate'),
(16, 'Can view numupdate', 4, 'view_numupdate'),
(17, 'Can add report', 5, 'add_report'),
(18, 'Can change report', 5, 'change_report'),
(19, 'Can delete report', 5, 'delete_report'),
(20, 'Can view report', 5, 'view_report'),
(21, 'Can add sim', 6, 'add_sim'),
(22, 'Can change sim', 6, 'change_sim'),
(23, 'Can delete sim', 6, 'delete_sim'),
(24, 'Can view sim', 6, 'view_sim'),
(25, 'Can add spin', 7, 'add_spin'),
(26, 'Can change spin', 7, 'change_spin'),
(27, 'Can delete spin', 7, 'delete_spin'),
(28, 'Can view spin', 7, 'view_spin'),
(29, 'Can add log entry', 8, 'add_logentry'),
(30, 'Can change log entry', 8, 'change_logentry'),
(31, 'Can delete log entry', 8, 'delete_logentry'),
(32, 'Can view log entry', 8, 'view_logentry'),
(33, 'Can add permission', 9, 'add_permission'),
(34, 'Can change permission', 9, 'change_permission'),
(35, 'Can delete permission', 9, 'delete_permission'),
(36, 'Can view permission', 9, 'view_permission'),
(37, 'Can add group', 10, 'add_group'),
(38, 'Can change group', 10, 'change_group'),
(39, 'Can delete group', 10, 'delete_group'),
(40, 'Can view group', 10, 'view_group'),
(41, 'Can add user', 11, 'add_user'),
(42, 'Can change user', 11, 'change_user'),
(43, 'Can delete user', 11, 'delete_user'),
(44, 'Can view user', 11, 'view_user'),
(45, 'Can add content type', 12, 'add_contenttype'),
(46, 'Can change content type', 12, 'change_contenttype'),
(47, 'Can delete content type', 12, 'delete_contenttype'),
(48, 'Can view content type', 12, 'view_contenttype'),
(49, 'Can add session', 13, 'add_session'),
(50, 'Can change session', 13, 'change_session'),
(51, 'Can delete session', 13, 'delete_session'),
(52, 'Can view session', 13, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `csv`
--

DROP TABLE IF EXISTS `csv`;
CREATE TABLE IF NOT EXISTS `csv` (
  `fid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `file_csv` varchar(100) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `csv`
--

INSERT INTO `csv` (`fid`, `name`, `file_csv`) VALUES
(1, 'ara', 'csv_file/Book12_Y72B0kZ.csv'),
(2, 'who', 'csv_file/Book12_M0g4W0p.csv'),
(3, 'be', 'csv_file/Book12_aXG2K1c.csv'),
(4, 'fadf', 'csv_file/Book12_E1DJyrc.csv'),
(5, 'hii', 'csv_file/Book12_ASwcX2p.csv'),
(6, 'demo', 'csv_file/Book12_bSuaWE1.csv'),
(7, 'sms', 'csv_file/Book12_hRXcza1.csv'),
(8, 'sms2', 'csv_file/Book12_Jir54vm.csv');

-- --------------------------------------------------------

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
CREATE TABLE IF NOT EXISTS `device` (
  `id` int NOT NULL AUTO_INCREMENT,
  `port` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `imei` varchar(100) NOT NULL,
  `signal` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `device`
--

INSERT INTO `device` (`id`, `port`, `status`, `pin`, `phone`, `imei`, `signal`, `report`) VALUES
(1, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'w'),
(2, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '6', 'e'),
(3, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '7', 'e'),
(4, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '10', 'k'),
(5, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(6, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '6', 'week'),
(7, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '7', 'week'),
(8, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '7', 'week'),
(9, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(10, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(11, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(12, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '8', 'week'),
(13, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(14, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(15, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(16, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '8', 'week'),
(17, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(18, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(19, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(20, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(21, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(22, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(23, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(24, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(25, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(26, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(27, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(28, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(29, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(30, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(31, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(32, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(33, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(34, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(35, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(36, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(37, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(38, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(39, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(40, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(41, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(42, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(43, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(44, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(45, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(46, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(47, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(48, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(49, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(50, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(51, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(52, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(53, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(54, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(55, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(56, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(57, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(58, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(59, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(60, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(61, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(62, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(63, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(64, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(65, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(66, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(67, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(68, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(69, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(70, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(71, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(72, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(73, 'COM24', 'Ready', 'Ready', 'Check the sim', '861529049197581', '5', 'week'),
(74, 'COM25', 'Ready', 'Ready', 'Check the sim', '867032056810166', '10', 'week'),
(75, 'COM26', 'Ready', 'Ready', 'Check the sim', '867032056824100', '12', 'week'),
(76, 'COM23', 'Ready', 'Ready', 'Check the sim', '861529045040041', '11', 'week'),
(77, 'COM24', 'Ready', 'Not Ready', 'Check the sim', '867032056810166', '12', 'week');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(8, 'admin', 'logentry'),
(1, 'app', 'csv'),
(2, 'app', 'device'),
(3, 'app', 'num'),
(4, 'app', 'numupdate'),
(5, 'app', 'report'),
(6, 'app', 'sim'),
(7, 'app', 'spin'),
(10, 'auth', 'group'),
(9, 'auth', 'permission'),
(11, 'auth', 'user'),
(12, 'contenttypes', 'contenttype'),
(13, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'app', '0001_initial', '2021-02-25 07:02:28.053081'),
(2, 'contenttypes', '0001_initial', '2021-02-25 08:00:32.329333'),
(3, 'auth', '0001_initial', '2021-02-25 08:00:37.897959'),
(4, 'admin', '0001_initial', '2021-02-25 08:00:53.529517'),
(5, 'admin', '0002_logentry_remove_auto_add', '2021-02-25 08:00:56.472353'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2021-02-25 08:00:56.563797'),
(7, 'contenttypes', '0002_remove_content_type_name', '2021-02-25 08:00:59.872132'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-02-25 08:01:02.022879'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-02-25 08:01:03.118378'),
(10, 'auth', '0004_alter_user_username_opts', '2021-02-25 08:01:03.222098'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-02-25 08:01:05.075245'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-02-25 08:01:05.154273'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-02-25 08:01:05.263446'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-02-25 08:01:06.778179'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-02-25 08:01:08.559165'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-02-25 08:01:09.173493'),
(17, 'auth', '0011_update_proxy_permissions', '2021-02-25 08:01:09.277431'),
(18, 'sessions', '0001_initial', '2021-02-25 08:01:10.129351'),
(19, 'app', '0002_auto_20210228_1321', '2021-02-28 07:52:45.439337');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6rfhfebo1xp0q2fm1x414rldghz2doq4', 'YTBkZGRiY2U1NWVjMTY5MGMzMWEzNDJlOTRmYTRhODJiOGI0N2E1Nzp7ImZpbmFtZSI6bnVsbH0=', '2021-03-19 05:33:18.609139');

-- --------------------------------------------------------

--
-- Table structure for table `num`
--

DROP TABLE IF EXISTS `num`;
CREATE TABLE IF NOT EXISTS `num` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(250) NOT NULL,
  `finame` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `num`
--

INSERT INTO `num` (`id`, `content`, `finame`) VALUES
(1, 'hi', 'ara'),
(2, 'hii', 'ara'),
(3, 'hii', 'ara'),
(4, 'hii', 'ara'),
(5, 'print', 'ara'),
(6, 'dg', 'ara'),
(7, 'hiiij', 'ara'),
(8, 'dfgf', 'ara'),
(9, 'hi', 'ara'),
(10, 'hii', 'ara'),
(11, 'hii arav', 'ara'),
(12, 'hii', 'ara'),
(13, 'hi', 'ara'),
(14, 'hi', 'ara'),
(15, 'hii', 'who'),
(16, 'hii', 'who'),
(17, 'hu', 'be'),
(18, 'anea', 'demo'),
(19, 'hii', 'demo'),
(20, 'hii', 'demo'),
(21, 'hii', 'demo'),
(22, 'hii', 'demo'),
(23, 'hii', 'demo'),
(24, 'hii', 'demo'),
(25, 'hii', 'demo'),
(26, 'hii', 'demo'),
(27, 'hello welcome to adaptek', 'sms2'),
(28, 'hello welcome to adaptek', 'sms2'),
(29, 'hii', 'sms2'),
(30, 'hii', 'demo'),
(31, 'hii', 'demo'),
(32, 'gi', 'hii'),
(33, 'hii', 'demo');

-- --------------------------------------------------------

--
-- Table structure for table `numupdate`
--

DROP TABLE IF EXISTS `numupdate`;
CREATE TABLE IF NOT EXISTS `numupdate` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `numupdate`
--

INSERT INTO `numupdate` (`id`, `name`, `mobile`) VALUES
(1, 'csv_file/Book12_Y72B0kZ.csv', '99887'),
(2, 'csv_file/Book12_Y72B0kZ.csv', '8695704181'),
(3, 'csv_file/Book12_Y72B0kZ.csv', '9626714714'),
(4, 'csv_file/Book12_Y72B0kZ.csv', '9789796449'),
(5, 'csv_file/Book12_M0g4W0p.csv', '99887'),
(6, 'csv_file/Book12_M0g4W0p.csv', '8695704181'),
(7, 'csv_file/Book12_M0g4W0p.csv', '9626714714'),
(8, 'csv_file/Book12_M0g4W0p.csv', '9789796449'),
(9, 'csv_file/Book12_aXG2K1c.csv', '99887'),
(10, 'csv_file/Book12_aXG2K1c.csv', '8695704181'),
(11, 'csv_file/Book12_aXG2K1c.csv', '9626714714'),
(12, 'csv_file/Book12_aXG2K1c.csv', '9789796449'),
(13, 'csv_file/Book12_E1DJyrc.csv', '99887'),
(14, 'csv_file/Book12_E1DJyrc.csv', '8695704181'),
(15, 'csv_file/Book12_E1DJyrc.csv', '9626714714'),
(16, 'csv_file/Book12_E1DJyrc.csv', '9789796449'),
(17, 'csv_file/Book12_ASwcX2p.csv', '99887'),
(18, 'csv_file/Book12_ASwcX2p.csv', '8695704181'),
(19, 'csv_file/Book12_ASwcX2p.csv', '9626714714'),
(20, 'csv_file/Book12_ASwcX2p.csv', '9789796449'),
(21, 'csv_file/Book12_bSuaWE1.csv', '7845631161'),
(22, 'csv_file/Book12_bSuaWE1.csv', '8695704181'),
(23, 'csv_file/Book12_bSuaWE1.csv', '9626714714'),
(24, 'csv_file/Book12_bSuaWE1.csv', '9789796449'),
(25, 'csv_file/Book12_hRXcza1.csv', '6374434664'),
(26, 'csv_file/Book12_hRXcza1.csv', '8925456354'),
(27, 'csv_file/Book12_hRXcza1.csv', '9551093320'),
(28, 'csv_file/Book12_hRXcza1.csv', '9600090990'),
(29, 'csv_file/Book12_hRXcza1.csv', '9600862186'),
(30, 'csv_file/Book12_Jir54vm.csv', '6374434664'),
(31, 'csv_file/Book12_Jir54vm.csv', '8695704181'),
(32, 'csv_file/Book12_Jir54vm.csv', '8925456354'),
(33, 'csv_file/Book12_Jir54vm.csv', '9551093320'),
(34, 'csv_file/Book12_Jir54vm.csv', '9600090990'),
(35, 'csv_file/Book12_Jir54vm.csv', '9600862186');

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
CREATE TABLE IF NOT EXISTS `report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `num` varchar(50) NOT NULL,
  `msg` varchar(250) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `pin` varchar(50) NOT NULL,
  `port` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`id`, `num`, `msg`, `date`, `status`, `pin`, `port`) VALUES
(1, '8695704181', 'hi', '2021-02-25', 'success', '', ''),
(2, '8695704181', 'hi', '2021-02-25', 'success', '', ''),
(3, '8695704181', 'hi', '2021-02-25', 'success', '', ''),
(4, '8695704181', 'hi', '2021-02-25', 'success', '', ''),
(5, '9626714714', 'hi', '2021-02-25', 'success', '', ''),
(6, '9626714714', 'hi', '2021-02-25', 'success', '', ''),
(7, '9626714714', 'hi', '2021-02-25', 'success', '', ''),
(8, '9789796449', 'hi', '2021-02-25', 'success', '', ''),
(9, '9789796449', 'hi', '2021-02-25', 'success', '', ''),
(10, '9789796449', 'hi', '2021-02-25', 'success', '', ''),
(11, '9626714714', 'hi', '2021-02-25', 'success', '', ''),
(12, '99887', 'hi', '2021-02-25', 'success', '', ''),
(13, '99887', 'hi', '2021-02-25', 'success', '', ''),
(14, '99887', 'hi', '2021-02-25', 'success', '', ''),
(15, '9789796449', 'hi', '2021-02-25', 'success', '', ''),
(16, '99887', 'hi', '2021-02-25', 'success', '', ''),
(17, '99887', 'hii', '2021-02-26', 'fail', 'A', ''),
(18, '99887', 'hii', '2021-02-26', 'fail', 'A', ''),
(19, '99887', 'hii', '2021-02-26', 'fail', 'A', ''),
(20, '99887', 'hii', '2021-02-26', 'fail', 'A', ''),
(21, '99887', 'print', '2021-02-26', 'fail', 'A', ''),
(22, '99887', 'print', '2021-02-26', 'fail', 'A', ''),
(23, '99887', 'print', '2021-02-26', 'fail', 'A', ''),
(24, '99887', 'print', '2021-02-26', 'fail', 'A', ''),
(25, '99887', 'dg', '2021-02-26', 'fail', 'A', ''),
(26, '99887', 'dg', '2021-02-26', 'fail', 'A', ''),
(27, '99887', 'dg', '2021-02-26', 'fail', 'A', ''),
(28, '99887', 'dg', '2021-02-26', 'fail', 'A', ''),
(29, '99887', 'hiiij', '2021-02-26', 'fail', 'A', ''),
(30, '99887', 'hiiij', '2021-02-26', 'fail', 'A', ''),
(31, '99887', 'dfgf', '2021-02-26', 'fail', 'A', ''),
(32, '99887', 'dfgf', '2021-02-26', 'fail', 'A', ''),
(33, '99887', 'hii', '2021-02-26', 'fail', 'A', ''),
(34, '99887', 'hii', '2021-02-26', 'fail', 'A', ''),
(35, '8695704181', 'hii arav', '2021-02-26', 'success', 'A', ''),
(36, '8695704181', 'hii arav', '2021-02-26', 'success', 'A', ''),
(37, '9626714714', 'hii arav', '2021-02-26', 'fail', 'B', ''),
(38, '9789796449', 'hii arav', '2021-02-26', 'fail', 'B', ''),
(39, '9626714714', 'hii arav', '2021-02-26', 'fail', 'B', ''),
(40, '99887', 'hii arav', '2021-02-26', 'fail', 'B', ''),
(41, '9789796449', 'hii arav', '2021-02-26', 'fail', 'B', ''),
(42, '99887', 'hii arav', '2021-02-26', 'fail', 'B', ''),
(43, '9789796449', 'hii', '2021-02-28', 'fail', 'B', ''),
(44, '9626714714', 'hii', '2021-02-28', 'fail', 'B', ''),
(45, '8695704181', 'hii', '2021-02-28', 'fail', 'B', ''),
(46, '9789796449', 'hi', '2021-02-28', 'fail', 'A', ''),
(47, '8695704181', 'hi', '2021-02-28', 'fail', 'A', ''),
(48, '99887', 'hi', '2021-02-28', 'fail', 'A', ''),
(49, '9626714714', 'hi', '2021-02-28', 'fail', 'A', ''),
(50, '9789796449', 'hii', '2021-02-28', 'fail', 'A', ''),
(51, '8695704181', 'hii', '2021-02-28', 'success', 'A', ''),
(52, '99887', 'hii', '2021-02-28', 'fail', 'A', ''),
(53, '9626714714', 'hii', '2021-02-28', 'success', 'B', ''),
(54, '9789796449', 'hii', '2021-03-04', 'success', 'A', 'COM26'),
(55, '8695704181', 'hii', '2021-03-04', 'success', 'A', 'COM25'),
(56, '7845631161', 'hii', '2021-03-04', 'fail', 'B', 'COM26'),
(57, '9626714714', 'hii', '2021-03-04', 'success', 'B', 'COM25'),
(58, '9551093320', 'hello welcome to adaptek', '2021-03-04', 'success', 'A', 'COM25'),
(59, '9551093320', 'hello welcome to adaptek', '2021-03-04', 'success', 'A', 'COM26'),
(60, '9600090990', 'hello welcome to adaptek', '2021-03-04', 'success', 'B', 'COM25'),
(61, '9600090990', 'hello welcome to adaptek', '2021-03-04', 'success', 'B', 'COM26'),
(62, '8925456354', 'hello welcome to adaptek', '2021-03-04', 'success', 'B', 'COM25'),
(63, '8925456354', 'hello welcome to adaptek', '2021-03-04', 'success', 'B', 'COM26'),
(64, '6374434664', 'hello welcome to adaptek', '2021-03-04', 'success', 'B', 'COM25'),
(65, '6374434664', 'hello welcome to adaptek', '2021-03-04', 'fail', 'B', 'COM26'),
(66, '9600862186', 'hello welcome to adaptek', '2021-03-04', 'fail', 'B', 'COM26'),
(67, '9600862186', 'hello welcome to adaptek', '2021-03-04', 'fail', 'B', 'COM25'),
(68, '9551093320', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(69, '9600090990', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(70, '8925456354', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(71, '6374434664', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(72, '9600862186', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(73, '9551093320', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(74, '9600090990', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(75, '8925456354', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(76, '6374434664', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(77, '9600862186', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(78, '8695704181', 'hello welcome to adaptek', '2021-03-04', 'fail', 'A', 'COM26'),
(79, '(784)563-1161', 'hii', '2021-03-05', 'fail', 'A', 'COM24'),
(80, '(962)671-4714', 'hii', '2021-03-05', 'fail', 'A', 'COM26'),
(81, '(978)979-6449', 'hii', '2021-03-05', 'fail', 'A', 'COM23'),
(82, '(869)570-4181', 'hii', '2021-03-05', 'fail', 'A', 'COM25'),
(83, '(962)671-4714', 'hii', '2021-03-05', 'fail', 'A', 'COM26'),
(84, '(784)563-1161', 'hii', '2021-03-05', 'fail', 'A', 'COM25'),
(85, '(978)979-6449', 'hii', '2021-03-05', 'fail', 'A', 'COM26'),
(86, '(869)570-4181', 'hii', '2021-03-05', 'fail', 'A', 'COM25'),
(87, '9626714714', 'hii', '2021-03-05, 11:03:24', 'fail', 'A', 'COM26'),
(88, '9789796449', 'hii', '2021-03-05, 11:03:24', 'fail', 'A', 'COM26'),
(89, '7845631161', 'hii', '2021-03-05, 11:03:24', 'success', 'A', 'COM25'),
(90, '8695704181', 'hii', '2021-03-05, 11:03:24', 'success', 'B', 'COM25');

-- --------------------------------------------------------

--
-- Table structure for table `sim`
--

DROP TABLE IF EXISTS `sim`;
CREATE TABLE IF NOT EXISTS `sim` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pin` varchar(50) NOT NULL,
  `port` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=464 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sim`
--

INSERT INTO `sim` (`id`, `pin`, `port`) VALUES
(1, 'False', ''),
(2, 'False', ''),
(3, 'False', ''),
(4, 'False', ''),
(5, 'False', ''),
(6, 'False', ''),
(7, 'False', ''),
(8, 'False', ''),
(9, 'False', ''),
(10, 'False', ''),
(11, 'False', ''),
(12, 'False', ''),
(13, 'False', ''),
(14, 'False', ''),
(15, 'False', ''),
(16, 'False', ''),
(17, 'True', ''),
(18, 'True', ''),
(19, 'False', ''),
(20, 'False', ''),
(21, 'False', ''),
(22, 'False', ''),
(23, 'False', ''),
(24, 'False', ''),
(25, 'False', ''),
(26, 'False', ''),
(27, 'False', ''),
(28, 'False', ''),
(29, 'False', ''),
(30, 'False', ''),
(31, 'False', ''),
(32, 'False', ''),
(33, 'False', ''),
(34, 'False', ''),
(35, 'False', ''),
(36, 'False', ''),
(37, 'False', ''),
(38, 'False', ''),
(39, 'False', ''),
(40, 'False', ''),
(41, 'False', ''),
(42, 'False', ''),
(43, 'False', ''),
(44, 'False', ''),
(45, 'False', ''),
(46, 'False', ''),
(47, 'False', ''),
(48, 'False', ''),
(49, 'True', ''),
(50, 'False', ''),
(51, 'False', ''),
(52, 'False', ''),
(53, 'False', ''),
(54, 'False', ''),
(55, 'False', ''),
(56, 'False', ''),
(57, 'False', ''),
(58, 'False', ''),
(59, 'False', ''),
(60, 'False', ''),
(61, 'False', ''),
(62, 'False', ''),
(63, 'False', ''),
(64, 'False', ''),
(65, 'False', ''),
(66, 'False', ''),
(67, 'False', ''),
(68, 'False', ''),
(69, 'False', ''),
(70, 'False', ''),
(71, 'False', ''),
(72, 'False', ''),
(73, 'True', ''),
(74, 'True', ''),
(75, 'True', ''),
(76, 'True', ''),
(77, 'True', ''),
(78, 'True', ''),
(79, 'True', ''),
(80, 'True', ''),
(81, 'True', ''),
(82, 'False', ''),
(83, 'False', ''),
(84, 'False', ''),
(85, 'False', ''),
(86, 'False', ''),
(87, 'False', ''),
(88, 'False', ''),
(89, 'False', ''),
(90, 'False', ''),
(91, 'False', ''),
(92, 'False', ''),
(93, 'False', ''),
(94, 'False', ''),
(95, 'False', ''),
(96, 'False', ''),
(97, 'False', ''),
(98, 'False', ''),
(99, 'False', ''),
(100, 'False', ''),
(101, 'False', ''),
(102, 'False', ''),
(103, 'False', ''),
(104, 'False', ''),
(105, 'True', ''),
(106, 'False', ''),
(107, 'False', ''),
(108, 'False', ''),
(109, 'False', ''),
(110, 'False', ''),
(111, 'False', ''),
(112, 'False', ''),
(113, 'False', ''),
(114, 'False', ''),
(115, 'False', ''),
(116, 'False', ''),
(117, 'False', ''),
(118, 'False', ''),
(119, 'False', ''),
(120, 'False', ''),
(121, 'True', ''),
(122, 'True', ''),
(123, 'True', ''),
(124, 'True', ''),
(125, 'True', ''),
(126, 'True', ''),
(127, 'True', ''),
(128, 'True', ''),
(129, 'True', ''),
(130, 'False', ''),
(131, 'False', ''),
(132, 'False', ''),
(133, 'False', ''),
(134, 'False', ''),
(135, 'False', ''),
(136, 'False', ''),
(137, 'False', ''),
(138, 'False', ''),
(139, 'False', ''),
(140, 'False', ''),
(141, 'False', ''),
(142, 'False', ''),
(143, 'False', ''),
(144, 'False', ''),
(145, 'False', ''),
(146, 'False', ''),
(147, 'False', ''),
(148, 'False', ''),
(149, 'False', ''),
(150, 'False', ''),
(151, 'False', ''),
(152, 'False', ''),
(153, 'True', ''),
(154, 'True', ''),
(155, 'True', ''),
(156, 'True', ''),
(157, 'True', ''),
(158, 'True', ''),
(159, 'True', ''),
(160, 'True', ''),
(161, 'True', ''),
(162, 'False', ''),
(163, 'False', ''),
(164, 'False', ''),
(165, 'False', ''),
(166, 'False', ''),
(167, 'False', ''),
(168, 'False', ''),
(169, 'False', ''),
(170, 'False', ''),
(171, 'False', ''),
(172, 'False', ''),
(173, 'False', ''),
(174, 'False', ''),
(175, 'False', ''),
(176, 'False', ''),
(177, 'False', ''),
(178, 'False', ''),
(179, 'False', ''),
(180, 'False', ''),
(181, 'False', ''),
(182, 'False', ''),
(183, 'False', ''),
(184, 'False', ''),
(185, 'True', ''),
(186, 'True', ''),
(187, 'True', ''),
(188, 'True', ''),
(189, 'True', ''),
(190, 'True', ''),
(191, 'True', ''),
(192, 'True', ''),
(193, 'True', ''),
(194, 'False', ''),
(195, 'False', ''),
(196, 'False', ''),
(197, 'False', ''),
(198, 'False', ''),
(199, 'False', ''),
(200, 'False', ''),
(201, 'False', ''),
(202, 'False', ''),
(203, 'False', ''),
(204, 'False', ''),
(205, 'False', ''),
(206, 'False', ''),
(207, 'False', ''),
(208, 'False', ''),
(209, 'False', ''),
(210, 'False', ''),
(211, 'False', ''),
(212, 'False', ''),
(213, 'False', ''),
(214, 'False', ''),
(215, 'False', ''),
(216, 'False', ''),
(217, 'True', ''),
(218, 'True', ''),
(219, 'True', ''),
(220, 'True', ''),
(221, 'True', ''),
(222, 'True', ''),
(223, 'True', ''),
(224, 'True', ''),
(225, 'True', ''),
(226, 'True', ''),
(227, 'False', ''),
(228, 'False', ''),
(229, 'False', ''),
(230, 'False', ''),
(231, 'False', ''),
(232, 'False', ''),
(233, 'False', ''),
(234, 'False', ''),
(235, 'False', ''),
(236, 'False', ''),
(237, 'False', ''),
(238, 'False', ''),
(239, 'False', ''),
(240, 'False', ''),
(241, 'False', ''),
(242, 'False', ''),
(243, 'False', ''),
(244, 'False', ''),
(245, 'False', ''),
(246, 'False', ''),
(247, 'False', ''),
(248, 'False', ''),
(249, 'False', ''),
(250, 'False', ''),
(251, 'False', ''),
(252, 'False', ''),
(253, 'False', ''),
(254, 'False', ''),
(255, 'False', ''),
(256, 'False', ''),
(257, 'True', ''),
(258, 'True', ''),
(259, 'False', ''),
(260, 'False', ''),
(261, 'False', ''),
(262, 'False', ''),
(263, 'False', ''),
(264, 'False', ''),
(265, 'False', ''),
(266, 'False', ''),
(267, 'False', ''),
(268, 'False', ''),
(269, 'False', ''),
(270, 'False', ''),
(271, 'False', ''),
(272, 'False', ''),
(273, 'False', ''),
(274, 'False', ''),
(275, 'False', ''),
(276, 'False', ''),
(277, 'False', ''),
(278, 'False', ''),
(279, 'False', ''),
(280, 'False', ''),
(281, 'True', ''),
(282, 'False', ''),
(283, 'False', ''),
(284, 'False', ''),
(285, 'False', ''),
(286, 'False', ''),
(287, 'False', ''),
(288, 'False', ''),
(289, 'False', ''),
(290, 'False', ''),
(291, 'False', ''),
(292, 'False', ''),
(293, 'True', ''),
(294, 'True', ''),
(295, 'True', ''),
(296, 'True', ''),
(297, 'True', ''),
(298, 'True', ''),
(299, 'True', ''),
(300, 'True', ''),
(301, 'True', ''),
(302, 'True', ''),
(303, 'False', ''),
(304, 'False', ''),
(305, 'False', ''),
(306, 'False', ''),
(307, 'False', ''),
(308, 'False', ''),
(309, 'False', ''),
(310, 'False', ''),
(311, 'False', ''),
(312, 'False', ''),
(313, 'False', ''),
(314, 'True', ''),
(315, 'True', ''),
(316, 'True', ''),
(317, 'True', ''),
(318, 'True', ''),
(319, 'True', ''),
(320, 'True', ''),
(321, 'True', ''),
(322, 'False', ''),
(323, 'False', ''),
(324, 'False', ''),
(325, 'False', ''),
(326, 'False', ''),
(327, 'False', ''),
(328, 'False', ''),
(329, 'False', ''),
(330, 'False', ''),
(331, 'False', ''),
(332, 'False', ''),
(333, 'False', ''),
(334, 'False', ''),
(335, 'False', ''),
(336, 'False', ''),
(337, 'False', ''),
(338, 'False', ''),
(339, 'False', ''),
(340, 'False', ''),
(341, 'False', ''),
(342, 'False', ''),
(343, 'False', ''),
(344, 'False', ''),
(345, 'False', ''),
(346, 'True', ''),
(347, 'True', ''),
(348, 'True', ''),
(349, 'True', ''),
(350, 'True', ''),
(351, 'True', ''),
(352, 'True', ''),
(353, 'True', ''),
(354, 'True', ''),
(355, 'True', ''),
(356, 'False', ''),
(357, 'False', ''),
(358, 'False', ''),
(359, 'False', ''),
(360, 'False', ''),
(361, 'False', ''),
(362, 'False', ''),
(363, 'False', ''),
(364, 'False', ''),
(365, 'False', ''),
(366, 'False', ''),
(367, 'False', ''),
(368, 'False', ''),
(369, 'False', ''),
(370, 'False', ''),
(371, 'False', ''),
(372, 'False', ''),
(373, 'False', ''),
(374, 'False', ''),
(375, 'False', ''),
(376, 'False', ''),
(377, 'False', ''),
(378, 'True', ''),
(379, 'True', ''),
(380, 'True', ''),
(381, 'True', ''),
(382, 'True', ''),
(383, 'True', ''),
(384, 'True', ''),
(385, 'True', ''),
(386, 'True', ''),
(387, 'True', ''),
(388, 'False', ''),
(389, 'False', ''),
(390, 'False', ''),
(391, 'False', ''),
(392, 'False', ''),
(393, 'False', ''),
(394, 'False', ''),
(395, 'False', ''),
(396, 'False', ''),
(397, 'False', ''),
(398, 'False', ''),
(399, 'False', ''),
(400, 'False', ''),
(401, 'False', ''),
(402, 'False', ''),
(403, 'False', ''),
(404, 'False', ''),
(405, 'False', ''),
(406, 'False', ''),
(407, 'False', ''),
(408, 'False', ''),
(409, 'False', ''),
(410, 'True', ''),
(411, 'True', ''),
(412, 'True', ''),
(413, 'True', ''),
(414, 'True', ''),
(415, 'True', ''),
(416, 'True', ''),
(417, 'True', ''),
(418, 'False', ''),
(419, 'False', ''),
(420, 'False', ''),
(421, 'False', ''),
(422, 'False', ''),
(423, 'False', ''),
(424, 'False', ''),
(425, 'False', ''),
(426, 'False', ''),
(427, 'False', ''),
(428, 'False', ''),
(429, 'False', ''),
(430, 'False', ''),
(431, 'False', ''),
(432, 'False', ''),
(433, 'False', ''),
(434, 'False', ''),
(435, 'False', ''),
(436, 'False', ''),
(437, 'False', ''),
(438, 'False', ''),
(439, 'False', ''),
(440, 'True', ''),
(441, 'True', ''),
(442, 'True', ''),
(443, 'True', ''),
(444, 'True', ''),
(445, 'True', ''),
(446, 'True', ''),
(447, 'True', ''),
(448, 'True', ''),
(449, 'True', ''),
(450, 'False', ''),
(451, 'False', ''),
(452, 'False', ''),
(453, 'False', ''),
(454, 'False', ''),
(455, 'False', ''),
(456, 'False', ''),
(457, 'False', ''),
(458, 'False', ''),
(459, 'False', ''),
(460, 'False', ''),
(461, 'False', ''),
(462, 'False', ''),
(463, 'False', '');

-- --------------------------------------------------------

--
-- Table structure for table `spin`
--

DROP TABLE IF EXISTS `spin`;
CREATE TABLE IF NOT EXISTS `spin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `port` varchar(50) NOT NULL,
  `sim` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `spin`
--

INSERT INTO `spin` (`id`, `port`, `sim`) VALUES
(1, 'COM25', 'A'),
(2, 'COM24', 'A'),
(3, 'COM26', 'A'),
(4, 'COM23', 'A'),
(5, 'COM25', 'B'),
(6, 'COM24', 'B'),
(7, 'COM23', 'B'),
(8, 'COM26', 'B'),
(9, 'COM24', 'B'),
(10, 'COM25', 'B'),
(11, 'COM23', 'B'),
(12, 'COM24', 'B'),
(13, 'COM25', 'B'),
(14, 'COM23', 'B'),
(15, 'COM26', 'B'),
(16, 'COM26', 'B'),
(17, 'COM24', 'A'),
(18, 'COM26', 'A'),
(19, 'COM24', 'A'),
(20, 'COM23', 'A'),
(21, 'COM25', 'A'),
(22, 'COM24', 'A'),
(23, 'COM23', 'A'),
(24, 'COM26', 'A'),
(25, 'COM25', 'A'),
(26, 'COM24', 'A'),
(27, 'COM23', 'A'),
(28, 'COM25', 'A'),
(29, 'COM26', 'A'),
(30, 'COM25', 'A'),
(31, 'COM26', 'A'),
(32, 'COM25', 'A'),
(33, 'COM26', 'A'),
(34, 'COM26', 'A'),
(35, 'COM25', 'A'),
(36, 'COM25', 'A'),
(37, 'COM26', 'A'),
(38, 'COM25', 'B'),
(39, 'COM25', 'B'),
(40, 'COM26', 'B'),
(41, 'COM25', 'B'),
(42, 'COM26', 'B'),
(43, 'COM26', 'B'),
(44, 'COM25', 'B'),
(45, 'COM24', 'B'),
(46, 'COM26', 'B'),
(47, 'COM26', 'A'),
(48, 'COM25', 'A'),
(49, 'COM26', 'A'),
(50, 'COM25', 'A'),
(51, 'COM25', 'A'),
(52, 'COM26', 'A'),
(53, 'COM26', 'A'),
(54, 'COM25', 'B'),
(55, 'COM26', 'A'),
(56, 'COM25', 'A'),
(57, 'COM26', 'B'),
(58, 'COM25', 'B'),
(59, 'COM25', 'A'),
(60, 'COM26', 'A'),
(61, 'COM25', 'B'),
(62, 'COM26', 'B'),
(63, 'COM25', 'B'),
(64, 'COM26', 'B'),
(65, 'COM25', 'B'),
(66, 'COM26', 'B'),
(67, 'COM25', 'B'),
(68, 'COM26', 'B'),
(69, 'COM26', 'A'),
(70, 'COM26', 'A'),
(71, 'COM26', 'A'),
(72, 'COM26', 'A'),
(73, 'COM26', 'A'),
(74, 'COM26', 'A'),
(75, 'COM26', 'A'),
(76, 'COM26', 'A'),
(77, 'COM26', 'A'),
(78, 'COM26', 'A'),
(79, 'COM26', 'A'),
(80, 'COM24', 'A'),
(81, 'COM25', 'A'),
(82, 'COM23', 'A'),
(83, 'COM26', 'A'),
(84, 'COM25', 'A'),
(85, 'COM26', 'A'),
(86, 'COM26', 'A'),
(87, 'COM25', 'A'),
(88, 'COM26', 'A'),
(89, 'COM25', 'A'),
(90, 'COM26', 'A'),
(91, 'COM25', 'B');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
