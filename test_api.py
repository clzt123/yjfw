import sys
import json
import urllib.request
import urllib.error

url = 'http://localhost:8080/api/user/login'
data = json.dumps({'username': '20230001', 'password': '123456'}).encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')
req.add_header('Content-Type', 'application/json')

try:
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    print("SUCCESS: API call worked!")
    print("Response:", result)
except urllib.error.HTTPError as e:
    print("ERROR: HTTP Error", e.code, "-", e.reason)
    print("Response:", e.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("ERROR: Network Error", e.reason)
except Exception as e:
    print("ERROR: Unexpected error:", type(e).__name__, "-", str(e))