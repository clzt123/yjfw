
-- 统一用户表
CREATE TABLE IF NOT EXISTS `sys_user` (
    `id` BIGINT NOT NULL AUTO_INCREMENT COMMENT '主键ID',
    `username` VARCHAR(64) NOT NULL COMMENT '用户名/登录账号',
    `password` VARCHAR(255) NOT NULL COMMENT '密码',
    `real_name` VARCHAR(64) NOT NULL COMMENT '真实姓名',
    `user_type` VARCHAR(32) NOT NULL COMMENT '用户大类（STUDENT 学生 / EMPLOYEE 员工）',
    `employee_role` VARCHAR(64) DEFAULT NULL COMMENT '员工角色',
    `department` VARCHAR(128) DEFAULT NULL COMMENT '所属部门/院系',
    `contact_info` VARCHAR(64) DEFAULT NULL COMMENT '联系方式',
    `status` VARCHAR(16) DEFAULT '正常' COMMENT '账号状态',
    `create_time` DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='统一用户表';

-- 插入测试数据
INSERT INTO `sys_user` (`username`, `password`, `real_name`, `user_type`, `employee_role`, `department`, `contact_info`) VALUES
('admin', '123456', '管理员', 'EMPLOYEE', '管理员', '信息中心', '13800138000'),
('teacher001', '123456', '张老师', 'EMPLOYEE', '教师', '计算机学院', '13800138001'),
('student001', '123456', '李明', 'STUDENT', NULL, '计算机学院', '13800138002'),
('student002', '123456', '王芳', 'STUDENT', NULL, '电子工程学院', '13800138003');
