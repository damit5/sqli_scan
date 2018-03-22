"""
Author : d4m1ts
Version : 0.0.1

Search from yahoo.com
"""

import requests


from bs4 import BeautifulSoup

class Yahoo:
    def __init__(self,keyword,page_num=3):
        '''
        type    keyword : str
        param   keyword : keyword to search

        type    page_num : int
        param   page_num : pages what you want to search
        '''
        self.keyword = keyword
        self.page_num = page_num

    def yahoo(self):
        '''
        return type : generate
        return content : the links you want
        '''
        for first in range(self.page_num):
            url = 'https://ca.search.yahoo.com/search?p=%s&b=%d'%(self.keyword,first*10)
            headers = {'User-Agent':'"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"'}
            content = (requests.get(url,headers=headers).content.decode())
            soup = BeautifulSoup(content,'lxml')
            items = soup.findAll('span',class_=" fz-ms fw-m fc-12th wr-bw")
            #print (items)
            for item in items:
                item = item.get_text()
                if 'id=' in item:
                    if '&amp;' in item:
                        item = item.replace('&amp;','&')
                    if 'http' not in item:
                        item = 'http://' + item
                    yield item

if __name__ == '__main__':
    a = Yahoo('inurl:php?id=',3)
    for i in a.yahoo():
        print (i)
