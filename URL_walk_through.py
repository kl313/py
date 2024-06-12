import requests
from time import sleep
l=[]
for x in range(300,400):
    url=f"http://39.134.217.27/wh7f454c46tw954775492_1289827739/iptv.cdn.ha.chinamobile.com/PLTV/88888888/224/3221226{x}/1.m3u8"

    re=requests.get(url)
    if(re.status_code==200):
        l.append(x)
    sleep(0.1)
print(l)

