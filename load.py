import requests
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
etree = html.etree

# 欢迎文字
print('\n\n')
print('####### 天学网登录程序 #######\n')
# print('Author~~')
print('Jellow 看见我请一定一定叫我学习')
print('Creative By ZhiyuShang With Love\n')
# print('Thanks for being addicted')
print('')


headers = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	'Host': 'live-api.up366.cn',
	'Origin': 'http://me.up366.cn',
	'Referer': 'http://me.up366.cn/center/student/course/liveclasses.html?courseId=89440&createTime=undefined',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
	'Cookie': 'acw_tc=7b39758215802092127684930e1234175f6acbea06d4bbf933eca866daecde; BIGipServercn_liveclass-api_pool=2467735744.38175.0000; SESSION=301df37e-80f0-4372-b3a1-2ab37363de0e'
}


print('测试获取直播课列表\n')
print('出现我校直播课名称即为获取成功\n')


play_url = 'http://live-api.up366.cn/client/liveclass/list'
s = requests.session()
response = s.get(play_url, headers=headers).content
s = BeautifulSoup(response, 'lxml')

print(s)