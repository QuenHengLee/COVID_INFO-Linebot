import urllib.request as req
import bs4

url = "https://www.china-airlines.com/nz/zh/discover/news/travel-advisory/Immigration-Information"
request = req.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")

#篩出tbody
data_tbody = root.find_all('tbody')

#愈篩選出之國家
all_country=['日本','南韓','新加坡','馬來西亞','越南','泰國','菲律賓','印尼']

#用來存爬下來之"目的地"與"入境限制及檢疫規定"
data_country=[]
data_country_law=[]

#篩出tbody中每一個tr，存至data_tr(data_tr為一個二為陣列)
for tr in data_tbody:
    data_tr = tr.find_all('tr')


#篩出tr中每一個td，並依照style分出"目的地"與"入境限制及檢疫規定"，分別存至data_country(data_country為一個二為陣列)、data_country_law(data_country_law為一個二為陣列)
for td in data_tr:
    data_country.append(
        td.find_all(name = 'td', attrs = {"style":"width: 15%; text-align: center; vertical-align: top;"})
    )
    data_country_law.append(
        td.find_all(name = 'td', attrs = {"style":"width: 75%;"})
    )

#利用for迴圈比對data_country中國家那些是我們要的，我現在是print出來你可以執行看結果，爬下來的結果再看你要怎麼處理(補：中華航空沒有澳門)
for i in range(1,len(data_country)):
    for country in all_country:
        if data_country[i][0].get_text() == country:
            print(data_country[i][0].get_text())
            print(data_country_law[i][0].get_text())
        else:
            continue
            
    




