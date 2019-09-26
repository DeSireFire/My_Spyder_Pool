import requests,json
from onedrive.authDemo import flush_token,oauthDict
from onedrive.sec import *

def odf(client):
    '''
    选择性查询od
    :param client:
    :return:
    '''
     # 查询文件名包含.jpg且 "image类型不为 null" 的所有子项
    url = app_url + '/v1.0/me/drive/'+"/root/search(q='.jpg')?filter=image%20ne%20null"

    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    get_res = requests.get(url, headers=headers)
    get_res = json.loads(get_res.text)
    print(get_res)
    print(len(get_res['value']))
    for i in get_res['value']:
        print(i)


if __name__ == '__main__':
    temp = flush_token(info["refresh_token"])
    odf(temp)

    # f = open("test.txt", "r")
    # TEMP = json.loads(f.read().replace('\x20',' ').replace(r'\x2',' '))
    # # TEMP = json.loads(json.dumps(f.read()))
    # print(TEMP)
    # print(type(TEMP))
    #
    # print(TEMP['address']['address1'])
