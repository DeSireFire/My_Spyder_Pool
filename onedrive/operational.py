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

def od_filesList(od_type,path=''):
    '''
    文件列表查询
    :param od_type: 布尔，onedrive 类型
    :param path: 字符串，目标目录名
    :return:
    '''
    app_url = "https://graph.microsoft.com"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(info["access_token"])}
    if od_type:
        app_url = app_url+"/v1.0/me/drive"
    # else:
    #     app_url = "https://{}-my.sharepoint.cn/_api/v2.0/me/drive".format(data_list.other)
    if path:
        BaseUrl = app_url + '/root:{}:/children?expand=thumbnails'.format(path)
    else:
        BaseUrl = app_url + '/root/children?expand=thumbnails'

    get_res = requests.get(BaseUrl, headers=headers, timeout=30)
    get_res = json.loads(get_res.text)
    print(get_res)
    for i in get_res:
        print('%s:%s'%(i,get_res[i]))
        if i == 'value':
            for n in get_res[i]:
                print(n)



if __name__ == '__main__':
    od_filesList(1)