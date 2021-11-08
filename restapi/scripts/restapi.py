import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list(id=None): #--> Lists all this out
    data = json.dumps({})
    print(type(data))
    if id is not None:
        data = json.dumps({"id": id})
        #print(data)
    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200: # not found
        print('probably not good sign?')
    data = r.json()
    return data

def create_update():
    new_data= {
        'user': 1,
        'content': 'conten1',
        'id' : 10
    }

    r = requests.post("http://127.0.0.1:8000/api/updates/", data=new_data )
    print('script')
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()

    return r.text


def do_obj_update():
    new_data = {
        "content": "awesomer"  
    }
    r = requests.put(BASE_URL + ENDPOINT + "1/", data=json.dumps(new_data))
    # new_data = {
    #     'id': 1
    #     "content": "Another more cool content"  
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)
    #print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        #print(r.json())
        return r.json()
    return r.text

# print(get_list(5))
# print(create_update())
print(do_obj_update())