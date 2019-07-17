from requests_oauthlib import OAuth2Session

oauthDict = {
'app_id':'e2d585cd-751f-4c7e-aab7-d8b48c485f94',
'app_secret':'vpSUH80#^xtdwvWCSI194*|',
'redirect':'http://localhost:5360/tutorial/callback',
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
    # return sign_in_url, state

if __name__ == '__main__':
    get_sign_in_url()