
package com.example.app.service;

import com.example.app.schema.LoginResponse;

/**
 * 用户服务接口
 */
public interface UserService {

    /**
     * 用户登录
     * @param username 用户名
     * @param password 密码
     * @return 登录响应
     */
    LoginResponse login(String username, String password);
}
