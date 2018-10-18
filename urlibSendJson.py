# send http
import urllib.request
The_id = "1"
# name = "233666888"
department = "233666888"
position = "233666888"
phone = "233666888"
email = "233666888"
data = {}
data['id'] = The_id
# data['name'] = name
data['department'] = department
data['position'] = position
data['phone'] = phone
data['email'] = email
my_headers = {'Content-Type': 'application/json'}

# url = 'http://172.19.237.1:8091/web/index.jsp'
url = 'http://httpbin.org/post'
params = urllib.parse.urlencode(data).encode(encoding='UTF8')
my_request = urllib.request.Request(url,data = params,headers = my_headers)
my_responese = urllib.request.urlopen(my_request)
my_html = my_responese.read().decode('utf-8')
print(my_html)