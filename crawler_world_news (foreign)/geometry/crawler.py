class Crawler :
    def __init__(self,url): #初始化並把要連線的網址傳進來
        self.url=url
        self.data = None    #data是存最一開始所抓到的html
        import urllib.request as req
        request = req.Request(self.url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        })
        with req.urlopen(request) as response:
            self.data=response.read().decode("utf-8")
    def anaylis(self,label,name):   #分析剛剛所抓下來的html檔，label是想搜尋的標籤，name是標籤名稱(class)
        import bs4
        root=bs4.BeautifulSoup(self.data,"html.parser")
        titles=root.find_all(label,class_=name)
        return titles


