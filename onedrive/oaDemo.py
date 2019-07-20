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
    '''
        {'client_id': 'e2d585cd-751f-4c7e-aab7-d8b48c485f94', 'redirect_uri': 'https://github.com/DeSireFire/AlienVan', 'client_secret': 'vpSUH80#^xtdwvWCSI194*|', 'code': 'M4d63b8cd-2951-1a96-fe98-f186a5c6e302', 'grant_type': 'authorization_code'}
        {"token_type":"Bearer","scope":"openid profile User.Read Calendars.Read","expires_in":3600,"ext_expires_in":3600,"access_token":"EwBwA8l6BAAURSN/FHlDW5xN74t6GzbtsBBeBUYAAdsemN1CnDHq+Y5iSLFXAwjk+8w0/lu+08PkykSHUhK/nffXIqpiEjC8Ql2yCjAIQ8L2iNqQIJwkpeTbo6p3Sh/84eNLOT1woQ36LZR8qS21G9SVs8Rs/oc8w6778ehSchz+QeQqTPrEmYycY0szvSWTGgpvIrY7rWUTVc8iccU3zTLQz7Oic/slnD9JdilSphoMFh5Emj0oo8Efx2n4xXUZ2IMPQVRU2ZNbw3s0RPtI5kK5Me6dxRkuQJe3ukWGNvNp606/71W48Jd1Uj1eIu26yVsSkrx0nzmHasys8JeK7ptMS5aT6JhgqHyIZa/5KyeHIiAYNz+zNsGryQYqOg0DZgAACLF7AiukjldIQAIIdVx68pkr5UzOljwl8FRAFnPqXuyqfBATGBTRNzt/WLAwRtCuEOrwuoWsziWg+TBbAScpIdaXBrXRUgFu08F+8S8jSSEWXrI5ZJyWad9FPXrSAqtrh9hNC3AoJOBVfTjJt9EdddlwQGAnXqr4m5jqTnpXhaL4o0uvJ/iweQ6VnMc/NErhWxy+qB7bQmfF9abIeJgvUITil8rlxty8+VCPpjWhEF6bz2g+8aWtvEudYgqe19m8b49Hd8SpsGx4mcDqwPAH+OFj2Rsr028EDKonApkbOfTEQLVHrUDfq2lerKhtI18SIkoxUz63XpjKzV6MKPt7j8JoB0VkZdQTyVLYI+tzE3EIyZc5glCWX6RS0afxpwDbuxQ5WaGluisdparnjlYqTNs4hGsiApJRtvLrkcsWOsTE98SmxUPfZWKyFIIoyqbXcZ+84t+vx5azvTnHNcagjvqyRsoRXb15CePDFsDVvbLN//pN5DXL4qUgwvYjL2ASKjiYDhe8FIY25PGrD8m6vz3XGOgfTa660eEcrrWlVe0lgRLTT9my9Eqgm/l2lH0EsHheqFjSgxPcYilzXOktVDxJm/mKoG/gK5kXhtw/n4yZ4m+1NQy+zzfBnPI0ScJb7ao5IEm+vlSnKJtcrvmDJa3q9TgfUz0+hJYK0B2fgz+sOprZYsiSkOZg8ICMC/7qbAxAMtGRarQBRXY9rDGAO+TpIakPlFnIRbgrnF39h1lp337IReOSm3XJBaUzI5glRpK5hq5tyzb8MsF0Ag==","refresh_token":"MCQpNgzX2jEUctXK9KfckUZ5UkSJc4SZiEFgQcfF9yWNye6qRgQ69FJlrJEDzq6tpNvaqYZyHPG60mu5aTd2zZHkax3*C6vaiK!DEDt2oLf*SGgIiWMtok77nB9aXp1dfR8gbGxatfNaERX3A7QQ3CxPxgkZ4*KYVGT6iUxCjExXqPCXPs2VkW5yK*gUprWRqRPTaj3WYpGfuBBtmMFitPz41lyPU7QFXWHfFLrNfCelsIEHTs59PNEiGV!H1fr3PQkcMlELcZ!9ASrNzjyqtT99o*nT1wENvhDOoc8pB5EJX1Onxqw3igsuW7gci2UDFxByF6swP0*a0u4EoxQySZwrlv87WVTnH2N*Sn*inCNgF7Djb7BASNFCRAYruw3m5JBzGd*murLeH62b0v3!5Our*VtKuahYntNYquZpQ4mFL6CBiDQUzHxvhN1*QbWp*dw$$","id_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjFMVE16YWtpaGlSbGFfOHoyQkVKVlhlV01xbyJ9.eyJ2ZXIiOiIyLjAiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vOTE4ODA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkL3YyLjAiLCJzdWIiOiJBQUFBQUFBQUFBQUFBQUFBQUFBQUFFeDhBWjg3aVBEUzBqdVZUVzAtQVlFIiwiYXVkIjoiZTJkNTg1Y2QtNzUxZi00YzdlLWFhYjctZDhiNDhjNDg1Zjk0IiwiZXhwIjoxNTYzNTU0NjkwLCJpYXQiOjE1NjM0Njc5OTAsIm5iZiI6MTU2MzQ2Nzk5MCwibmFtZSI6IuazvealtyDlkagiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiIxMDI1MjEyNzc5QHFxLmNvbSIsIm9pZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC1hMjkyLWI0MjRiYmUwYzcxOSIsInRpZCI6IjkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImFpbyI6IkRTeHEyTDZINkNVN05FZXBqbld0Nk5tZFozSjhIdiEqT3RtMDlNNW1uZGZkclRQQlpIVzdZZXJGcnlqU0dyeGJPNHohSzZ5czRlekVCSGtBUWFLdmxncktwdGJ6cDZkemdNRSFxTlZaR1k0Kkt4bmJUZ05WVTNQeUxrUk15diptbTM3ZnJiTkxoSXhOTmh4IWV5eTlncFEkIn0.vJJd3QR9wlFEKRiV4m5tGjXNokN9b4kQyTTu_kMmSnQqh6ZZnmaKirF_kJWwsvhSJg7_Ri2JoTHwr1HmPWp-vWOl8jzHArJSwDKnIHzT5KmR_9KmaDZbGI-fmJhgQqf8r2z8kpG5MUM3hmCME5bb80BjZ94bsDlnqOqqzbS_59QfKo5mZ0F0HN-RaA8zs65O61jldO74KjEucoeY6kKsGBzHex8Qs-xJ68AfGF39-Z3cdQBdVfw-GtV2nZhvlDlDE8bF0w_NXNJsaXp0d0fIddTy1q87s-q8aA4WrbqW7M9wgBb40e-1XLuXNOGSIOUhHtcc6dYKMqq_0lX3aVlFTg"}
    '''

