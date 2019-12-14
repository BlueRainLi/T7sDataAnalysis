# -*- coding:utf-8 -*-
import requests as re
import hmac
from Crypto.Cipher import AES
import json

header = {
    'Expect':'100-continue',
    'X-Unity-Version':'2018.4.5f1',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'174',
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 9; MI 8 Build/PQ3A.190801.002)',
    'Host':'api.t7s.jp',
    'Connection':'Keep-Alive',
    'Accept-Encoding':'gzip'
}

content2 = 'userRev=0&downloadType=1&ver=6.8.1&rev=0&ts=1576322461&os=android&blt=163&device=Android&platform=MI%208&osversion=9&jb=0&pid=3552916&sig=ZY12vXF9okjowYwFHzk3YDESc%252BI%253D'

url = 'https://api.t7s.jp/setup/resource/result'


test = re.post(url,data=content2,headers=header)

data = json.loads(test.text)

data2 = json.dumps(data)
with open('test/versionreport.json','w') as f:
    f.write(data2)
print(data['updateResource']['downloadConfig']['oneByOneDownloadPath'])