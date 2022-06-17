import json
from numpy import size
import requests
def req(size=10,lat=30.946805,lont=104.308798):
    hds = {
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjAwMTY3MTYsIm5hbWUiOiIxMzc4MzUzMTU5MCIsImFwcFVzZXJJZCI6MTQzMDM3MDcsImlhdCI6MTY1NTQ2OTgwOSwiZXhwIjoxNjYzNTA1MDA5fQ.ZfC6FX1z2DfitzqezRu_gWhCZPwILhKDdpaIKcdDf9g'
    }

    url = f'https://phoenix.ujing.online/api/v1/stores/near?page=1&size={size}&lat={lat}&lont={lont}&scope=2000&mode=BA' 
    r = requests.get(url, headers=hds)
    return r.text

def filew():
    f = open('uc.json','w')
    f.write(req())
    f.close()

# 将 JSON 对象转换为 Python 字典
filew()
size=10
with open('uc.json','r') as js:
    data2 = json.loads(js.read())

    lieb = data2['data']['storeList']  # 列表
    for n in range(size):  # 遍历楼层
        for j in lieb[n]:
            if lieb[n]['id'] == '6039d48dd05d8b9662000020':
                print(n)
                a1 = lieb[n]['storeInfo'][0]['access']  # 【{}】
                floor = lieb[n]['name']
                print(f"{floor}可用洗衣机数量", a1)
                break
