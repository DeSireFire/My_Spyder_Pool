import requests

URLS = {
    'trackers_best':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt',
    'trackers_all':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt',
    'trackers_all_udp':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt',
    'trackers_all_http':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt',
    'trackers_all_https':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt',
    'trackers_all_ws':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt',
    'trackers_best_ip':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt',
    'trackers_all_ip':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt',
        }

_header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

def getBest(URL,_header,_str = False):
    '''
    获取git上的Tracker,提高磁链的下载速度
    :param URL: 字符串，请求的URL地址
    :param _header: 字典，请求的网页头部
    :param _str: 布尔值，是否将结果拼接成字符串。
    :return: 根据变量_str,来决定试输出字符串还是列表
    '''

    _respone = requests.get(url=URL,headers=_header)
    if _str:
        print(''.join(list(map(lambda x: '&tr='+x,_respone.text.split()))))
        return ''.join(list(map(lambda x: '&tr='+x,_respone.text.split())))
    else:
        print(list(map(lambda x: '&tr='+x,_respone.text.split())))
        return list(map(lambda x: '&tr='+x,_respone.text.split()))



if __name__ == '__main__':
    for k in URLS:
        getBest(URLS[k],_header,True)
        getBest(URLS[k],_header)

# magnet:?xt=urn:btih:deade98152a7b4683204e02989b8c0aab5a05366&tr=udp://tracker.coppersurfer.tk:6969/announce&tr=udp://tracker.open-internet.nl:6969/announce&tr=udp://tracker.leechers-paradise.org:6969/announce&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=http://tracker.opentrackr.org:1337/announce&tr=udp://9.rarbg.to:2710/announce&tr=udp://9.rarbg.me:2710/announce&tr=udp://tracker.openbittorrent.com:80/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://tracker.torrent.eu.org:451/announce&tr=udp://tracker.tiny-vps.com:6969/announce&tr=udp://denis.stalker.upeer.me:6969/announce&tr=udp://tracker.cyberia.is:6969/announce&tr=udp://thetracker.org:80/announce&tr=udp://open.demonii.si:1337/announce&tr=udp://bt.xxx-tracker.com:2710/announce&tr=udp://explodie.org:6969/announce&tr=http://open.acgnxtracker.com:80/announce&tr=http://explodie.org:6969/announce&tr=udp://ipv4.tracker.harry.lu:80/announce&tr=udp://tracker.uw0.xyz:6969/announce&tr=http://tracker.bz:80/announce&tr=udp://tracker.moeking.me:6969/announce&tr=udp://tracker.iamhansen.xyz:2000/announce&tr=udp://tracker.filepit.to:6969/announce&tr=udp://tracker.filemail.com:6969/announce&tr=udp://torrentclub.tech:6969/announce&tr=udp://retracker.netbynet.ru:2710/announce&tr=http://vps02.net.orel.ru:80/announce&tr=http://tracker.tvunderground.org.ru:3218/announce&tr=http://torrentclub.tech:6969/announce&tr=http://t.nyaatracker.com:80/announce&tr=http://retracker.mgts.by:80/announce&tr=udp://tracker.supertracker.net:1337/announce&tr=udp://tracker.nyaa.uk:6969/announce&tr=https://tracker.fastdownload.xyz:443/announce&tr=https://t.quic.ws:443/announce&tr=http://torrent.nwps.ws:80/announce&tr=http://open.trackerlist.xyz:80/announce&tr=udp://zephir.monocul.us:6969/announce&tr=udp://tracker.trackton.ga:7070/announce&tr=udp://tracker-udp.gbitt.info:80/announce&tr=udp://retracker.sevstar.net:2710/announce&tr=udp://retracker.maxnet.ua:80/announce&tr=udp://retracker.baikal-telecom.net:2710/announce&tr=udp://retracker.akado-ural.ru:80/announce&tr=udp://pubt.in:2710/announce&tr=udp://home.penza.com.ru:6969/announce&tr=udp://carapax.net:6969/announce&tr=udp://bt.dy20188.com:80/announce&tr=https://tracker.vectahosting.eu:2053/announce&tr=https://tracker.parrotsec.org:443/announce&tr=https://tracker.gbitt.info:443/announce&tr=http://tracker.torrentyorg.pl:80/announce&tr=http://tracker.moxing.party:6969/announce&tr=http://tracker.gbitt.info:80/announce&tr=http://tracker.bt4g.com:2095/announce&tr=http://retracker.sevstar.net:2710/announce&tr=http://mail2.zelenaya.net:80/announce&tr=http://gwp2-v19.rinet.ru:80/announce&tr=http://carapax.net:6969/announce&tr=udp://tracker.msm8916.com:6969/announce&tr=udp://tracker.fixr.pro:6969/announce&tr=udp://packages.crunchbangplusplus.org:6969/announce&tr=udp://chihaya.toss.li:9696/announce&tr=https://1337.abcvg.info:443/announce&tr=http://t.acg.rip:6699/announce&tr=http://share.camoe.cn:8080/announce&tr=http://bt-tracker.gamexp.ru:2710/announce&tr=udp://tracker4.itzmx.com:2710/announce&tr=http://tracker4.itzmx.com:2710/announce&tr=http://tracker3.itzmx.com:6961/announce&tr=http://tracker2.itzmx.com:6961/announce&tr=http://tracker1.itzmx.com:8080/announce
# magnet:?xt=urn:btih:547D64DEC379E0A5511C56065C75D7FE9E860BCB&tr=udp://tracker.coppersurfer.tk:6969/announce&tr=udp://tracker.open-internet.nl:6969/announce&tr=udp://tracker.leechers-paradise.org:6969/announce&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=http://tracker.opentrackr.org:1337/announce&tr=udp://9.rarbg.to:2710/announce&tr=udp://9.rarbg.me:2710/announce&tr=udp://tracker.openbittorrent.com:80/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://tracker.torrent.eu.org:451/announce&tr=udp://tracker.tiny-vps.com:6969/announce&tr=udp://denis.stalker.upeer.me:6969/announce&tr=udp://tracker.cyberia.is:6969/announce&tr=udp://thetracker.org:80/announce&tr=udp://open.demonii.si:1337/announce&tr=udp://bt.xxx-tracker.com:2710/announce&tr=udp://explodie.org:6969/announce&tr=http://open.acgnxtracker.com:80/announce&tr=http://explodie.org:6969/announce&tr=udp://ipv4.tracker.harry.lu:80/announce&tr=udp://tracker.uw0.xyz:6969/announce&tr=http://tracker.bz:80/announce&tr=udp://tracker.moeking.me:6969/announce&tr=udp://tracker.iamhansen.xyz:2000/announce&tr=udp://tracker.filepit.to:6969/announce&tr=udp://tracker.filemail.com:6969/announce&tr=udp://torrentclub.tech:6969/announce&tr=udp://retracker.netbynet.ru:2710/announce&tr=http://vps02.net.orel.ru:80/announce&tr=http://tracker.tvunderground.org.ru:3218/announce&tr=http://torrentclub.tech:6969/announce&tr=http://t.nyaatracker.com:80/announce&tr=http://retracker.mgts.by:80/announce&tr=udp://tracker.supertracker.net:1337/announce&tr=udp://tracker.nyaa.uk:6969/announce&tr=https://tracker.fastdownload.xyz:443/announce&tr=https://t.quic.ws:443/announce&tr=http://torrent.nwps.ws:80/announce&tr=http://open.trackerlist.xyz:80/announce&tr=udp://zephir.monocul.us:6969/announce&tr=udp://tracker.trackton.ga:7070/announce&tr=udp://tracker-udp.gbitt.info:80/announce&tr=udp://retracker.sevstar.net:2710/announce&tr=udp://retracker.maxnet.ua:80/announce&tr=udp://retracker.baikal-telecom.net:2710/announce&tr=udp://retracker.akado-ural.ru:80/announce&tr=udp://pubt.in:2710/announce&tr=udp://home.penza.com.ru:6969/announce&tr=udp://carapax.net:6969/announce&tr=udp://bt.dy20188.com:80/announce&tr=https://tracker.vectahosting.eu:2053/announce&tr=https://tracker.parrotsec.org:443/announce&tr=https://tracker.gbitt.info:443/announce&tr=http://tracker.torrentyorg.pl:80/announce&tr=http://tracker.moxing.party:6969/announce&tr=http://tracker.gbitt.info:80/announce&tr=http://tracker.bt4g.com:2095/announce&tr=http://retracker.sevstar.net:2710/announce&tr=http://mail2.zelenaya.net:80/announce&tr=http://gwp2-v19.rinet.ru:80/announce&tr=http://carapax.net:6969/announce&tr=udp://tracker.msm8916.com:6969/announce&tr=udp://tracker.fixr.pro:6969/announce&tr=udp://packages.crunchbangplusplus.org:6969/announce&tr=udp://chihaya.toss.li:9696/announce&tr=https://1337.abcvg.info:443/announce&tr=http://t.acg.rip:6699/announce&tr=http://share.camoe.cn:8080/announce&tr=http://bt-tracker.gamexp.ru:2710/announce&tr=udp://tracker4.itzmx.com:2710/announce&tr=http://tracker4.itzmx.com:2710/announce&tr=http://tracker3.itzmx.com:6961/announce&tr=http://tracker2.itzmx.com:6961/announce&tr=http://tracker1.itzmx.com:8080/announce