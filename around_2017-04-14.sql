# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.13)
# Database: around
# Generation Time: 2017-04-14 12:26:12 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table label
# ------------------------------------------------------------

DROP TABLE IF EXISTS `label`;

CREATE TABLE `label` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `label` WRITE;
/*!40000 ALTER TABLE `label` DISABLE KEYS */;

INSERT INTO `label` (`id`, `name`)
VALUES
	(1,'约饭'),
	(2,'约电影'),
	(3,'打球');

/*!40000 ALTER TABLE `label` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table post
# ------------------------------------------------------------

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `longitude` float(9,6) DEFAULT NULL,
  `latitude` float(9,6) DEFAULT NULL,
  `label_id` int(11) DEFAULT NULL,
  `content` text,
  `timestamp` timestamp NULL DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `stop_time` datetime DEFAULT NULL,
  `is_closed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;

INSERT INTO `post` (`id`, `user_id`, `longitude`, `latitude`, `label_id`, `content`, `timestamp`, `start_time`, `stop_time`, `is_closed`)
VALUES
	(11,4,116.969299,35.595474,1,'一起吃饭啊\r\n','2017-04-09 02:50:05',NULL,NULL,NULL),
	(12,4,116.969131,35.595428,2,'想找人一起看电影','2017-04-09 02:50:57',NULL,NULL,NULL),
	(14,5,116.969193,35.595387,1,'想吃排骨、有一起的吗？我请','2017-04-09 03:30:41',NULL,NULL,NULL),
	(16,7,116.968826,35.595310,3,'有打球的吗\r\n','2017-04-09 07:40:13',NULL,NULL,NULL),
	(17,4,116.969238,35.595516,1,'自己在宿舍好无聊，有一起打球的吗','2017-04-09 10:58:01',NULL,NULL,NULL),
	(18,5,116.969398,35.595490,3,'兄弟们，有一起打篮球的吗？\r\n','2017-04-09 12:05:44',NULL,NULL,NULL),
	(19,8,116.968819,35.595577,2,'一起去看流星雨\r\n','2017-04-09 13:13:41',NULL,NULL,NULL),
	(20,9,116.968117,35.599674,2,'一起去看电影啊啊啊?','2017-04-09 14:02:17',NULL,NULL,NULL),
	(21,4,116.966583,35.594898,1,'good\r\n?','2017-04-10 08:33:55',NULL,NULL,NULL),
	(22,5,116.966583,35.594898,1,'?','2017-04-10 09:28:59',NULL,NULL,NULL),
	(23,5,116.969185,35.595318,1,'测试一下距离','2017-04-11 13:21:16',NULL,NULL,NULL),
	(24,5,116.963753,35.595497,1,'再测试一下','2017-04-11 13:27:14',NULL,NULL,NULL),
	(25,5,NULL,NULL,1,'测试一下这个定位问题','2017-04-12 07:03:34',NULL,NULL,NULL),
	(26,5,NULL,NULL,1,'测试一下这个定位问题','2017-04-12 07:04:12',NULL,NULL,NULL),
	(27,4,116.969551,35.595245,3,'qqqqqqqqqq?⚽️⚽️⚽️⚽️⚽️⚽️⚽️⚽️','2017-04-12 07:12:18',NULL,NULL,NULL);

/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL DEFAULT '',
  `password_hash` varchar(128) DEFAULT NULL,
  `pic` varchar(128) DEFAULT NULL,
  `describe` text,
  `wechat_id` varchar(30) DEFAULT NULL,
  `wechat_qr` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;

INSERT INTO `user` (`id`, `name`, `password_hash`, `pic`, `describe`, `wechat_id`, `wechat_qr`)
VALUES
	(4,'mm','pbkdf2:sha256:50000$damD0WrK$34ed55f50044f0f8c64b894ab257b1bca084fc0e46401ce6b675cd9168c88dc9','pic/22dafade4a153a6f3c8f466e30bf6249.png','爱好：吃吃吃、睡睡睡','wechat_id','pic/1c164d11e28708e8e372342e629bbcc4.jpg'),
	(5,'gg','pbkdf2:sha256:50000$IuQKZlhD$5af1be90b327592a0b1f42519d5c413d7de80e333d5309570c4cb99f2830a247','pic/4f9fedea22ed8c13638510ac151a50f7.png','hhh','elkkek','pic/7caa463d3591a11267a72d78cdf782e7.jpg'),
	(6,'admin','pbkdf2:sha256:50000$RTAt9U7B$127b6840adcf1c968f4e7ab190ff025fb2885db730a646a4424a50bb40100fb6','pic/c4b4f8789212ba5671c92db7ecb0130c.jpg','','',NULL),
	(7,'fjw','pbkdf2:sha256:50000$y0DEdlgX$ef0134c614745f04683c724b86c598d1ae956bb4b2a57d009772079582a5cc1e','pic/0cac49b3ad5a2a70874f5f9dbdce4238.jpg','好好学习','',NULL),
	(8,'hkx','pbkdf2:sha256:50000$s6ZY6fIE$c6521ff4044eb941593cf10645f4011de933b263d61f9f3dafe9eb2f3ea2446e','pic/84a4119da1a51ef2ae263317dd6c4384.jpg','1234','',NULL),
	(9,'BobSmith','pbkdf2:sha256:50000$hbbLIjx2$77c8ed2000c4f5743d581175a56b1dfa423c91e0fcc44175f3dc556caa526bd3','pic/c7917219eef4c72370cd505c24fbee40.png','blabla...','',NULL),
	(10,'test','pbkdf2:sha256:50000$Jx18t9CF$58448b251e4f50e30393aab8df682d0e451ac86df8912944cc9de7420ed8026a','pic/a8dc9cc8e2802d131eef98e2353ba7cb.jpg','','',NULL);

/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