def flush_token(access_token):
    myheader = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {
        'client_id':oauthDict['app_id'],
        'redirect_uri':oauthDict['redirect'],
        'client_secret':oauthDict['app_secret'],
        'refresh_token':access_token,
        'grant_type':'refresh_token',
    }
    print(data)
    req = requests.post(token_url,headers = myheader,data=data)
    print(req.text)

if __name__ == '__main__':
    # a,b = get_sign_in_url()
    # get_token_from_code('M6e2b77fc-9a73-f918-3232-dff443e62a13','xDBCZVUyedJtgOezX8RVNX5Sb2NjIA')
    flush_token('EwBwA8l6BAAURSN/FHlDW5xN74t6GzbtsBBeBUYAAckE+++tSz5D++LMImrGnqdMjmbNSs2qt5il065Mrge4m7zmgTqTzjSrIJ5RbeBKF4cXxrKmbUUMnVnqDyU72JtWCBWxHSFNRNlyE78NcnNPk4KTjeaWMkJ8AkYpLBGQaqPC97zVpqXxGxKfhWFZ/38hB51Tfa0BFBZQ9gfO58dO2LwpYJtTNLF3EwIbARY4aQB8zRmOe/6Nmk+43OBlJR2ULlHG1ZbJ6Z3A1h021uSzhUj7nlD8QksxVAkpbZe4rramYgVciAM3EKl1I/h7JgYQYBMvZDG9+Xpz4inHnJ8KoIol+KcWDsnyWmKjzCFVeZeVwaMo0O3Jrij/ZI0Y8loDZgAACM1SXtui/xzuQAKaIQBZ+B53jlngo1urw2Qh5Cdh7yI6aNk/IOW4kY83yJBTzr+NYqTJP7kViscEQcpRI6m75N0CX/ydxfMrig5bS1Xbr/Jz6RZ4xq9Yvpnp9CyLl4gV+aWm4dcHtTW3Lup87Kc5rEgta0hTfN7DRjqRvXs6pXi7alU96AiVt6LQKh+vtT8Ig4V1SlYpjIdv5F2tcVcllH+4nQPYa1FDUsI8isuUClKLxP122ZVek19Xa40dO8wCe057MW/UmbV8p0q8ojG8q+7K9U7bvh/A5SYPooO9M1TLMKf/QW1NqKdRGZYp4M6ezGkJ2Q0n/D57plJofmLsYc4elQkpz1J6IOdrdKaTNTn74x4GZyi9YyzVgmxRhw90fkbiFuIvCUlbw6mDRW6znOwwno2zsEV59yYWkDsuI8xgMRLHMBO6EXrPy1SGbcrHmPn20FqkUQhZv+iAt2bqjbkmuvXdqfduBk+VTHMj0C3dvOpMm8vuszuSpfLI1o9wrq7p6ooKw2UBbXum69oIMcbj01HcNce30nvhQtb4M9EzZtGK7FS54BvV+u3VEAU7jjrrFgngxlJs/NBuf/K/PsbMJ6lmNW/Pzd/yaQ9BVrDRdpADEiQdmVsSV2zwUh9d2/aGc7LRybWdEgy4Vu0kgmStXF8Au7SdSvHeJEc61rHgShQw4bczIYVWJfcB66PfqIf5Tg1gtJXX/kPLjsGIZe/6EPK1bgdi7h1nRzITmxS2I66n/mI1CN5pWQsGuW37zd0Nb7IbjgXnPIt1Ag==","refresh_token":"MCXpyfbzEaZAxSiuyTv93nee6GRw7VqIagW!Y06d58HMLrxFHHhOsDKi9Y0kor0XLZJhhBjzJF*FbgsO8yvXlmp6EEediGdYhOgbKh39WZYSRegrE0JvsvD4Gv234s5IIaoX!k!EEd6YAW2GdKOlJ9cmHXsCt7Hpln*DvP6TuP4XlPJGm568pshtJKqF!XsfAn41Kq7zLVNxLkLZOEjG0lf5xwp!T!47WEWp7PorHPDDMdhUJDpF0kUX5VQ51IW6PfG*mtl6UKQ!gHIVi7CXJPwegJSU77qd6xXJSMFPeWnvE7vO7Tikcfa1loJFsiYuy2vxm4rBJMR*BcnKeIUzH3vV20JBHfw*Ttiv0Wic**IVKG4xht0mkS501m*iioddBKYyQKO4l3tZsx7yJhWXgr9EpFbbrWJf5BWfCJLsPDl632cSkNPDUGUfHiLbnMj6U4A$$","id_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjFMVE16YWtpaGlSbGFfOHoyQkVKVlhlV01xbyJ9.eyJ2ZXIiOiIyLjAiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vOTE4ODA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkL3YyLjAiLCJzdWIiOiJBQUFBQUFBQUFBQUFBQUFBQUFBQUFFeDhBWjg3aVBEUzBqdVZUVzAtQVlFIiwiYXVkIjoiZTJkNTg1Y2QtNzUxZi00YzdlLWFhYjctZDhiNDhjNDg1Zjk0IiwiZXhwIjoxNTYzNzEzODE5LCJpYXQiOjE1NjM2MjcxMTksIm5iZiI6MTU2MzYyNzExOSwibmFtZSI6IuazvealtyDlkagiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiIxMDI1MjEyNzc5QHFxLmNvbSIsIm9pZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC1hMjkyLWI0MjRiYmUwYzcxOSIsInRpZCI6IjkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImFpbyI6IkRVeG9lRlJ3IW9zTUVTN0dObEx2R0tEQ2JnN0I3cVo4MnhVVkRaV2lsc0NsNXRCU3FRaDZCU2MzOTRrZXZCZGZLWnBvZnVJV0VCUWVmVVVFKldPZ2VVRE4hV2lHdktsZXl0UHF3a0F0UHhaZlBHQXhLYmZvQWdWWnJkbmY2RjBsRVBSWmZjWEZxZk9ubXpxbUhTdUZEbzgkIn0.1BwIWicdNpvhli0Dj7JelLwTEexqEHVg1eeic615aDz07xaOD6_lT6nkxsni5ni-HSBkFBHruVMLw_eqGqog_xLdXEcBJX3CLfH5OgkrXow1QyHAJfmL8o6KhFU1p6OUCN9fjiW4OuC2nCZ4BGIc-VufHMoOhR7Ab6-c3p2tBUGo1D2bahxgjfLJaM4U505sylg4ZSnAxMg7P05FG1cU_fgvzu-sikEqvBdY8hK2fL5ZSLwgIlliXIDwSXun5u0eO0aJ94XokZ5ViC3atORhc_TDIi5PoXT2xxhwm4zI7ODrELeea8rhYEXHuVNFNlwl8QuUG6WbVatSkzv_oDzjsw')