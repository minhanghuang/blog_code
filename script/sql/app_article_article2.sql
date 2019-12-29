/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : blog_db

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 29/12/2019 12:33:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app_article_article
-- ----------------------------
DROP TABLE IF EXISTS `app_article_article`;
CREATE TABLE `app_article_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL,
  `subtitle` longtext NOT NULL,
  `content` longtext NOT NULL,
  `readcount` int(11) NOT NULL,
  `createdate` datetime(6) NOT NULL,
  `updatedate` datetime(6) NOT NULL,
  `state` int(11) NOT NULL,
  `image` longtext NOT NULL,
  `istop` int(11) NOT NULL,
  `tag` varchar(127) NOT NULL,
  `category` varchar(127) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_article_article_author_id_b5186284_fk_app_user_` (`author_id`),
  CONSTRAINT `app_article_article_author_id_b5186284_fk_app_user_` FOREIGN KEY (`author_id`) REFERENCES `app_user_UserProfile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_article_article
-- ----------------------------
BEGIN;
INSERT INTO `app_article_article` VALUES (1, 'RabbitMQ在Python中的使用详解', 'q', '1', 41, '2019-12-24 21:58:00.429613', '2019-12-25 21:55:15.391184', 1, '1', 0, '1', '{}', 1);
COMMIT;
SET FOREIGN_KEY_CHECKS=1;