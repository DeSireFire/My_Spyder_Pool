import requests
import chardet
import re

'''
得到的关键数据样本：
<trclass=""><tdwidth="98">今天17:04<spanstyle="display:none;">2018/12/1317:04</span></td><tdwidth="6%"align="center"><aclass="sort-2"href="/topics/list/sort_id/2"><fontcolor=red>動畫</font></a></td><tdclass="title"><ahref="/topics/view/506220_2018_9_1080P.html"target="_blank">【国漫2018】[画江湖之不良人][第三季][第9话][负载而行][1080P]</a></td><tdnowrap="nowrap"align="center"><aclass="download-arrowarrow-magnet"title="磁力下載"href="magnet:?xt=urn:btih:PGTZGKCVW7YMEE3U22YGNXVPGVYTT2PF&dn=&tr=http%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=udp%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=http%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.prq.to%2Fannounce&tr=http%3A%2F%2Fopen.acgtracker.com%3A1096%2Fannounce&tr=https%3A%2F%2Ft-115.rhcloud.com%2Fonly_for_ylbud&tr=http%3A%2F%2Fbtfile.sdo.com%3A6961%2Fannounce&tr=http%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce">&nbsp;</a></td><tdnowrap="nowrap"align="center">706.1MB</td><tdnowrap="nowrap"align="center"><spanclass="btl_1">-</span></td><tdnowrap="nowrap"align="center"><spanclass="bts_1">-</span></td><tdnowrap="nowrap"align="center">-</td><tdalign="center"><ahref="/topics/list/user_id/678521">欧炀龙俊</a></td>
进行提取
<trclass=""><tdwidth="98">今天17:04<spanstyle="display:none;">([\s\S]*?)</span></td><tdwidth="6%"align="center"><aclass="sort-2"href="/topics/list/sort_id/2"><fontcolor=red>([\s\S]*?)</font></a></td><tdclass="title"><ahref="([\s\S]*?)"target="_blank">([\s\S]*?)</a></td><tdnowrap="nowrap"align="center"><aclass="download-arrowarrow-magnet"title="磁力下載"href="([\s\S]*?)">&nbsp;</a></td><tdnowrap="nowrap"align="center">([\s\S]*?)</td><tdnowrap="nowrap"align="center"><spanclass="btl_1">([\s\S]*?)</span></td><tdnowrap="nowrap"align="center"><spanclass="bts_1">([\s\S]*?)</span></td><tdnowrap="nowrap"align="center">([\s\S]*?)</td><tdalign="center"><ahref="/topics/list/user_id/678521">欧炀龙俊</a></td>
<trclass=""><tdwidth="98">今天01:05<spanstyle="display:none;">2018/12/1301:05</span></td><tdwidth="6%"align="center"><aclass="sort-2"href="/topics/list/sort_id/2"><b><fontcolor=red>動畫</font></b></a></td><tdclass="title"><spanclass="tag"><ahref="/topics/list/team_id/303">动漫国字幕组</a></span><ahref="/topics/view/506188_10_10_720P_MP4.html"target="_blank">【茉语星梦&动漫国字幕组】★10月新番[哥布林杀手][10][720P][简体][MP4]</a></td><tdnowrap="nowrap"align="center"><aclass="download-arrowarrow-magnet"title="磁力下載"href="magnet:?xt=urn:btih:A7TDIKGNUNWU2PKQGN2RUHTQFTNV2CJB&dn=&tr=http%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=udp%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=http%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.prq.to%2Fannounce&tr=http%3A%2F%2Fopen.acgtracker.com%3A1096%2Fannounce&tr=https%3A%2F%2Ft-115.rhcloud.com%2Fonly_for_ylbud&tr=http%3A%2F%2Fbtfile.sdo.com%3A6961%2Fannounce&tr=http%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=http%3A%2F%2Ftr.bangumi.moe%3A6969%2Fannounce&tr=http%3A%2F%2Ft.nyaatracker.com%2Fannounce&tr=http%3A%2F%2Fopen.nyaatorrents.info%3A6544%2Fannounce&tr=http%3A%2F%2Ft2.popgo.org%3A7456%2Fannonce&tr=http%3A%2F%2Fshare.camoe.cn%3A8080%2Fannounce&tr=http%3A%2F%2Fopentracker.acgnx.se%2Fannounce&tr=http%3A%2F%2Ftracker.acgnx.se%2Fannounce&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=http%3A%2F%2F208.67.16.113%3A8000%2Fannonuce&tr=https%3A%2F%2Ftr.bangumi.moe%3A6969%2Fannounce&tr=http%3A%2F%2Ft.acg.rip%3A6699%2Fannounce&tr=http%3A%2F%2Ftracker.kamigami.org%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker.kisssub.org%3A2015%2Fannounce&tr=http%3A%2F%2F94.228.192.98%2Fannounce&tr=http%3A%2F%2Ftracker.btcake.com%2Fannounce&tr=http%3A%2F%2Fbt.sc-ol.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker3.torrentino.com%2Fannounce&tr=http%3A%2F%2Ftracker2.torrentino.com%2Fannounce&tr=http%3A%2F%2Fpubt.net%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker.tfile.me%2Fannounce&tr=http%3A%2F%2Fbigfoot1942.sektori.org%3A6969%2Fannounce&tr=http%3A%2F%2Fsukebei.tracker.wf%3A8888%2Fannounce&tr=http%3A%2F%2Ft.nyaatracker.com%3A80%2Fannounce&tr=https%3A%2F%2Fopen.kickasstracker.com%3A443%2Fannounce&tr=http%3A%2F%2Ftracker.ktxp.com%3A6868%2Fannounce&tr=http%3A%2F%2Ftracker.ktxp.com%3A7070%2Fannounce">&nbsp;</a></td><tdnowrap="nowrap"align="center">187.1MB</td><tdnowrap="nowrap"align="center"><spanclass="btl_1">-</span></td><tdnowrap="nowrap"align="center"><spanclass="bts_1">-</span></td><tdnowrap="nowrap"align="center">-</td><tdalign="center"><ahref="/topics/list/user_id/420797">春音爱良aira</a></td></tr>
<div class="topic-title box ui-corner-all">
	<h3>【极影字幕社】★ 腹黑妹妹控兄记 ~人家才不喜欢哥哥这种人呢~ 全集 GB_CN 720P MP4  </h3>
	<div class="info resource-info right">
		<ul>
            <li>所屬分類: <span>
<a href="/topics/list/sort_id/2">動畫</a>&nbsp;&gt;&nbsp;			<a href="/topics/list/sort_id/31"><b><font color=red>季度全集</font></b></a><span></li>
			<li>發佈時間: <span>2011/04/01 12:27</span></li>
						<li>種子下載: <a href="#description-end">下載種子/磁力鏈接</a></li>
			<li>文件大小: <span>2.2GB</span></li>
			<li>訪客互動: 
			
			<a class="magnet" id="a_magnet" href="magnet:?xt=urn:btih:HUP7UONMHZB7TPNVEG4ZF4LDRLZSH5QG&amp;dn=%5BKTXP%5D%5BOniichan%5D%5B01-12%5D%5BGB_CN%5D%5B720P%5D%5BMP4%5D&amp;tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&amp;tr=http%3A%2F%2Fdenis.stalker.h3q.com%3A6969%2Fannounce&amp;tr=http%3A%2F%2Ftracker.prq.to%2Fannounce&amp;tr=http%3A%2F%2Ftracker.ktxp.com%3A6868%2Fannounce&amp;tr=http%3A%2F%2Ftracker.ktxp.com%3A7070%2Fannounce&amp;tr=http%3A%2F%2Ftracker.openbittorrent.com%2Fannounce&amp;tr=http%3A%2F%2Ftracker.publicbt.com%2Fannounce&amp;tr=http%3A%2F%2Ftracker.dmhy.org%3A8000%2Fannounce&amp;tr=http%3A%2F%2Fbt.popgo.net%3A7456%2Fannounce&amp;tr=http%3A%2F%2Fnyaatorrents.info%3A7266%2Fannounce&amp;tr=http%3A%2F%2Fnyaatorrents.info%3A3277%2Fannounce&amp;tr=http%3A%2F%2Fanisource.spb.ru%2Fannounce&amp;tr=http%3A%2F%2Ftracker.anirena.com%3A81%2Fannounce&amp;tr=http%3A%2F%2Ftracker.anirena.com%3A6969%2Fannounce&amp;tr=http%3A%2F%2Ftracker.frozen-layer.net%3A6969%2Fannounce">magnet:?xt=urn:btih:HUP7UONMHZB7TPNVEG4ZF4LDRLZSH5QG</a>



<strong>簡介:&nbsp;</strong><br /><p><font face="Helvetica">字幕制作 <a href="http://windmoe.com/" target="_blank" rel="external nofollow">WINDMOE.COM</a></font></p>
<p>&nbsp;</p>
<p><img src="http://windmoe.com/wp-content/uploads/2011/04/ryuki02.jpg" style="width: 500px; height: 283px" alt="" /></p>
<p>&nbsp;</p>
<p><font face="Helvetica">制作废话<br />
三月这样那样的忙，所以第二话迟来了，抱歉。魔法少女小圆跟假面骑士龙骑，意外的有不少相似，但貌似不能相提并论。另外，个人也想跟QB或神崎士郎签约，笑。</font></p>
<p>&nbsp;</p>
<p><font face="Helvetica">【名称】<br />
仮面ライダー龍騎,Kamen Rider Ryuki,假面骑士龙骑,幪面超人龍騎</font></p>
<p>&nbsp;</p>
<p><font face="Helvetica">【介绍】<br />
平成第三作，以镜世界为主题，假面骑士再不是英雄的代名词，而是欲望的追随者。作为13名假面骑士的一员，城户真司却是以保护人类为己任，这也引发与其他骑士间的一系列斗争&hellip;&hellip;（By yamilawliet）</font></p><br />
</div>

<strong>簡介:&nbsp;</strong><br /><p><font face="Helvetica">字幕制作 <a href="http://windmoe.com/" target="_blank" rel="external nofollow">WINDMOE.COM</a></font></p>\r\n<p>&nbsp;</p>\r\n<p><img src="http://windmoe.com/wp-content/uploads/2011/04/ryuki02.jpg" style="width: 500px; height: 283px" alt="" /></p>\r\n<p>&nbsp;</p>\r\n<p><font face="Helvetica">制作废话<br />\r\n三月这样那样的忙，所以第二话迟来了，抱歉。魔法少女小圆跟假面骑士龙骑，意外的有不少相似，但貌似不能相提并论。另外，个人也想跟QB或神崎士郎签约，笑。</font></p>\r\n<p>&nbsp;</p>\r\n<p><font face="Helvetica">【名称】<br />\r\n仮面ライダー龍騎,Kamen Rider Ryuki,假面骑士龙骑,幪面超人龍騎</font></p>\r\n<p>&nbsp;</p>\r\n<p><font face="Helvetica">【介绍】<br />\r\n平成第三作，以镜世界为主题，假面骑士再不是英雄的代名词，而是欲望的追随者。作为13名假面骑士的一员，城户真司却是以保护人类为己任，这也引发与其他骑士间的一系列斗争&hellip;&hellip;（By yamilawliet）</font></p><br />\n</div>
'''

