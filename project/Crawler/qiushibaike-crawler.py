# #糗事百科爬虫实战
# #写个爬虫，
# # 需要深入了解re、urllib3、sqlite3、threading，Queue等几个模块。
# # 需要用上多线程抓取，正则表达式分析，并发资源控制，重新开启程序自动继续抓取和分析
import re
import urllib3
import certifi
from lxml import etree
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
res = http.request('GET','https://www.qiushibaike.com')

html = etree.HTML(res.data)
print(html)
result = etree.tostring(html)
print(result.decode('utf-8'))
# pattern = re.compile('<a>(.*?)<\/a>')
# result = res.data.decode()
# # resu = pattern.findall(result)
# print(pattern.findall(result))



