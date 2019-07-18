from requests_oauthlib import OAuth2Session
import requests
'''
redirect 跳转URL必须与应用中 平台 添加的 web 重定向URL 保持一致
https://apps.dev.microsoft.com/?referrer=https%3A%2F%2Fdev.onedrive.com#/appList
使用非localhost时，URL必须使用https.
'''
oauthDict = {
'app_id':'e2d585cd-751f-4c7e-aab7-d8b48c485f94',
'app_secret':'vpSUH80#^xtdwvWCSI194*|',
'redirect':'https://github.com/DeSireFire/AlienVan',
# 'redirect':'http://localhost:5360/',
'scopes':'openid profile offline_access user.read calendars.read',
'authority':'https://login.microsoftonline.com/common',
'authorize_endpoint':'/oauth2/v2.0/authorize',
'token_endpoint':'/oauth2/v2.0/token',
}
authorize_url = '{0}{1}'.format(oauthDict['authority'], oauthDict['authorize_endpoint'])
token_url = '{0}{1}'.format(oauthDict['authority'], oauthDict['token_endpoint'])

def get_sign_in_url():
    '''
    初始化OA链接
    :return:
    '''
    new_auth = OAuth2Session(oauthDict['app_id'],
    scope=oauthDict['scopes'],
    redirect_uri=oauthDict['redirect'])
    sign_in_url, state = new_auth.authorization_url(authorize_url, prompt='login')
    print(sign_in_url)
    print(state)
    print(authorize_url)
    print(token_url)
    return sign_in_url, state

def get_token_from_code(callback_url, expected_state):
    '''
    得到返回链接：https://github.com/DeSireFire/AlienVan?code=M4d63b8cd-2951-1a96-fe98-f186a5c6e302&state=a13ypG9SFzKej0tQXvBiD1QPt46x9v
    :param callback_url: 为示例链接里面的code
    :param expected_state: 为实例链接里面的state
    :return:
    '''
    # Initialize the OAuth client
    # aad_auth = OAuth2Session(oauthDict['app_id'],
    # state=expected_state,
    # scope=oauthDict['scopes'],
    # redirect_uri=oauthDict['redirect'])
    #
    # token = aad_auth.fetch_token(token_url,
    # client_secret = oauthDict['app_secret'],
    # authorization_response=callback_url)
    #   return token
    myheader = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {
        'client_id':oauthDict['app_id'],
        'redirect_uri':oauthDict['redirect'],
        'client_secret':oauthDict['app_secret'],
        'code':callback_url,
        'grant_type':'authorization_code',
    }
    print(data)
    req = requests.post(token_url,headers = myheader,data=data)
    print(req.text)

if __name__ == '__main__':
    # pass
    # get_sign_in_url()
    # a,b = get_sign_in_url()
    get_token_from_code('M4d63b8cd-2951-1a96-fe98-f186a5c6e302','a13ypG9SFzKej0tQXvBiD1QPt46x9v')