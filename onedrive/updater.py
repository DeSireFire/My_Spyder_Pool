import requests,json
from onedrive.authDemo import flush_token,oauthDict
from onedrive.sec import *

def main_uploader(client,filePath,remotePath='/',fileid=False):
    '''上传文件，总函数
    :param filePath:str,上传的目标文件在本地的完整路径
    :param remotePath:str,远程网盘要放的路径
    '''
    import os.path

    # 如果存在文件id,则使用文件更新已有项目
    if fileid:
        return updater(client, fileid,filePath)

    # 小于8MB用小文件上传
    if os.path.getsize(filePath) < 8388608:
        return small_uploader(client,os.path.basename(filePath),remotePath)
    else:   # 大于8mb用大文件上传
        return big_uploader(client,os.path.basename(filePath),remotePath)




def updater(client,fileid,filePath):
    '''更新上传已有项目
    PUT /me/drive/items/{item-id}/content
    '''
    url = app_url + '/v1.0/me/drive/items/{}/content'.format(fileid)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    pull_res = requests.put(url, headers=headers, data=open(filePath, 'rb'))
    pull_res = json.loads(pull_res.text)
    return pull_res

def small_uploader(client,fileName,remotePath):
    '''上传新项目
    PUT /me/drive/items/{parent-id}:/{filename}:/content

    PUT /me/drive/root:/FolderA/FileB.txt:/content??
    两者都可以


    坑逼微软api，你奶奶的,↓根本不用写好不
    Content-Type: text/plain

    '''
    url = app_url + '/v1.0/me/drive/items/root:/{}:/content'.format(fileName)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    pull_res = requests.put(url, headers=headers, data=open(fileName, 'rb'))
    pull_res = json.loads(pull_res.text)
    return pull_res

def big_uploader(client,filePath,remotePath):
    '''
    上传大文件
    :param filePath:str,上传的目标文件在本地的完整路径
    :param remotePath:str,远程网盘要放的路径
    '''
    import os.path
    # 创建上传会话，获取上传URL
    sessionInfo = uploader_creatSession(client,os.path.basename(filePath),remotePath)

    # 目标文件分段
    #todo fileRuler可以写活而不用固定长度
    fileSize = os.path.getsize(filePath)
    print(fileSize)# 获取文件大小
    fileRuler = 10485760    # 10MB 尺
    listSlice = [[i, i + fileRuler - 1, fileRuler] for i in range(0, fileSize, fileRuler)] # 生成切好的分段组数
    # 对齐末尾剩余的文件片段
    listSlice[-1] =[listSlice[-1][0],   # setPoint
        fileSize-1 if listSlice[-1][1]>fileSize else listSlice[-1][1],  # endPoint
        fileSize % fileRuler if listSlice[-1][1]>fileSize else listSlice[-1][2]] # Content-Length

    # 分段上传的头部base
    headers = {
        'Content-Type': 'application/octet-stream',
        'Content-Length': '',   # 上传片段的长度
        'Content-Range': ''  # 下一次上传，endPoint等于setPoint+新读取的片段长度-1
    }

    # 遍历分段
    for i in listSlice:
        # 构造新的分段头部
        headers['Content-Length'] = str(i[2])
        headers['Content-Range'] = 'bytes {setPoint}-{endPoint}/{fullLen}'.format(setPoint=i[0],endPoint=i[1],fullLen=fileSize)    # 下一次上传，endPoint等于setPoint+新读取的片段长度-1
        # 上传
        uploaderPart = requests.put(sessionInfo['uploadUrl'], headers=headers, data=uploader_fileSlice(filePath,i[0],i[2]))
        if uploaderPart.status_code in [200,201,202,204]:
            if uploaderPart.status_code == 201:  # 201 表示上传完成
                print({"status":"ok","info":json.loads(uploaderPart.text),"percent": "100%"})
                return {"status":"ok","info":json.loads(uploaderPart.text),"percent": "100%"}
            else:
                print({"status":"uploading","info":"","percent": '{:.0%}'.format(int(json.loads(uploaderPart.text)['nextExpectedRanges'][0].split('-')[0])/fileSize)})
                # return {"status":"uploading","info":"","percent": '{:.0%}'.format(int(json.loads(uploaderPart.text)['nextExpectedRanges'][0].split('-')[0])/fileSize)}

        else:
            print('发生错误')
            print(i)
            print(headers)
            print(uploaderPart.status_code)
            print(json.loads(uploaderPart.text))
            print(uploaderPart.status_code)


