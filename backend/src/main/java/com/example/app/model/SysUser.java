
package com.example.app.model;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.time.LocalDateTime;

/**
 * 统一用户表实体类
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "sys_user", indexes = {
    @Index(name = "idx_username", columnList = "username", unique = true)
})
public class SysUser {

    /**
     * 主键ID
     */
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    /**
     * 用户名/登录账号
     */
    @Column(name = "username", nullable = false, length = 64)
    private String username;

    /**
     * 密码
     */
    @Column(name = "password", nullable = false, length = 255)
    private String password;

    /**
     * 真实姓名
     */
    @Column(name = "real_name", nullable = false, length = 64)
    private String realName;

    /**
     * 用户大类（STUDENT 学生 / EMPLOYEE 员工）
     */
    @Column(name = "user_type", nullable = false, length = 32)
    private String userType;

    /**
     * 员工角色
     */
    @Column(name = "employee_role", length = 64)
    private String employeeRole;

    /**
     * 所属部门/院系
     */
    @Column(name = "department", length = 128)
    private String department;

    /**
     * 联系方式
     */
    @Column(name = "contact_info", length = 64)
    private String contactInfo;

    /**
     * 账号状态
     */
    @Column(name = "status", length = 16)
    private String status = "正常";

    /**
     * 创建时间
     */
    @Column(name = "create_time")
    private LocalDateTime createTime;

    /**
     * 更新时间
     */
    @Column(name = "update_time")
    private LocalDateTime updateTime;

    @PrePersist
    protected void onCreate() {
        createTime = LocalDateTime.now();
        updateTime = LocalDateTime.now();
    }

    @PreUpdate
    protected void onUpdate() {
        updateTime = LocalDateTime.now();
    }
}
