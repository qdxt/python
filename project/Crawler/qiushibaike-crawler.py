#糗事百科爬虫实战

import requests
import re
res  = requests.get(url='https://www.qiushibaike.com')
content = res.text
# pattern = re.compile('<div content></div>',re.S)

# items = re.findall(pattern,content)

print(content,'hello')