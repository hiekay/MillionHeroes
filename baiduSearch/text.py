import urllib.request,time,_thread,urllib.parse

class Ai:
    
    def __init__(self,issue,answer): # 注意前后各两个下划线
        self.start = time.time()
        self.issue = issue
        self.answer = answer
        self.a = 0
        self.b = 0
        self.c = 0
        self.count = 0
        
    def gethtml(self,url):
     headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

     opener = urllib.request.build_opener()
     opener.addheaders = [headers]
     date = opener.open(url).read()
     
     if "zhidao.baidu.com" in url:
        str1=str(date,"gbk")
     else:
        str1=str(date,"utf-8")


     self.count += 1
     self.a += str1.count(self.answer[0])
     self.b += str1.count(self.answer[1])
     self.c += str1.count(self.answer[2])
     
    def threhtml(self,url):
        _thread.start_new_thread(self.gethtml,(url,))

    def search(self):
        
  
         #baidu = self.threhtml("https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word="+urllib.parse.quote(self.issue))

         sousou = self.threhtml("http://wenwen.sogou.com/s/?w="+urllib.parse.quote(self.issue)+"&ch=ww.header.ssda")

         iask = self.threhtml("https://iask.sina.com.cn/search?searchWord="+urllib.parse.quote(self.issue)+"&record=1")

         so360 = self.threhtml("https://wenda.so.com/search/?q="+urllib.parse.quote(self.issue))

    
         print ("Error: 无法启动线程")

         while 1:
           if(self.count == 3):
               break

        #str1=str(iask,"utf-8")

         print('A' + str(self.a))
         print('B' + str(self.b))
         print('C' + str(self.c))

         end = time.time()
         print('程序用时：'+str(end-self.start)+'秒')
