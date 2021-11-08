import requests
import json
ENDPOINT = 'http://127.0.0.1:8000/api/status/'

AWT_ENDPOINT = 'http://127.0.0.1:8000/api/auth/jwt/'
headers = {
    "Content-Type": "application/json",
}

data = {'username':'admin',
        'password': 'admin'
        }
# r1 = requests.post(AWT_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r1.json()['token']
# print(token)

data1 = {
        'content' : 'content by script'
}
headers = {
        "Content-Type": "application/json",
        "Authorization" : "JWT" + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjM1ODYxMTk0LCJlbWFpbCI6IiJ9.cHXtj__Bq1Cy0rwzLU1prhj00vpsfBPYN5pXCPyUDLE'
}

post_data = json.dumps({"content": "data added by script "})
r2 = requests.post(ENDPOINT, data=post_data, headers=headers)
print(r2.text)

# headers = {
#         "Content-Type": "application/json",
#         "Authorization" : "JWT " + token
# }

# data1 = {
#         'content' : 'patch data by script'
# }
# json_data = json.dumps(data1)
# r3 = requests.put(ENDPOINT + str(10) + '/', data=json_data , headers=headers )
# print(r3.text)
