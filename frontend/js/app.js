
// 当前用户类型（用于登录后判断）
let currentLoginType = null;

// 页面元素引用
const menuPage = document.getElementById('menu-page');
const loginPage = document.getElementById('login-page');
const chatPage = document.getElementById('chat-page');
const chatTitle = document.getElementById('chat-title');
const agentType = document.getElementById('agent-type');
const chatIframe = document.getElementById('chat-iframe');
const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');
const loadingOverlay = document.getElementById('loading-overlay');

/**
 * 显示指定页面
 */
function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    document.getElementById(pageId).classList.add('active');
}

/**
 * 返回上一页
 */
function goBack() {
    // 清除iframe内容
    chatIframe.src = '';
    
    // 显示菜单页面
    showPage('menu-page');
    currentLoginType = null;
}

/**
 * 导航到聊天页面（通用方法）
 * @param {string} agentTypeStr - 智能体类型 (customer/employee/student)
 * @param {number} [studentId] - 用户数据库ID（学生/员工智能体需要，来自登录接口返回的id字段）
 */
function openChat(agentTypeStr, studentId = null) {
    const config = AGENT_CONFIG[agentTypeStr];
    if (!config) return;
    
    // 显示加载遮罩
    loadingOverlay.classList.add('show');
    
    // 设置聊天标题
    chatTitle.textContent = config.title;
    agentType.textContent = config.name;
    
    // 构造Dify WebApp URL（正确格式）
    // 格式: http://host/chat/{appId}
    let iframeUrl = `${config.baseUrl}/chat/${config.appId}`;
    
    // 通过sys.user_id传递登录用户数据库ID（Dify原生支持，学生和员工均需自动绑定）
    if ((agentTypeStr === 'student' || agentTypeStr === 'employee') && studentId) {
        iframeUrl += `?sys.user_id=${encodeURIComponent(studentId)}`;
    }
    
    // 设置iframe源
    chatIframe.src = iframeUrl;
    
    // 等待iframe加载
    chatIframe.onload = function() {
        loadingOverlay.classList.remove('show');
    };
    
    // 显示聊天页面
    showPage('chat-page');
}

/**
 * 导航到登录页面
 * @param {string} userType - 用户类型 (STUDENT/EMPLOYEE)
 */
function navigateToLogin(userType) {
    currentLoginType = userType;
    // 重置登录表单
    loginForm.reset();
    loginError.classList.remove('show');
    loginError.textContent = '';
    // 显示登录页面
    showPage('login-page');
}

/**
 * 处理登录请求
 * @param {Event} event - 表单提交事件
 */
async function handleLogin(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // 显示加载遮罩
    loadingOverlay.classList.add('show');
    loginError.classList.remove('show');
    
    try {
        const response = await fetch(`${API_BASE_URL}/user/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });
        
        const result = await response.json();
        
        if (result.success) {
            // 登录成功，获取用户类型
            const userType = result.user_type;
            
            // 验证入口类型和用户类型是否匹配
            if (currentLoginType === 'EMPLOYEE' && userType === 'EMPLOYEE') {
                // 员工入口 + 员工账号 = 正确，传递数据库ID
                openChat('employee', result.id);
            } else if (currentLoginType === 'STUDENT' && userType === 'STUDENT') {
                // 学生入口 + 学生账号 = 正确，传递数据库ID
                openChat('student', result.id);
            } else if (currentLoginType === 'EMPLOYEE' && userType === 'STUDENT') {
                // 员工入口 + 学生账号 = 错误
                loginError.textContent = '您使用的是学生账号，请从学生入口登录';
                loginError.classList.add('show');
                return;  // 阻止跳转
            } else if (currentLoginType === 'STUDENT' && userType === 'EMPLOYEE') {
                // 学生入口 + 员工账号 = 错误
                loginError.textContent = '您使用的是员工账号，请从员工入口登录';
                loginError.classList.add('show');
                return;  // 阻止跳转
            }
            
            // 保存用户信息到本地存储
            localStorage.setItem(USER_INFO_KEY, JSON.stringify(result));
        } else {
            // 登录失败，显示错误信息
            loginError.textContent = result.message;
            loginError.classList.add('show');
        }
    } catch (error) {
        console.error('登录请求失败:', error);
        loginError.textContent = '登录请求失败，请检查网络连接';
        loginError.classList.add('show');
    } finally {
        loadingOverlay.classList.remove('show');
    }
}

/**
 * 客服入口直接进入聊天（供HTML调用）
 */
function navigateToChat(type) {
    if (type === 'customer') {
        openChat('customer');
    }
}

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    // 确保显示菜单页面
    showPage('menu-page');
});

// 导出函数供HTML调用
window.navigateToChat = navigateToChat;
window.navigateToLogin = navigateToLogin;
window.goBack = goBack;
window.handleLogin = handleLogin;