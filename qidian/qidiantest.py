import requests,chardet

# url = 'https://book.qidian.com/ajax/book/category?_csrfToken=wlXYhEZruscwFhTm0ydpg1DXxnNvHTdaE7kk7WGu&bookId=1004608738'
# url = 'https://sou.xanbhx.com/search?siteid=qula&q=%E5%A4%A7%E7%8E%8B%E9%A5%B6%E5%91%BD+%E4%BC%9A%E8%AF%B4%E8%AF%9D%E7%9A%84%E8%82%98%E5%AD%90'
# url = 'http://www.mmkuu.com/modules/article/search.php'
url = 'https://www.biquge.com.cn/book/23488/'
# url = 'https://so.biqusoso.com/s.php?ie=gbk&siteid=biqiuge.com&s=2758772450457967865&q=圣墟'
# url = 'https://www.biquge.com.cn/search.php?keyword=道君'
data = {

}
reps = requests.get(url)
reps.encoding = chardet.detect(reps.content)['encoding']
if reps.encoding == "GB2312":
    reps.encoding = "GBK"
# reps = requests.post(url,data=data)
print(reps.text)
print([reps.text])