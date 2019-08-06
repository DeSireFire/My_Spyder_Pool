from requests_oauthlib import OAuth2Session
import requests,json
from onedrive.authDemo import flush_token,oauthDict
from onedrive.sec import *

# def uploader():
#     headers = {
#         'Authorization': 'bearer %s'%info['refresh_token']
#     }
#     data = {
#         "name": "New Folder",
#         "folder": {},
#         "@microsoft.graph.conflictBehavior": "rename"
#     }
#     req = requests.post('https://api.onedrive.com/v1.0/me/drive/root/children',json=data,headers = headers)
#     # req = requests.post('https://graph.microsoft.com/v1.0/me/drive/root/children',json=data,headers = headers)
#     # req = requests.put('/me/drive/root:/FolderA/FileB.txt:/content',data=data)
#     print(json.loads(req.text))
#     print(type(json.loads(req.text)))
#     return json.loads(req.text)

def od_filesList():
    data = {
        'Authorization':'Bearer %s'%info['refresh_token'],
        # 'Content - Type':'application / json',
        # 'client_id':oauthDict['app_id'],
        # 'redirect_uri':oauthDict['redirect'],
        # 'client_secret':oauthDict['app_secret'],
        # 'refresh_token':info['refresh_token'],
        # 'grant_type':'refresh_token',
    }
    temp = flush_token(info['refresh_token'])
    print(temp)
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(temp['access_token'])}
    req = requests.get('https://graph.microsoft.com/v1.0/me/drive', headers = data)
    # req = requests.get('https://api.onedrive.com/v1.0/drive/root/children', headers = data)
    print(req.text)

if __name__ == '__main__':

    od_filesList()