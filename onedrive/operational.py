from requests_oauthlib import OAuth2Session
import requests,json
# from .authDemo import flush_token
from onedrive.sec import *

def uploader():
    headers = {
        'Authorization': 'bearer %s'%info['refresh_token']
    }
    data = {
        "name": "New Folder",
        "folder": {},
        "@microsoft.graph.conflictBehavior": "rename"
    }
    req = requests.post('https://api.onedrive.com/v1.0/me/drive/root/children',json=data,headers = headers)
    # req = requests.post('https://graph.microsoft.com/v1.0/me/drive/root/children',json=data,headers = headers)
    # req = requests.put('/me/drive/root:/FolderA/FileB.txt:/content',data=data)
    print(json.loads(req.text))
    print(type(json.loads(req.text)))
    return json.loads(req.text)
