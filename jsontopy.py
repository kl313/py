import json
import requests
from faker import Faker
fake = Faker()
#with open('response.json', 'r', encoding='utf-8') as f:  #文件无需关闭
hds ={
'User-Agent':fake.user_agent(),
'authorization': 'Bearer %.%.%',
'x-user-geo': '104.310345,30.946448',
'user-agent':'okhttp/4.3.1'
}

url = 'https://phoenix.ujing.online/api/v1/stores/near?page=1&size=30&lat=%f&lont=%f&scope=2000&mode=BA h2'     #%f为位置坐标
r = requests.get(url, headers=hds)

 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(r.text)

lieb = data2['data']['storeList']   #列表
for n in range(30):  #遍历楼层
    for j in lieb[n]:
        if lieb[n]['id'] == '6039d48dd05d8b9662000020':
            print(n)    
            a1 = lieb[n]['storeInfo'][0]['access'] #【{}】
            floor = lieb[n]['name']
            print(f"{floor}可用洗衣机数量", a1)
            break


