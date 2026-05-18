
package com.example.app.service.impl;

import com.example.app.dao.SysUserRepository;
import com.example.app.model.SysUser;
import com.example.app.schema.LoginResponse;
import com.example.app.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

/**
 * 用户服务实现类
 */
@Slf4j
@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final SysUserRepository sysUserRepository;

    @Override
    public LoginResponse login(String username, String password) {
        log.info("用户登录请求: username={}", username);
        
        // 根据用户名查询用户
        var userOptional = sysUserRepository.findByUsername(username);
        
        if (userOptional.isEmpty()) {
            log.warn("用户不存在: username={}", username);
            return LoginResponse.failure("用户名或密码错误");
        }
        
        SysUser user = userOptional.get();
        
        // 检查账号状态
        if (!"正常".equals(user.getStatus())) {
            log.warn("账号状态异常: username={}, status={}", username, user.getStatus());
            return LoginResponse.failure("账号状态异常，请联系管理员");
        }
        
        // 验证密码（实际项目中应使用加密密码验证）
        if (!password.equals(user.getPassword())) {
            log.warn("密码错误: username={}", username);
            return LoginResponse.failure("用户名或密码错误");
        }
        
        log.info("用户登录成功: username={}, userType={}", username, user.getUserType());
        return LoginResponse.success(user);
    }
}
