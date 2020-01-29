import requests
from bs4 import BeautifulSoup
import urllib.request
from lxml import html
import json
import time
import datetime
import csv
import os
import urllib

def show(i,s):
	os.system('cls')
	print('\n\n')
	print('####### 天学网直播课下载程序 #######\n')
	print('{0:5} | {1:15} | {2:15} | {3:15}'.format('##序号##','#### 课程时间 #####','####### 下载地址 ############################','####### 课程名称 #####################'))
	if s == '':s = 'abcdefghijk'
	j=1
	while j<=10 and i>=0:
		i = i-1
		if s.find(list1[i][3])!=-1:
			print('{3:8} | {0:20}| {1:15} | {2:15}'.format(list1[i][1],list1[i][2],list1[i][0],i))
			j = j+1

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' % per)

def subject(a):
	if a.find('数学') !=-1 :return 'b'
	if a.find('英语') !=-1 :return 'c'
	if a.find('物理') !=-1 :return 'd'
	if a.find('化学') !=-1 :return 'e'
	if a.find('生物') !=-1 :return 'f'
	if a.find('政治') !=-1 :return 'g'
	if a.find('历史') !=-1 :return 'h'
	if a.find('地理') !=-1 :return 'i'
	if a.find('技术') !=-1 :return 'j'
	return 'k'

# 欢迎文字
print('\n\n')
print('####### 天学网登录程序 #######\n')
# print('Author~~')
print('Jellow 看见我请一定一定叫我学习')
print('Creative By ZhiyuShang With Love\n')
# print('Thanks for being addicted')
print('')


print('测试获取直播课列表\n')
print('出现我校直播课名称即为获取成功\n')


cookie = input('请输入cookie\n')
if cookie =='' : cookie =  'acw_tc=65c86a0b15802051020836696ec67d6265a32efaf57f7f51f7f1004b74527a; BIGipServercn_liveclass-api_pool=2434181312.38175.0000; SESSION=a98a53c8-0310-4aba-afa6-9016db13cd41'

# 记得要常改cookie
headers = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	'Host': 'live-api.up366.cn',
	'Origin': 'http://me.up366.cn',
	'Referer': 'http://me.up366.cn/center/student/course/liveclasses.html?courseId=89440&createTime=undefined',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
	'Cookie': cookie
}

body = {
	'courseId': '89440',
	'pager.currentPage': '1',
	'pager.pageSize': '500',
	'status': '0'
}



# 获取json
play_url = 'http://live-api.up366.cn/client/liveclass/list'
s = requests.session()
response = s.post(play_url, headers=headers,data=body).content
s = BeautifulSoup(response, 'lxml')
s = s.find('p').text

# 把json转化为python对象
s = json.loads(s)

if s['result']['msg'] != 'success':
	print('登录失败')
	input('按Enter退出')
	exit()
else:
	print('登录成功')
	print('正在加载中。。。')
time.sleep(3)

os.system('cls')
time.sleep(1)


# 简化数据
course = s['data']['list']
#print(course)

list1 = []
for video in course:
	vodUrl = 'http://fs.up366.cn/download/' + video['vodUrl']
	# print(vodUrl)
	# 注意那个ms 到 s ，坑了好久
	timeStamp = int(video['updateTime'])/1000
	# print(timeStamp)
	timeArray = time.localtime(timeStamp)
	updateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	name = video['lcName']
	####subject(name)
	# print(updateTime)
	list1.append([video['lcName'],updateTime,vodUrl,subject(name)])

#print(list1)

# 欢迎文字
print('\n\n')
print('####### 天学网直播课下载程序 #######\n')
#print('####### 课程名称 #######|####### 课程时间 #######|####### 下载地址 #######')


i = len(list1)
s = ''

show(i,s)

while 1<2:
	ch = input('N键上翻，M键下翻，D键下载，X键筛选学科，Q键退出，S键刷新：')
	if ch == 'S' or ch == 's' : show(i,s)
	if ch == 'Q' or ch == 'q' : exit()
	if ch == 'N' or ch == 'n' : 
		if i>=len(list1) : print ('已到首页')
		else:
			os.system('cls')
			time.sleep(1)
			i=i+10
			show(i,s)
	if ch == 'M' or ch == 'm' : 
		if i<=0 : print ('已到末页')
		else:
			i=i-10
			os.system('cls')
			time.sleep(1)
			show(i,s)
	if ch == 'D' or ch == 'd' :
		print('\n使用说明：')
		print('\n1.所有直播课下载地址将写入E:/txw.csv')
		print('2.多段的视频目前只能下载一段，你可以手动下载\n')
		with open("E:/txw.csv",'w',newline='') as t:
			writer=csv.writer(t)
			writer.writerows(list1) 
		num = int(input('请输入要下载的视频序号：'))
		url = list1[num][2]
		name = list1[num][0]
		try:
			print('正在下载', name)
			time.sleep(1)
			#local = os.path.join('E:/','%s' % name + '.mp4')
			urllib.request.urlretrieve(url, 'E:/'+'%s' % name + '.mp4',Schedule)
			print('下载成功，位置'+'E:/'+'%s' % name + '.mp4')
		except:
			print('下载失败')
	if ch == 'X' or ch == 'x':
		print('语a 数b 英c 物d 化e 生f 政g 史h 地i 技j 其他k 取消筛选l')
		c = input('请输入代号（可多个）：')
		if c=='l' :s=''
		else:
			s = s+c
		show(i,s)




# pyinstaller --onefile --nowindowed --icon=" D:\Queena\PyCharmProjects\dist1\computer_three.ico" guess_exe.py


'''
# 写入csv
print('将写入E:/txw.csv')
with open("E:/txw.csv",'w',newline='') as t:
	writer=csv.writer(t)
	writer.writerows(list1) 
'''









