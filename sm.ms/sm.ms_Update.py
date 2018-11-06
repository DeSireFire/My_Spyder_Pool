import urllib.request,urllib.parse
import http.cookiejar


sm_url = "https://sm.ms/api/upload"
sm_dict = {
    "smfile":open('1.jpg', 'rb')
}
sm_headers = {
    "Host":"sm.ms",
    "Connection":"keep - alive",
    "Content - Length":"57398",
    "Content - Type":"multipart / form - data;boundary = ----WebKitFormBoundarypAIqI1RWBfPWiOKq------WebKitFormBoundarypAIqI1RWBfPWiOKq",
    "Content - Disposition":"form - data;name = 'smfile';filename = '1.png'",
    # "Content - Type":"image / png-----WebKitFormBoundarypAIqI1RWBfPWiOKq",
    # "Content - Disposition":"form - data;name = 'file_id'0- -----WebKitFormBoundarypAIqI1RWBfPWiOKq - -",
}
# sm_headers,sm_dict = multipart_encode({
#     "smfile":open('1.jpg', 'rb')
# })
# 载入cookies处理器
sm_cookie = http.cookiejar.CookieJar()
sm_handler = urllib.request.HTTPCookieProcessor(sm_cookie)
# 在此处build_opener()方法中放入handler类处理即可。
sm_opener = urllib.request.build_opener(sm_handler)
sm_data = bytes(urllib.parse.urlencode(sm_dict),encoding="utf8")
sm_request = urllib.request.Request(url=sm_url,data=sm_data,method="POST")
sm_response = sm_opener.open(sm_request)
print(sm_response.read().decode("utf-8"))
for i in sm_cookie:
    print(i.name+"="+i.value)