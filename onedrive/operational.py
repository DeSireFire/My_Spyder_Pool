from requests_oauthlib import OAuth2Session
import requests,json
from onedrive.authDemo import flush_token,oauthDict
from onedrive.sec import *

def updater(client,fileid):
    '''更新上传已有项目
    PUT /me/drive/items/{item-id}/content
    '''
    fileName = 'test.txt'
    url = app_url + '/v1.0/me/drive/items/{}/content'.format(fileid)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    pull_res = requests.put(url, headers=headers, data=open(fileName, 'rb'))
    pull_res = json.loads(pull_res.text)
    print(pull_res)

def uploader(client):
    '''上传新项目
    PUT /me/drive/items/{parent-id}:/{filename}:/content

    PUT /me/drive/root:/FolderA/FileB.txt:/content??
    两者都可以


    坑逼微软api，你奶奶的,↓根本不用写好不
    Content-Type: text/plain

    '''
    fileName = 'test.txt'
    url = app_url + '/v1.0/me/drive/items/root:/{}:/content'.format(fileName)
    print(url)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    pull_res = requests.put(url, headers=headers, data=open(fileName, 'rb'))
    pull_res = json.loads(pull_res.text)
    print(pull_res)

def uploaderBig(client):
    '''大文件上传
    POST /drives/{driveId}/items/{itemId}/createUploadSession
    POST /groups/{groupId}/drive/items/{itemId}/createUploadSession
    POST /me/drive/items/{itemId}/createUploadSession
    POST /sites/{siteId}/drive/items/{itemId}/createUploadSession
    POST /users/{userId}/drive/items/{itemId}/createUploadSession

    /drive/root:/{item-path}:/createUploadSession

    :param client:
    :return:
    '''
    fileName = 'test.txt'
    remotePath = '233'
    uid = 'a292b424bbe0c719'
    # 创建上传会话
    if remotePath == "None":
        remotePath = "/"
    url = app_url + '/v1.0/me/drive/root:/{}/{}/{}:/createUploadSession'.format(uid, remotePath,fileName)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"]), 'Content-Type': 'application/json'}
    data = {
        "item": {
            "@microsoft.graph.conflictBehavior": "fail",
        }
    }
    try:
        pull_res = requests.post(url, headers=headers, data=json.dumps(data))
        pull_res = json.loads(pull_res.text)
        if pull_res.status_code == 409:
            return False
        else:
            pull_res = json.loads(pull_res.text)
    except Exception as e:
        return False

def delup(client):
    '''
    DELETE https://sn3302.up.1drv.com/up/fe6987415ace7X4e1eF866337
    :param client:
    :return:
    '''
    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    del_res = requests.post("https://api.onedrive.com/rup/a292b424bbe0c719/eyJSZXNvdXJjZUlEIjoiQTI5MkI0MjRCQkUwQzcxOSExNjIiLCJSZWxhdGlvbnNoaXBOYW1lIjoidGVzdC50eHQifQ/4mfWNtlIYcsH5tRynvwD26B4LY-M2LGGTonII1w3-YLi6pJwRBLVGm6rF-4Lesn85LICeNn1gDCeNAbGoeytMDc3HZuJDatildNQSv6xmYajA/eyJuYW1lIjoidGVzdC50eHQiLCJAbmFtZS5jb25mbGljdEJlaGF2aW9yIjoiZmFpbCJ9/4wxqZqVdo5CgW_EadQ9Fxwl6lvtNCoBuyAjOAwyH1QL9d0plFf1I0DvKTLrHI7vEdaue6MsZBHIC_wnvPi3PG8lVUAOBv9TEhyOY7k7I4mA8J03bQemjQ03C_-j2K07rYkqXWXGOh79UndmTNiwxzqzdW70hmpLVPd4b74LcYdF-6bXIQYytxSrViiiUq3YohVx5PxYYSfBPxBsoqa-GWjKtf7y0DBR-3LlaS2tqBF6T1aXNIndcU35b_blGyBZtm9vXtXivEAMme8Mc6ydtfAjIcb-_bt8pGIQ3u3p66g3rl4lKVHPhvlSvIC0CASjH_GI0igOCwTZ77nsNz8xD1UszlKN8FiKwdvvOVc820zvf9c7UtTrfzUysYlEKfOCvpMDtpGhRMjzgFH5vnCSemIdnz5Qw6zIZcPUH-AR2Q-jg4_BoTNpTBF72Hvy_uN8Oj2rgGiCK31gKJyMl-v2IQ4cQX292Gq8vlr5dycYjZgGfQ_I18K71rUXRdeyYIrKo6NfSLMs2pnl_FGogmmjD51d-Gr70H4GOCvDWuWCHoGeEw'}", headers=headers)
    print(del_res)

def od_thumbnails(client,itemid,path=''):
    '''
    获取缩略图
    凡是文件都可以获得缩略图，但只有图片的缩略图可以用
    :param client:
    :param itemid:文件带有的id
    :return:
    '''
    app_url = "https://graph.microsoft.com"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(client["access_token"])}
    get_res = requests.get(app_url+'/items/{item_id}/thumbnails/{thumb_id}/{size}'.format(item_id=itemid,thumb_id='0',size='large'), headers=headers, timeout=30)
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

    # flist = od_filesList(temp,1,os.path.join('wori','wori 1').replace("\\",'/'))
    # flist = od_filesList(temp,1,'')

    # folder_create(1,'','wori')

    # rename_files(temp,flist['value'][1]['id'],'rename2')

    # delete_files(temp,flist['value'][1]['id'])
    # for i in flist['value']:
    #     od_thumbnails(temp,i['id'],'')

    # uploader(temp)
    # updater(temp,'A292B424BBE0C719!155')
    # uploaderBig(temp,)
    delup(temp)