URL = 'https://share.dmhy.org/topics/list/page/3400'

# re_time = '<spanstyle="display:none;">([\s\S]*?)</span></td>'
# re_type = '<tdwidth="6%"align="center"><aclass="([\s\S]*?)"href="'
# # re_title = '<tdclass="title"><spanclass="tag"><ahref="([\s\S]*?)">([\s\S]*?)</a></span><ahref="([\s\S]*?)"target="_blank">([\s\S]*?)</a></td><tdnowrap="nowrap"align="center"><aclass="download-arrowarrow-magnet"title="'
# re_title = '<tdclass="title">([\s\S]*?)<ahref="([\s\S]*?)"target="_blank">([\s\S]*?)</a>([\s\S]*?)</td><tdnowrap="nowrap"align="center">'
# re_title = '<tdclass="title"><spanclass="tag"><ahref="([\s\S]*?)">([\s\S]*?)</a></span><ahref="([\s\S]*?)"target="_blank">([\s\S]*?)</a></td><tdnowrap="nowrap"align="center"><aclass="download-arrowarrow-magnet"title="'


re_infoURL = '<ahref="/topics/view/([\s\S]*?)"target="_blank">'
re_time = '<li>發佈時間:<span>([\s\S]*?)</span></li>'
re_type = '<tdwidth="6%"align="center"><aclass="([\s\S]*?)"href="'
re_title = '<divclass="topic-titleboxui-corner-all"><h3>([\s\S]*?)</h3>'
re_size = '<li>文件大小:<span>([\s\S]*?)</span></li>'
re_info = '<strong>簡介:&nbsp;</strong>([\s\S]*?)<a name="description-end"></a>'
re_magnet1 = '<aclass="magnet"id="a_magnet"href="([\s\S]*?)">([\s\S]*?)</a>'
re_magnet2 = '<aid="magnet2"href="([\s\S]*?)">([\s\S]*?)</a>'




