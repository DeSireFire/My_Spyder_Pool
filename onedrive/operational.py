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

def od_thumbnails(client,path=''):
    '''
    获取缩略图
    :param client:
    :param path:
    :return:
    '''
    app_url = "https://graph.microsoft.com"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(client["access_token"])}
    app_url = app_url+"/v1.0/me/drive"
    if path:
        BaseUrl = app_url + '/root:/{}:/children'.format(path)
    else:
        BaseUrl = app_url + '/root/children'

    get_res = requests.get(app_url+'/items/{item_id}/thumbnails/{thumb_id}/{size}'.format(item_id='A292B424BBE0C719!122',thumb_id='0',size='large'), headers=headers, timeout=30)
    get_res = json.loads(get_res.text)
    print(get_res)


def od_filesList(client,od_type,path=''):
    '''
    文件列表查询
    :param od_type: 布尔，onedrive 类型
    :param path: 字符串，目标目录名
    :return:
    '''
    app_url = "https://graph.microsoft.com"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(client["access_token"])}
    if od_type:
        app_url = app_url+"/v1.0/me/drive"
    # else:
    #     app_url = "https://{}-my.sharepoint.cn/_api/v2.0/me/drive".format(data_list.other)
    if path:
        BaseUrl = app_url + '/root:/{}:/children?expand=thumbnails'.format(path)
    else:
        BaseUrl = app_url + '/root/children?expand=thumbnails'
    print(BaseUrl)
    get_res = requests.get(BaseUrl, headers=headers, timeout=30)
    get_res = json.loads(get_res.text)
    print(get_res)
    for i in get_res:
        print('%s:%s'%(i,get_res[i]))
        if i == 'value':
            for n in get_res[i]:
                print(n)
    return get_res


def folder_create(client, path, fileName):
    if path:
        # parent_id = models.mongodb_find_parent_id(id, path)
        parent_id = 'root'
        url = app_url + '/v1.0/me/drive/items/{}/children'.format(parent_id)
    else:
        url = app_url + '/v1.0/me/drive/root/children'

    # temp = flush_token(info["refresh_token"])

    headers = {'Authorization': 'bearer {}'.format(client["access_token"]), 'Content-Type': 'application/json'}
    payload = {
        "name": fileName,
        "folder": {},
        "@microsoft.graph.conflictBehavior": "rename"
    }
    get_res = requests.post(url, headers=headers, data=json.dumps(payload))
    get_res = json.loads(get_res.text)
    print(get_res)
    for i in get_res:
        print('%s:%s'%(i,get_res[i]))
        if i == 'value':
            for n in get_res[i]:
                print(n)
    return get_res
    # if 'error' in get_res.keys():
    #     flush_token(info["refresh_token"])
    #     return folder_create(id, path, fileName)
    # else:
    #     return {'code': True, 'msg': '成功', 'data':''}

def rename_files(client, fileid, new_name):
    '''
    重命名文件/目录
    :param client:字典
    :param new_name:
    :return:
    '''
    url = app_url + '/v1.0/me/drive/items/{}'.format(fileid)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"]), 'Content-Type': 'application/json'}
    payload = {
        "name": new_name
    }
    get_res = requests.patch(url, headers=headers, data=json.dumps(payload))
    get_res = json.loads(get_res.text)
    print(get_res)
    # if 'error' in get_res.keys():
    #     temp = flush_token(info["refresh_token"])
    #     return rename_files(temp, fileid, new_name)
    # else:
    #     return {'code': True, 'msg': '成功', 'data':''}

def delete_files(client, fileid):
    url = app_url + '/v1.0/me/drive/items/{}'.format(fileid)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"]), 'Content-Type': 'application/json'}
    get_res = requests.delete(url, headers=headers)
    print(get_res)
    # if get_res.status_code == 204:
    #     return {'code': True, 'msg': '成功', 'data':''}
    # else:
    #     common.reacquireToken(id)
    #     return delete_files(id, fileid)

if __name__ == '__main__':
    # pass
    import os
    # print(os.path.join('wori','wori 1').replace("\\",'/'))
    temp = flush_token(info["refresh_token"])
    #
    # flist = od_filesList(temp,1,os.path.join('wori','wori 1').replace("\\",'/'))
    flist = od_filesList(temp,1,'')

    # folder_create(1,'','wori')

    # rename_files(temp,flist['value'][1]['id'],'rename2')

    # delete_files(temp,flist['value'][1]['id'])

    od_thumbnails(temp,'TIM图片20190728215728.jpg')