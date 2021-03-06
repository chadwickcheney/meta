import time
import requests
import fake_useragent

class Browser:
    def __init__(self, url):
        self.url = url
        self.headers={'User-Agent':str(self.get_random_user_agent())}
        self.response=self.get_response(self.url)
        self.html=BeautifulSoup(self.page.text, 'lxml.parser')

    def get_random_user_agent(self):
        ua = fake_useragent.UserAgent()
        return ua.random

    def get_response(self,url):
        while True:
            resp = requests.get(self.url, headers=self.headers)
            try:
                return resp
            except Exception as e:
                user.prompt(feed=e)
            time.sleep(2)
        user.prompt(feed=str("Response acquired successfully with "+str(self.headers)))

#def test():
#    url = 'http://www.ichangtou.com/#company:data_000008.html'
#    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#    response = requests.get(url, headers=headers)
#    print(response.content)