_header = {
    'Referer':'https://share.dmhy.org/topics/list/sort_id/31/page/1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
def getDMHY_types(_str):
    '''
    动漫花园资源类别转换
    :param _str: 字符串，传入类似“sort-2”即可
    :return: 字符串
    '''
    types = {
        'sort-2':'动画',
        'sort-31':'季度全集',
        'sort-3':'漫画',
        'sort-41':'港台漫画',
        'sort-42':'日版漫画',
        'sort-4':'音乐',
        'sort-43':'动漫音乐',
        'sort-44':'同人音乐',
        'sort-15':'流行音乐',
        'sort-6':'日剧',
        'sort-7':'生肉（RAW）',
        'sort-9':'游戏',
        'sort-17':'电脑游戏',
        'sort-18':'电视游戏',
        'sort-19':'掌机游戏',
        'sort-20':'网络游戏',
        'sort-21':'游戏周边',
        'sort-12':'特摄',
        'sort-1':'其他',
        'viewInfoURL':'https://share.dmhy.org/topics/view/',
    }
    return types[_str]

def HtmlDownloader(URL,_header):
    _respone = requests.get(url=URL, headers=_header)
    return _respone.text

def re_DMHY(html_text,re_pattern,nbsp_del = True):
    '''
    增则过滤函数
    :param html_text: 字符串，网页的文本
    :param re_pattern: 字符串，正则表达式
    :param nbsp_del: 布尔值，控制是否以去除换行符的形式抓取有用信息
    :return:
    '''
    pattern = re.compile(re_pattern)
    if nbsp_del:
        return pattern.findall("".join(html_text.split()))
    else:
        return pattern.findall(html_text)

def main_DMHY():
    ha_hi_fu_he_ho = list(map(lambda x:getDMHY_types('viewInfoURL')+x,re_DMHY(HtmlDownloader(URL,_header),re_infoURL)))
    b = 0
    for ma_mi_mu_me_mo in ha_hi_fu_he_ho:
        ya_yu_yo = HtmlDownloader(ma_mi_mu_me_mo, _header)
        rec_dict = {
            # '标题':re_DMHY(ya_yu_yo, re_title)[0],
            # '发布时间':re_DMHY(ya_yu_yo, re_time)[0],
            '文件大小':re_DMHY(ya_yu_yo, re_size),
            # 'Magnet連接':list(re_DMHY(ya_yu_yo, re_magnet1)[0]),
            # 'Magnet連接typeII':list(re_DMHY(ya_yu_yo, re_magnet2)[0]),
            '简介':r'<div>\r\n'+re_DMHY(ya_yu_yo, re_info,False)[0],
            '详情URL':ma_mi_mu_me_mo,
        }
        print(rec_dict)



def BTchecker(URL,_header):
    _respone = requests.get(url=URL,headers=_header)
    # pattern_time = re.compile(re_time)
    # pattern_type = re.compile(re_type)
    # pattern_title = re.compile(re_title)
    pattern_info_url = re.compile(re_infoURL)
    # matchs_time = pattern_time.findall("".join(_respone.text.split()))
    # matchs_type = pattern_type.findall("".join(_respone.text.split()))
    # matchs_title = pattern_title.findall("".join(_respone.text.split()))
    matchs_infoURL = pattern_info_url.findall("".join(_respone.text.split()))
    # print("".join(_respone.text.split()))
    for i in matchs_infoURL[1:3]:
        # print(getDMHY_types(i))
        # print(i[2])
        # print(i)
        # print(len(i))
        _respone = requests.get(url=getDMHY_types('viewInfoURL')+i, headers=_header)
        print(_respone.text)
    print(matchs_infoURL)
    print(len(matchs_infoURL))

if __name__ == '__main__':
    # BTchecker(URL,_header)
    main_DMHY()