def uploader_creatSession(client,fileName,remotePath="/"):
    '''
    创建上传会话，获取上传URL
    :param fileName:str,文件名
    :param remotePath:str,远程网盘要放的路径
    '''
    url = app_url + '/v1.0/me/drive/root:/{}/{}:/createUploadSession'.format(remotePath,fileName)
    print(url)
    headers = {'Authorization': 'bearer {}'.format(client["access_token"]), 'Content-Type': 'application/json'}
    data = {
        "item": {
            "@microsoft.graph.conflictBehavior": "fail",    # 冲突行为属性,即是如果出现文件冲突则返回失败

            # "@microsoft.graph.conflictBehavior": "rename",    # 冲突行为属性,即是如果出现文件冲突则重命名

            # "@microsoft.graph.conflictBehavior": "replace",    # 冲突行为属性,即是如果出现文件冲突则替换
        }
    }
    pull_res = requests.post(url, headers=headers, data=json.dumps(data))
    print(json.loads(pull_res.text))
    if pull_res.status_code == 409:

        return False
    else:
        return json.loads(pull_res.text)


def uploader_fileSlice(filePath,setPoint,sliceLen):
    '''
    文件二进制切片
    :param filePath:
    :return:
    '''
    with open(filePath, 'rb') as f:
        f.seek(int(setPoint))   # 设置读取标头
        content = f.read(sliceLen)  # 从标头往后读取若干字节，不包括标头
    return content


def uploader_creatSession_demo(client):
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


def del_uploader(upURL):
    '''
    DELETE https://sn3302.up.1drv.com/up/fe6987415ace7X4e1eF866337
    :param client:
    :return:
    '''
    # headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    # del_res = requests.post(upURL, headers=headers)
    del_res = requests.post(upURL)
    print(del_res)

def big_uploader_demo(client,upUrl):
    '''大文件上传
    :return:
    '''
    # 创建上传会话,获取上传URL
    # sessionInfo = uploader_creatSession(client)
    # print(sessionInfo)

    # 读取需要上传的文件（部分）
    import os
    flen = os.path.getsize('test.zip')
    print(flen)
    with open('test.zip', 'rb') as f:
        f.seek(10485760)   # 标记从第几个字节 之后 开始读取
        content = f.read()    # 从标记往后读多少字节
        # print(content)

    # 上传
    headers = {
        'Content-Type': 'application/octet-stream',
        'Content-Length': str(flen-10485760),
        'Content-Range': 'bytes {setPoint}-{endPoint}/{fullLen}'.format(setPoint=10485760,endPoint=flen-1,fullLen=flen)    # 下一次上传，endPoint等于setPoint+新读取的片段长度-1
    }
    # {'expirationDateTime': '2019-09-03T06:47:03.857Z', 'nextExpectedRanges': ['60-279']}

    # 上传完成时
    # {'createdBy': {'application': {'displayName': 'AlienVan', 'id': '402aba1b'}, 'user': {'id': 'a292b424bbe0c719'}}, 'createdDateTime': '2019-08-27T11:06:21.2Z', 'cTag': 'aYzpBMjkyQjQyNEJCRTBDNzE5ITE2My4yNTc', 'eTag': 'aQTI5MkI0MjRCQkUwQzcxOSExNjMuMA', 'id': 'A292B424BBE0C719!163', 'lastModifiedBy': {'application': {'displayName': 'AlienVan', 'id': '402aba1b'}, 'user': {'id': 'a292b424bbe0c719'}}, 'lastModifiedDateTime': '2019-08-27T11:06:21.2Z', 'name': 'test.txt', 'parentReference': {'driveId': 'a292b424bbe0c719', 'driveType': 'personal', 'id': 'A292B424BBE0C719!154', 'name': '233', 'path': '/drive/root:/233'}, 'size': 280, 'webUrl': 'https://1drv.ms/t/s!ABnH4LsktJKigSM', 'items': [], 'file': {'hashes': {'quickXorHash': '4JlP/bnmCdIHBKyuoz6ZBTOta4A=', 'sha1Hash': '415FB8E95F365087303BE329F9578D18362CC8DE'}, 'mimeType': 'text/plain'}, 'fileSystemInfo': {'createdDateTime': '2019-08-27T11:06:21.2Z', 'lastModifiedDateTime': '2019-08-27T11:06:21.2Z'}, 'shared': {'owner': {'custom': {}, 'user': {'id': 'a292b424bbe0c719'}}, 'scope': 'users'}, 'tags': [], 'lenses': [], 'thumbnails': [{'id': '0', 'large': {'height': 800, 'url': 'https://wurinw.bn.files.1drv.com/y4pFSNeOfNzUVnLhd0QsizexjihHHhL0MHhebdLpfm0iM0iN_n4HRYRxbxh8qhhnySVictPnb4JUcKCd0WVQYRXMIy0IKzqxft6sIPJ5mR_L_Vm812VXUhG16PqP-ZzwyID917b9o_ZxRW_VKPIGFafyD7F4S9iUNJc57XtfUMLb-I?width=800&height=800&cropmode=none', 'width': 800}, 'medium': {'height': 176, 'url': 'https://wurinw.bn.files.1drv.com/y4pFSNeOfNzUVnLhd0QsizexjihHHhL0MHhebdLpfm0iM0iN_n4HRYRxbxh8qhhnySVictPnb4JUcKCd0WVQYRXMIy0IKzqxft6sIPJ5mR_L_Vm812VXUhG16PqP-ZzwyID917b9o_ZxRW_VKPIGFafyD7F4S9iUNJc57XtfUMLb-I?width=176&height=176&cropmode=none', 'width': 176}, 'small': {'height': 96, 'url': 'https://wurinw.bn.files.1drv.com/y4pFSNeOfNzUVnLhd0QsizexjihHHhL0MHhebdLpfm0iM0iN_n4HRYRxbxh8qhhnySVictPnb4JUcKCd0WVQYRXMIy0IKzqxft6sIPJ5mR_L_Vm812VXUhG16PqP-ZzwyID917b9o_ZxRW_VKPIGFafyD7F4S9iUNJc57XtfUMLb-I?width=96&height=96&cropmode=none', 'width': 96}}]}

    pull_res = requests.put(upUrl, headers=headers, data=content)
    pull_res = json.loads(pull_res.text)
    print(pull_res)


