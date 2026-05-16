import requests

base_url = 'http://localhost:8001'

print('=== 测试 POST /api/leads/update/dify 接口 ===')

# 创建测试数据
create_response = requests.post(f'{base_url}/api/leads', json={
    'customer_name': 'Dify测试客户',
    'owner_employee_id': 1001
})
if create_response.status_code == 200:
    lead_id = create_response.json()['id']
    print(f'创建测试数据: ID={lead_id}')
    
    # 使用 Dify 接口更新
    dify_payload = {
        "sql": f'{{"id":{lead_id},"customer_name":"Dify测试客户(已修改)","status":"已联系"}}'
    }
    response = requests.post(f'{base_url}/api/leads/update/dify', json=dify_payload)
    print(f'\n调用 POST /api/leads/update/dify')
    print(f'请求体: {dify_payload}')
    print(f'状态码: {response.status_code}')
    print(f'响应: {response.json()}')
else:
    print(f'创建测试数据失败: {create_response.status_code}')

print('\n=== 测试完成 ===')