/*
Navicat MySQL Data Transfer

Source Server         : phpstudy
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : articlespider

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2018-03-19 21:43:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ccwb_article
-- ----------------------------
DROP TABLE IF EXISTS `ccwb_article`;
CREATE TABLE `ccwb_article` (
  `url_object_id` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL COMMENT '文章url',
  `title` varchar(255) NOT NULL COMMENT '文章标题',
  `add_time` datetime DEFAULT NULL COMMENT '文章发布时间',
  `content` text,
  `source_article` varchar(255) DEFAULT NULL COMMENT '文章来源',
  `type_article` int(1) DEFAULT NULL COMMENT '文章类型',
  `create_time` datetime DEFAULT NULL COMMENT '抓起时间',
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`url_object_id`),
  UNIQUE KEY `url_object_id` (`url_object_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

