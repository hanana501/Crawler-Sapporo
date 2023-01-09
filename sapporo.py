from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np


# 設定字典
r_sapporo = {"en_name":[],"jp_name":[],
             "cuisine":[],"rating":[],
             "price":[],"url":[]}
# # 網址
# url = "https://tabelog.com/tw/rstLst/1/?maxLat=43.0706697&minLat=43.06570809999999&maxLon=141.35531265&minLon=141.34651085&lat=43.068188899999996&lon=141.35091175&zoom=17&RdoCosTp=2&LstCos=0&LstSitu=0&LstRev=0&LstReserve=0&ChkParking=0&LstSmoking=0"

#自訂函數
def get_page(url):
    # 發送請求
    web = requests.get(url)
    # 解析
    soup = BeautifulSoup(web.text,"lxml")
    # 欲搜尋區塊
    block = soup.find_all("li",class_="list-rst js-list-item")
    # 搜尋相關欄位資料及放入字典
    for row in block:
        en = row.find("a",class_="list-rst__name-main js-detail-anchor")
        jp = row.find("small",class_="list-rst__name-ja")
        group = row.find("li",class_="list-rst__catg")
        rating = row.find("b",class_="c-rating__val")
        price = row.find("span",class_="c-rating__val")
        net = en["href"]
        # print(en.text)
        # print(jp.text)
        r_sapporo["en_name"].append(en.text)
        r_sapporo["jp_name"].append(jp.text)
        r_sapporo["cuisine"].append(group.text)
        r_sapporo["rating"].append(rating.text)
        r_sapporo["price"].append(price.text)
        r_sapporo["url"].append(net)

#爬取多頁資料
for i in range(1,28):
    # 設定網址(找尋網址規律)
    url = "https://tabelog.com/tw/rstLst/"+str(i)+"/?maxLat=43.0706697&minLat=43.06570809999999&maxLon=141.35531265&minLon=141.34651085&lat=43.068188899999996&lon=141.35091175&zoom=17&RdoCosTp=2&LstCos=0&LstSitu=0&LstRev=0&LstReserve=0&ChkParking=0&LstSmoking=0"
    # 呼叫自訂函數
    get_page(url)
    # 列印目前讀取頁數
    print("第%d頁已讀取完畢" %i)
    # 間隔1秒
    time.sleep(1)
        
# 轉dataframe
df = pd.DataFrame(r_sapporo)

# 清理資料
# print('columns = ', file.columns)
# print(file["價位(日圓)"].value_counts())
df.replace("-", np.nan, inplace=True)
df.rating = df.rating.astype(float)
print(df.info())
df = df.dropna()
print(df.info())

# 另存csv檔
df.to_csv("r_sapporo.csv",encoding="utf-8",index=False)