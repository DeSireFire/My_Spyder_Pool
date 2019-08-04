redirect_uri = 'https://od.cnbeining.com'

## Normal
client_secret_normal = 'o.+2TBy+7-ijKLMl05spsohdx464OtwU'
client_id_normal = 'e2d585cd-751f-4c7e-aab7-d8b48c485f94'
api_base_url = 'https://api.onedrive.com/v1.0/'
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

## Business
discovery_uri = 'https://api.office.com/discovery/'
auth_server_url = 'https://login.microsoftonline.com/common/oauth2/authorize',
auth_token_url = 'https://login.microsoftonline.com/common/oauth2/token'

# If you are working with Office 365 you may want to create your own app
# and change the following:
# You can still use https://od.cnbeining.com as redirect URL.
client_id_business = '6fdb55b4-c905-4612-bd23-306c3918217c'
client_secret_business = 'HThkLCvKhqoxTDV9Y9uS+EvdQ72fbWr/Qrn2PFBZ/Ow='


"""
    OneDrive API接口
"""
BaseAuthUrl = "https://login.microsoftonline.com"
app_url = "https://graph.microsoft.com/"


"""
    世纪互联 API接口
"""
ChinaAuthUrl = "https://login.chinacloudapi.cn"
China_app_url = "https://microsoftgraph.chinacloudapi.cn"


configJson = {
  "token": "<refresh_token>",
  "location_path": "/",
  "start_directory": "/",
  "threads": 3,
  "diff_seconds": 480,
  "refresh_seconds": 720,
  "metadata_cached_seconds": 768,
  "structure_cached_seconds": 840
}


#-*- coding=utf-8 -*-
import os

#限制调用域名
allow_site=[u'no-referrer']

#######源码目录
config_dir="/root/PyOne"
data_dir=os.path.join(config_dir,'data')

#下载链接过期时间
downloadUrl_timeout="300"

#后台密码设置
password="PyOne"

#网站名称
title="PyOne"

#自定义代码
tj_code=""""""
headCode=""""""
footCode=""""""
cssCode=""""""
robots="""
User-agent:  *
Disallow:  /
"""

#主题设置
theme="material"

#网站标题前缀
title_pre="index of "

#onedrive api设置
redirect_uri="https://pyoneauth.github.io/" #不要修改！
BaseAuthUrl='https://login.microsoftonline.com'
app_url=u'https://graph.microsoft.com/'

#aria2配置
ARIA2_HOST="localhost"
ARIA2_PORT=6800
ARIA2_SECRET=""
ARIA2_SCHEME="http"

#MongoDB
MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_USER=""
MONGO_PASSWORD=""
MONGO_DB="three"

#Redis
REDIS_HOST="localhost"
REDIS_PORT="6379"
REDIS_PASSWORD=""
REDIS_DB="0"

#搜索模式
show_secret="no"

#文件默认排序字段
default_sort="lastModtime"
order_m="desc"

#文件是否支持加密--no-文件夹加密的情况下，如果直接访问该文件夹下的文件链接，则会跳过密码
encrypt_file="no"

#默认盘位
default_pan="A"

#后台路径
admin_prefix="admin"

#是否做负载均衡
balance="False"

#多线程最大线程
thread_num="5"

#是否开启下载链接验证
verify_url="True"


od_users={
    "A":{
        "client_id":"",
        "client_secret":"",
        "share_path":"/",
        "other_name":"网盘1区",
        "order":1
    },
    "B":{
        "client_id":"",
        "client_secret":"",
        "share_path":"/",
        "other_name":"网盘2区",
        "order":2
    },
    "C":{
        "client_id":"",
        "client_secret":"",
        "share_path":"/",
        "other_name":"网盘3区",
        "order":3
    }
}



show_doc="csv,doc,docx,odp,ods,odt,pot,potm,potx,pps,ppsx,ppsxm,ppt,pptm,pptx,rtf,xls,xlsx"
show_image="bmp,jpg,jpeg,png,gif"
show_video="mp4,webm"
show_dash="avi,mpg,mpeg,rm,rmvb,mov,wmv,mkv,asf"
show_audio="ogg,mp3,wav,aac,flac,m4a"
show_code="html,htm,php,py,css,go,java,js,json,txt,sh,md"
show_redirect="exe"

#上传服务器文件完成之后是否删除文件
delete_after_upload="True"

#是否转发流量
redirect_file="False"