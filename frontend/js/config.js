// Dify智能体配置
const AGENT_CONFIG = {
    // 客服智能体
    customer: {
        appId: 'G3Tsuspuu40ayj52',
        baseUrl: 'http://localhost',
        name: '客服智能体',
        title: '在线客服'
    },
    // 企业智能体
    employee: {
        appId: 'KOleENYxpzWkTSAX',
        baseUrl: 'http://localhost',
        name: '企业智能体',
        title: '企业助手'
    },
    // 学生智能体
    student: {
        appId: '1CWhaJpQNXAOijuA',
        baseUrl: 'http://localhost',
        name: '学生智能体',
        title: '学生助手'
    }
};

// 后端API地址
const API_BASE_URL = '/api/v1';

// 存储用户信息的key
const USER_INFO_KEY = 'dify_user_info';