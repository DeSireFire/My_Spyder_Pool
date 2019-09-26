import requests,json

def dlCSV(client):
    '''
    :param client:
    :return:
    '''
    url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=1583&Year=2018&Month=9&Day=1&timeframe=2"

    import chardet
    r = requests.get(url=url)

    # 获取网页编码格式，并修改为request.text的解码类型
    r.encoding = chardet.detect(r.content)['encoding']
    if r.encoding == "GB2312":
        r.encoding = "GBK"
    print(r.encoding)
    get_res = requests.get(url)
    print(get_res.text)
    print(type(get_res.text))
    with open('demo.csv', 'w',encoding=r.encoding) as f:
        f.write(get_res.text)
if __name__ == '__main__':
    dlCSV(233)