
package com.example.app.schema;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.Builder;

/**
 * 登录响应DTO
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class LoginResponse {

    /**
     * 是否登录成功
     */
    private boolean success;

    /**
     * 提示信息
     */
    private String message;

    /**
     * 用户ID
     */
    private Long id;

    /**
     * 用户名
     */
    private String username;

    /**
     * 真实姓名
     */
    private String realName;

    /**
     * 用户类型（STUDENT/EMPLOYEE）
     */
    private String userType;

    /**
     * 员工角色
     */
    private String employeeRole;

    /**
     * 所属部门/院系
     */
    private String department;

    /**
     * 创建成功响应
     */
    public static LoginResponse success(com.example.app.model.SysUser user) {
        return LoginResponse.builder()
                .success(true)
                .message("登录成功")
                .id(user.getId())
                .username(user.getUsername())
                .realName(user.getRealName())
                .userType(user.getUserType())
                .employeeRole(user.getEmployeeRole())
                .department(user.getDepartment())
                .build();
    }

    /**
     * 创建失败响应
     */
    public static LoginResponse failure(String message) {
        return LoginResponse.builder()
                .success(false)
                .message(message)
                .build();
    }
}
