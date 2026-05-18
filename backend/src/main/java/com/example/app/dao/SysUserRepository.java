
package com.example.app.dao;

import com.example.app.model.SysUser;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

/**
 * 用户数据访问接口
 */
@Repository
public interface SysUserRepository extends JpaRepository<SysUser, Long> {

    /**
     * 根据用户名查询用户
     * @param username 用户名
     * @return 用户信息
     */
    Optional<SysUser> findByUsername(String username);

    /**
     * 根据用户名和状态查询用户
     * @param username 用户名
     * @param status 状态
     * @return 用户信息
     */
    Optional<SysUser> findByUsernameAndStatus(String username, String status);
}