if __name__ == '__main__':
    temp = flush_token(info["refresh_token"])
    # # pull_res = uploader_creatSession(temp)
    # uploader_fileSlice('test.txt',233,233)

    big_uploader(temp,'test.zip','/')
    # big_uploader_demo(233,"https://api.onedrive.com/rup/a292b424bbe0c719/eyJSZXNvdXJjZUlEIjoiQTI5MkI0MjRCQkUwQzcxOSExMDMiLCJSZWxhdGlvbnNoaXBOYW1lIjoidGVzdC56aXAifQ/4mIQ2oPmMfRyQMDThAmabz9xEylkaMWXYZzXwA8dXOAhAUN7xY69_ZdYjkGhqpKPuLeJG57R3ip1iVuBut3cL0gdy4ep6ocWgZGNE_Hm5vQYE/eyJuYW1lIjoidGVzdC56aXAiLCJAbmFtZS5jb25mbGljdEJlaGF2aW9yIjoiZmFpbCJ9/4wEtH2bc6PNBIBv64vcE_gCyO36s3MMeOeSlP-CmgrJ6cWP5diQl2UMr8s6E0u6F7s_PPuIeNYZ6CL8td3XaZZJubzG8QznGgV2QMatcq2ZeC2sOBlzLRdDyo8tz5ikT6DgJTl3YnsJOBPalGrdGqzlK7fmV5Unfs10g8HfPek5U5mnlUyOYTt8VocdD2s60II4Mf7zHjCyAlXJZb3fSrENEWhaXjIh1d2WwewNrd1ATEYvmD-yvCU9-gVFvrNkr3L7xZ7qzkNw7RIO491fIal4Mwn21rzpv9z2b8mS1HZr8XTMKIi7Q1qy0Lf5gF0sUmapn7xAS9KT39ocM6wVLFvLLkX1dDix9Fe8yqbAInoG-IFsVQDid_7HRn_scpNIe91LXIONJA2xT5oPMqaaBCaaK1YdpZyt6eEZfm_wpv36Rfrt8w1dgzl9WaLDkohNYJO9Jh1sBVc1oZleLztbZk8qrVdm4V3sISkI0qK0E0pn-AQvrGj9pU318GIeT8xxqxPyEtktpqvIi2r1xk-pBBn9Px0QImpPgkV9KPGjEvp4CM")