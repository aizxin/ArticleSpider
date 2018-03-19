/*
Navicat MySQL Data Transfer

Source Server         : phpstudy
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : articlespider

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-03-15 00:16:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jobbole_article
-- ----------------------------
DROP TABLE IF EXISTS `jobbole_article`;
CREATE TABLE `jobbole_article` (
  `url_object_id` varchar(255) NOT NULL DEFAULT '',
  `url` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `create_date` varchar(255) DEFAULT NULL,
  `front_image_url` varchar(255) DEFAULT NULL,
  `praise_nums` varchar(255) DEFAULT NULL,
  `comment_nums` varchar(255) DEFAULT NULL,
  `fav_nums` varchar(255) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `content` text,
  `front_image_path` varchar(255) DEFAULT NULL,
  `crawl_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`url_object_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jobbole_article
-- ----------------------------
