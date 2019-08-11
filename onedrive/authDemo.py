from requests_oauthlib import OAuth2Session
import requests,json
from onedrive.sec import *
'''
授权链接(旧)：
https://login.live.com/oauth20_authorize.srf?client_id=e2d585cd-751f-4c7e-aab7-d8b48c485f94&response_type=code&redirect_uri=https://od.cnbeining.com&scope=wl.signin wl.offline_access onedrive.readwrite
授权链接（新）：
https://login.microsoftonline.com/common/oauth2/authorize?client_id=4345a7b9-9a63-4910-a426-35363201d503&response_mode=form_post&response_type=code+id_token&scope=openid+profile&state=OpenIdConnect.AuthenticationProperties%3dpdFzlJpy3Dlq7gdE-ZdSaP5asedm7arwGYseEQl4QDJRmFuMMfdZs210IrclKHsGOLkDTZ5VOAKe8Fu-fwBYeH7JoS7IbOKN7NRB1h8_FffjcCiRofqeBmIxaVmRoHfxBC8Sm_x2IGsLa7mbFhIOlcd5KCAIzr9uxjzHrd0wJ7lgQ4zxiRYPwSfAL7ruDbxiYCN3ln8wxNj5lh2VKldAHA&nonce=637004951218826063.MzlhNDAxM2MtNTJmNC00MDI4LWE4ZTMtOWIzNTVhMjYzMGFhYmQzYmQ4Y2EtODEyYy00MDczLWIyMzQtNGRjODRmOGUyODg2&redirect_uri=https%3a%2f%2fwww.office.com%2f&ui_locales=zh-CN&mkt=zh-CN&client-request-id=913f7c24-73ed-46bb-bdbe-45ebcb22bc99&prompt=select_account
'''
'''
redirect 跳转URL必须与应用中 平台 添加的 web 重定向URL 保持一致
https://apps.dev.microsoft.com/?referrer=https%3A%2F%2Fdev.onedrive.com#/appList
使用非localhost时，URL必须使用https.
https://login.live.com/oauth20_authorize.srf?client_id=e2d585cd-751f-4c7e-aab7-d8b48c485f94&response_type=code&redirect_uri=https%3A%2F%2Fod.cnbeining.com&scope=wl.signin+wl.offline_access+onedrive.readwrite
'''

def get_sign_in_url():
    '''
    初始化OA链接
    :return:
    '''
    new_auth = OAuth2Session(oauthDict['app_id'],
    scope=oauthDict['scopes'],
    redirect_uri=oauthDict['redirect'])
    sign_in_url, state = new_auth.authorization_url(authorize_url, prompt='login')
    return sign_in_url, state

def get_token_from_code(code, expected_state):
    '''
    得到返回链接：https://github.com/DeSireFire/AlienVan?code=M4d63b8cd-2951-1a96-fe98-f186a5c6e302&state=a13ypG9SFzKej0tQXvBiD1QPt46x9v
    :param callback_url: 为示例链接里面的code
    :param expected_state: 为实例链接里面的state
    :return:
    '''
    myheader = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {
        'client_id':oauthDict['app_id'],
        'redirect_uri':oauthDict['redirect'],
        'client_secret':oauthDict['app_secret'],
        'code':code,
        'grant_type':'authorization_code',
    }
    req = requests.post(token_url,headers = myheader,data=data)
    print(json.loads(req.text))
    print(type(json.loads(req.text)))
    return json.loads(req.text)

def flush_token(refresh_token):
    '''
    令牌刷新
    :param refresh_token: 字符串，原旧的令牌
    :return:
    '''
    data = {
        'client_id':oauthDict['app_id'],
        'redirect_uri':oauthDict['redirect'],
        'client_secret':oauthDict['app_secret'],
        'refresh_token':refresh_token,
        'grant_type':'refresh_token',
    }
    req = requests.post(token_url,data=data)
    print(json.loads(req.text))
    print(type(json.loads(req.text)))
    return json.loads(req.text)

def flush_oken(id):
    redirect_url = "https://127.0.0.1/auth"
    ReFreshData = 'client_id={client_id}&redirect_uri={redirect_uri}&client_secret={client_secret}&refresh_token={refresh_token}&grant_type=refresh_token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = ReFreshData.format(client_id = info['app_id'], redirect_uri = redirect_url, client_secret = info['app_secret'],
                              refresh_token = info["refresh_token"])
    if True == 1:
        url = BaseAuthUrl + '/common/oauth2/v2.0/token'
    # else:
    #     url = config.ChinaAuthUrl + '/common/oauth2/token'
    #     data = "{}&resource=https://{}-my.sharepoint.cn/".format(data, data_list.other)
    res = requests.post(url, data=data, headers=headers)
    return res.text



if __name__ == '__main__':
    print(authorize_url)
    print(token_url)
    sign_in_url,state = get_sign_in_url()
    print(sign_in_url)
    print(state)
    code = input('code:')
    temp = get_token_from_code(code,state)
    flush_token(temp['refresh_token'])