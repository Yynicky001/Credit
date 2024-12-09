/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : competition1

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 19/11/2024 16:30:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for credit_score_rule
-- ----------------------------
DROP TABLE IF EXISTS `credit_score_rule`;
CREATE TABLE `credit_score_rule`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '评估者姓名',
  `credit_history` smallint NULL DEFAULT NULL,
  `credit_card_utilization_rate` smallint NULL DEFAULT NULL,
  `number_of_overdue_payments` smallint NULL DEFAULT NULL,
  `debt-to-income_ratio` smallint NULL DEFAULT NULL,
  `asset-liability_situation` smallint NULL DEFAULT NULL,
  `credit_account_quantity` smallint NULL DEFAULT NULL,
  `income_stability` smallint NULL DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '信贷评分规则表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of credit_score_rule
-- ----------------------------
INSERT INTO `credit_score_rule` VALUES (11, '100001', 5, 1, 4, 1, 150, 2, 0, '2024-11-05 18:47:51');
INSERT INTO `credit_score_rule` VALUES (12, '100002', 3, 1, 4, 1, 50, 1, 100, '2024-11-05 13:50:51');
INSERT INTO `credit_score_rule` VALUES (13, '100003', 7, 1, 4, 0, 150, 1, 0, '2024-11-05 13:50:51');
INSERT INTO `credit_score_rule` VALUES (14, '100004', 12, 1, 4, 0, 150, 4, 0, '2024-11-05 13:50:51');
INSERT INTO `credit_score_rule` VALUES (15, '100005', 9, 1, 4, 0, 100, 2, 100, '2024-11-05 13:50:51');
INSERT INTO `credit_score_rule` VALUES (16, '100006', 1, 1, 4, 1, 100, 2, 100, '2024-11-05 13:50:51');
INSERT INTO `credit_score_rule` VALUES (17, '100007', 3, 1, 4, 1, 100, 2, 0, '2024-11-05 13:50:51');
INSERT INTO `credit_score_rule` VALUES (18, '100008', 5, 1, 4, 1, 50, 2, 100, '2024-11-05 13:50:51');

-- ----------------------------
-- Table structure for loan_user
-- ----------------------------
DROP TABLE IF EXISTS `loan_user`;
CREATE TABLE `loan_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户名',
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '密码',
  `nickname` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '昵称',
  `credit_score` int NULL DEFAULT NULL,
  `remark` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `age` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of loan_user
-- ----------------------------
INSERT INTO `loan_user` VALUES (1, 'admin', 'admin', 'VIP用户', 2389, '', '2021-03-12 13:50:51', '3136757823@qq.com', '31');
INSERT INTO `loan_user` VALUES (2, 'fs', 'fs123', '普通用户', 2324, NULL, '2021-03-12 13:56:23', '1733504786@qq.com', '27');

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户名',
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '密码',
  `nickname` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '昵称',
  `credit_score` int NULL DEFAULT NULL,
  `remark` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `age` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES (1, 'admin', 'admin', '管理员', 2389, NULL, '2021-03-12 13:50:51', '3136757823@qq.com', '31');
INSERT INTO `sys_user` VALUES (2, 'fs', 'fs123', '普通用户', 2324, NULL, '2021-03-12 13:56:23', '1733504786@qq.com', '27');

SET FOREIGN_KEY_CHECKS = 1;
