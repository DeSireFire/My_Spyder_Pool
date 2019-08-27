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

def uploader_creatSession(client):
    '''创建上传会话
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
    if remotePath == "None":
        remotePath = "/"
    url = app_url + '/v1.0/me/drive/root:/{}/{}:/createUploadSession'.format(remotePath,fileName)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"]), 'Content-Type': 'application/json'}
    data = {
        "item": {
            "@microsoft.graph.conflictBehavior": "fail",
        }
    }
    pull_res = requests.post(url, headers=headers, data=json.dumps(data))
    pull_res = json.loads(pull_res.text)
    if pull_res.status_code == 409:
        return False
    else:
        return pull_res


def uploaderBig(client,upUrl):
    '''大文件上传
    :return:
    '''
    # 创建上传会话,获取上传URL
    # sessionInfo = uploader_creatSession(client)
    # print(sessionInfo)

    # 读取需要上传的文件（部分）
    import os
    flen = os.path.getsize('test.txt')
    print(flen)
    with open('test.txt', 'rb') as f:
        f.seek(100)   # 标记从第几个字节 之后 开始读取
        content = f.read()    # 从标记往后读多少字节
        print(content)

    # 上传
    headers = {
        'Content-Type': 'application/octet-stream',
        'Content-Length': str(180),
        'Content-Range': 'bytes {setPoint}-{endPoint}/{fullLen}'.format(setPoint=100,endPoint=279,fullLen=flen)    # 下一次上传，endPoint等于setPoint+新读取的片段长度-1
    }
    # {'expirationDateTime': '2019-09-03T06:47:03.857Z', 'nextExpectedRanges': ['60-279']}

    # 上传完成时
    # {'createdBy': {'application': {'displayName': 'AlienVan', 'id': '402aba1b'}, 'user': {'id': 'a292b424bbe0c719'}}, 'createdDateTime': '2019-08-27T11:06:21.2Z', 'cTag': 'aYzpBMjkyQjQyNEJCRTBDNzE5ITE2My4yNTc', 'eTag': 'aQTI5MkI0MjRCQkUwQzcxOSExNjMuMA', 'id': 'A292B424BBE0C719!163', 'lastModifiedBy': {'application': {'displayName': 'AlienVan', 'id': '402aba1b'}, 'user': {'id': 'a292b424bbe0c719'}}, 'lastModifiedDateTime': '2019-08-27T11:06:21.2Z', 'name': 'test.txt', 'parentReference': {'driveId': 'a292b424bbe0c719', 'driveType': 'personal', 'id': 'A292B424BBE0C719!154', 'name': '233', 'path': '/drive/root:/233'}, 'size': 280, 'webUrl': 'https://1drv.ms/t/s!ABnH4LsktJKigSM', 'items': [], 'file': {'hashes': {'quickXorHash': '4JlP/bnmCdIHBKyuoz6ZBTOta4A=', 'sha1Hash': '415FB8E95F365087303BE329F9578D18362CC8DE'}, 'mimeType': 'text/plain'}, 'fileSystemInfo': {'createdDateTime': '2019-08-27T11:06:21.2Z', 'lastModifiedDateTime': '2019-08-27T11:06:21.2Z'}, 'shared': {'owner': {'custom': {}, 'user': {'id': 'a292b424bbe0c719'}}, 'scope': 'users'}, 'tags': [], 'lenses': [], 'thumbnails': [{'id': '0', 'large': {'height': 800, 'url': 'https://wurinw.bn.files.1drv.com/y4pFSNeOfNzUVnLhd0QsizexjihHHhL0MHhebdLpfm0iM0iN_n4HRYRxbxh8qhhnySVictPnb4JUcKCd0WVQYRXMIy0IKzqxft6sIPJ5mR_L_Vm812VXUhG16PqP-ZzwyID917b9o_ZxRW_VKPIGFafyD7F4S9iUNJc57XtfUMLb-I?width=800&height=800&cropmode=none', 'width': 800}, 'medium': {'height': 176, 'url': 'https://wurinw.bn.files.1drv.com/y4pFSNeOfNzUVnLhd0QsizexjihHHhL0MHhebdLpfm0iM0iN_n4HRYRxbxh8qhhnySVictPnb4JUcKCd0WVQYRXMIy0IKzqxft6sIPJ5mR_L_Vm812VXUhG16PqP-ZzwyID917b9o_ZxRW_VKPIGFafyD7F4S9iUNJc57XtfUMLb-I?width=176&height=176&cropmode=none', 'width': 176}, 'small': {'height': 96, 'url': 'https://wurinw.bn.files.1drv.com/y4pFSNeOfNzUVnLhd0QsizexjihHHhL0MHhebdLpfm0iM0iN_n4HRYRxbxh8qhhnySVictPnb4JUcKCd0WVQYRXMIy0IKzqxft6sIPJ5mR_L_Vm812VXUhG16PqP-ZzwyID917b9o_ZxRW_VKPIGFafyD7F4S9iUNJc57XtfUMLb-I?width=96&height=96&cropmode=none', 'width': 96}}]}

    # pull_res = requests.put(sessionInfo['uploadUrl'], headers=headers, data=content)
    pull_res = requests.put(upUrl, headers=headers, data=content)
    pull_res = json.loads(pull_res.text)
    print(pull_res)

def delup(client,upURL):
    '''
    DELETE https://sn3302.up.1drv.com/up/fe6987415ace7X4e1eF866337
    :param client:
    :return:
    '''
    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    del_res = requests.post(upURL, headers=headers)
    print(del_res)


if __name__ == '__main__':
    temp = flush_token(info["refresh_token"])
    # # pull_res = uploader_creatSession(temp)
    # pull_res = {'@odata.context': 'https://graph.microsoft.com/v1.0/$metadata#microsoft.graph.uploadSession', 'expirationDateTime': '2019-09-03T06:47:03.857Z', 'nextExpectedRanges': ['0-'], 'uploadUrl': 'https://api.onedrive.com/rup/a292b424bbe0c719/eyJSZXNvdXJjZUlEIjoiQTI5MkI0MjRCQkUwQzcxOSExNTQiLCJSZWxhdGlvbnNoaXBOYW1lIjoidGVzdC50eHQifQ/4mJpullRYS6xp0jTI7r69qC7SMOmzNZYXafZt5SP75IaLOAfkeNWxXHNQqQpC1JkzbnsBahzUolymU5f8W8muz_5MogIeVwp3XxO65qNAHuCw/eyJuYW1lIjoidGVzdC50eHQiLCJAbmFtZS5jb25mbGljdEJlaGF2aW9yIjoiZmFpbCJ9/4wfbKrWZRCD82qjclyFHcm-0qE0PMeUQxaG0MVKY6x_iEcZARPnn3dehcg73SXEMO3m9_eLCvW-4TC90B2cEpUdHI_X6emHkPgfcCPvlBco7rUCvmR5C8b5DtQ3oqL_VfYRbPGK1hevstVDpQYb9YtCfbZhB5P8GHy5JTTAVoBRJ-MGjvvO9F309eUj8JFuxeADxlMkCUFuCkIC-sZKDJwS7W0j3LPODMIw5GkBSDl9NqN8gnnkEVbW-wT0zzsceOrTItZocqfTX4GFemezWx1Tvrnn2CNcx9rkHEZVW3CtTm2FGpu24e2cWk9vgU4DWRySrN6pgz069bOc1zvkCSAA8ebQdM7Vl72psH2CAhUBgC-PtiLQt8DTZcRH0x8v5fWtrpn_YWN86R1tduKtYs81C5RJMNcMJ0DyePuiE_U49iidnr03oDp9jzX2JvM5PDFAbJzhPDAE7aXf254rBRiblh3rgB13uD4PfgvCGBF57U166GGk5FP3zhNMDeh0rsuAiJaS81HwfpM7EfK-7rWWWtFuCxlsY2CqnvXXQQTwUk'}
    # delup(temp, pull_res['uploadUrl'])

    uploaderBig(temp,'https://api.onedrive.com/rup/a292b424bbe0c719/eyJSZXNvdXJjZUlEIjoiQTI5MkI0MjRCQkUwQzcxOSExNTQiLCJSZWxhdGlvbnNoaXBOYW1lIjoidGVzdC50eHQifQ/4mJpullRYS6xp0jTI7r69qC7SMOmzNZYXafZt5SP75IaLOAfkeNWxXHNQqQpC1JkzbnsBahzUolymU5f8W8muz_5MogIeVwp3XxO65qNAHuCw/eyJuYW1lIjoidGVzdC50eHQiLCJAbmFtZS5jb25mbGljdEJlaGF2aW9yIjoiZmFpbCJ9/4wfbKrWZRCD82qjclyFHcm-0qE0PMeUQxaG0MVKY6x_iEcZARPnn3dehcg73SXEMO3m9_eLCvW-4TC90B2cEpUdHI_X6emHkPgfcCPvlBco7rUCvmR5C8b5DtQ3oqL_VfYRbPGK1hevstVDpQYb9YtCfbZhB5P8GHy5JTTAVoBRJ-MGjvvO9F309eUj8JFuxeADxlMkCUFuCkIC-sZKDJwS7W0j3LPODMIw5GkBSDl9NqN8gnnkEVbW-wT0zzsceOrTItZocqfTX4GFemezWx1Tvrnn2CNcx9rkHEZVW3CtTm2FGpu24e2cWk9vgU4DWRySrN6pgz069bOc1zvkCSAA8ebQdM7Vl72psH2CAhUBgC-PtiLQt8DTZcRH0x8v5fWtrpn_YWN86R1tduKtYs81C5RJMNcMJ0DyePuiE_U49iidnr03oDp9jzX2JvM5PDFAbJzhPDAE7aXf254rBRiblh3rgB13uD4PfgvCGBF57U166GGk5FP3zhNMDeh0rsuAiJaS81HwfpM7EfK-7rWWWtFuCxlsY2CqnvXXQQTwUk')