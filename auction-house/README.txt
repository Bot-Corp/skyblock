Do those commands in mysql query before starting the project for the first time

CREATE DATABASE `skyblock`;

CREATE TABLE `finished_auctions` (
  `auction_id` varchar(200),
  `item_name` varchar(200) NOT NULL,
  `price` float NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `buyer` varchar(200) NOT NULL,
  `seller` varchar(200) NOT NULL,
  `extra_info` varchar(2000) NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`auction_id`));

  CREATE TABLE `active_auctions` (
  `auction_id` varchar(200),
  `item_name` varchar(200) NOT NULL,
  `price` float NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `extra_info` varchar(2000) NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`auction_id`));

  CREATE TABLE `median_values` (
  `item_name` varchar(200) NOT NULL,
  `median` float NOT NULL,
  PRIMARY KEY (`item_name`));