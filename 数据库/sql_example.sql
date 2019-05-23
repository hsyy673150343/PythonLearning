/*
Navicat MySQL Data Transfer

Source Server         : hongsong
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : sql_example

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-05-23 16:37:19
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(32) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('1', '三年二班');
INSERT INTO `class` VALUES ('2', '三年三班');
INSERT INTO `class` VALUES ('3', '一年二班');
INSERT INTO `class` VALUES ('4', '二年九班');

-- ----------------------------
-- Table structure for `course`
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(32) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`cid`),
  KEY `fk_course_teacher` (`teacher_id`),
  CONSTRAINT `fk_course_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('1', '生物', '1');
INSERT INTO `course` VALUES ('2', '物理', '2');
INSERT INTO `course` VALUES ('3', '体育', '3');
INSERT INTO `course` VALUES ('4', '美术', '2');

-- ----------------------------
-- Table structure for `score`
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`sid`),
  KEY `fk_score_student` (`student_id`),
  KEY `fk_score_course` (`course_id`),
  CONSTRAINT `fk_score_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`cid`),
  CONSTRAINT `fk_score_student` FOREIGN KEY (`student_id`) REFERENCES `student` (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES ('1', '1', '1', '10');
INSERT INTO `score` VALUES ('2', '1', '2', '9');
INSERT INTO `score` VALUES ('5', '1', '4', '66');
INSERT INTO `score` VALUES ('6', '2', '1', '8');
INSERT INTO `score` VALUES ('8', '2', '3', '68');
INSERT INTO `score` VALUES ('9', '2', '4', '99');
INSERT INTO `score` VALUES ('10', '3', '1', '77');
INSERT INTO `score` VALUES ('11', '3', '2', '66');
INSERT INTO `score` VALUES ('12', '3', '3', '87');
INSERT INTO `score` VALUES ('13', '3', '4', '99');
INSERT INTO `score` VALUES ('14', '4', '1', '79');
INSERT INTO `score` VALUES ('15', '4', '2', '11');
INSERT INTO `score` VALUES ('16', '4', '3', '67');
INSERT INTO `score` VALUES ('17', '4', '4', '100');
INSERT INTO `score` VALUES ('18', '5', '1', '79');
INSERT INTO `score` VALUES ('19', '5', '2', '11');
INSERT INTO `score` VALUES ('20', '5', '3', '67');
INSERT INTO `score` VALUES ('21', '5', '4', '100');
INSERT INTO `score` VALUES ('22', '6', '1', '9');
INSERT INTO `score` VALUES ('23', '6', '2', '100');
INSERT INTO `score` VALUES ('24', '6', '3', '67');
INSERT INTO `score` VALUES ('25', '6', '4', '100');
INSERT INTO `score` VALUES ('26', '7', '1', '9');
INSERT INTO `score` VALUES ('27', '7', '2', '100');
INSERT INTO `score` VALUES ('28', '7', '3', '67');
INSERT INTO `score` VALUES ('29', '7', '4', '88');
INSERT INTO `score` VALUES ('30', '8', '1', '9');
INSERT INTO `score` VALUES ('31', '8', '2', '100');
INSERT INTO `score` VALUES ('32', '8', '3', '67');
INSERT INTO `score` VALUES ('33', '8', '4', '88');
INSERT INTO `score` VALUES ('34', '9', '1', '91');
INSERT INTO `score` VALUES ('35', '9', '2', '88');
INSERT INTO `score` VALUES ('36', '9', '3', '67');
INSERT INTO `score` VALUES ('37', '9', '4', '22');
INSERT INTO `score` VALUES ('38', '10', '1', '90');
INSERT INTO `score` VALUES ('39', '10', '2', '77');
INSERT INTO `score` VALUES ('40', '10', '3', '43');
INSERT INTO `score` VALUES ('41', '10', '4', '87');
INSERT INTO `score` VALUES ('42', '11', '1', '90');
INSERT INTO `score` VALUES ('43', '11', '2', '77');
INSERT INTO `score` VALUES ('44', '11', '3', '43');
INSERT INTO `score` VALUES ('45', '11', '4', '87');
INSERT INTO `score` VALUES ('46', '12', '1', '90');
INSERT INTO `score` VALUES ('47', '12', '2', '77');
INSERT INTO `score` VALUES ('48', '12', '3', '43');
INSERT INTO `score` VALUES ('49', '12', '4', '87');
INSERT INTO `score` VALUES ('52', '13', '3', '87');

-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `gender` char(1) NOT NULL,
  `class_id` int(11) NOT NULL,
  `sname` varchar(32) NOT NULL,
  PRIMARY KEY (`sid`),
  KEY `fk_class` (`class_id`),
  CONSTRAINT `fk_class` FOREIGN KEY (`class_id`) REFERENCES `class` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', '男', '1', '理解');
INSERT INTO `student` VALUES ('2', '女', '1', '钢蛋');
INSERT INTO `student` VALUES ('3', '男', '1', '张三');
INSERT INTO `student` VALUES ('4', '男', '1', '张一');
INSERT INTO `student` VALUES ('5', '女', '1', '张二');
INSERT INTO `student` VALUES ('6', '男', '1', '张四');
INSERT INTO `student` VALUES ('7', '女', '2', '铁锤');
INSERT INTO `student` VALUES ('8', '男', '2', '李三');
INSERT INTO `student` VALUES ('9', '男', '2', '李一');
INSERT INTO `student` VALUES ('10', '女', '2', '李二');
INSERT INTO `student` VALUES ('11', '男', '2', '李四');
INSERT INTO `student` VALUES ('12', '女', '3', '如花');
INSERT INTO `student` VALUES ('13', '男', '3', '刘三');
INSERT INTO `student` VALUES ('14', '男', '3', '刘一');
INSERT INTO `student` VALUES ('15', '女', '3', '刘二');
INSERT INTO `student` VALUES ('16', '男', '3', '刘四');

-- ----------------------------
-- Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(32) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1', '张磊老师');
INSERT INTO `teacher` VALUES ('2', '李平老师');
INSERT INTO `teacher` VALUES ('3', '刘海燕老师');
INSERT INTO `teacher` VALUES ('4', '朱云海老师');
INSERT INTO `teacher` VALUES ('5', '李杰老师');
