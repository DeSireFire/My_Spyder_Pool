import requests,json
from onedrive.authDemo import flush_token,oauthDict
from onedrive.sec import *

def get_driveInfo(client):
    '''
    获取od网盘信息
    :param client:
    :return:
    '''
    url = app_url + '/v1.0/me/drive/'
    headers = {'Authorization': 'bearer {}'.format(client["access_token"])}
    get_res = requests.get(url, headers=headers)
    get_res = json.loads(get_res.text)
    print(get_res)

if __name__ == '__main__':
    temp = flush_token(info["refresh_token"])
    get_driveInfo(temp)