# 天学网的小尝试哦

下载exe请至release页

> 高速下载链接 https://www.lanzous.com/i8wu8ha

> 慢速稳定下载 https://github.com/1299172402/up366/releases


## 目标1

- [x] 登录

请求头

```
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Length: 61
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Cookie: acw_tc=7b39758215802092127684930e1234175f6acbea06d4bbf933eca866daecde; BIGipServercn_liveclass-api_pool=2467735744.38175.0000; SESSION=301df37e-80f0-4372-b3a1-2ab37363de0e
DNT: 1
Host: live-api.up366.cn
Origin: http://me.up366.cn
Referer: http://me.up366.cn/center/student/course/liveclasses.html?courseId=89440&createTime=undefined
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
X-Requested-With: XMLHttpRequest
```

简化后

```
{
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
	"Host": "live-api.up366.cn",
	"Origin": "http://me.up366.cn",
	"Referer": "http://me.up366.cn/center/student/course/liveclasses.html?courseId=89440&createTime=undefined",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
	"Cookie": "acw_tc=7b39758215802092127684930e1234175f6acbea06d4bbf933eca866daecde; BIGipServercn_liveclass-api_pool=2467735744.38175.0000; SESSION=301df37e-80f0-4372-b3a1-2ab37363de0e"
}
```

***

## 目标2

- [X] 下载直播课视频

目前已经获取 直播课名称，时间，下载地址 并导出为csv

现在可以完成了，还增加了科目筛选功能

## 目标3 

英语听力自动提交(但其实不是很想做)

1. 选择课程
2. 选择分数
3. 提交

23333，就一个想法吧，这个还是不要实现了
