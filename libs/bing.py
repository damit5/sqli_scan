"""
Author : d4m1ts
Version : 0.0.1

Search from www.bing.com
"""

import requests
import re

class Bing:
    def __init__(self,keyword,page_num=3):
        '''
        type    keyword : str
        param   keyword : keyword to search

        type    page_num : int
        param   page_num : pages what you want to search
        '''
        self.keyword = keyword
        self.page_num = page_num

    def bing(self):
        '''
        return type : list
        return content : the links you want
        '''
        for first in range(self.page_num):
            url = 'https://www.bing.com/search?q=%s&first=%d'%(self.keyword,first*10)
            headers = {'User-Agent':'"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"'}
            content = (requests.get(url,headers=headers).content.decode())
            regex = '<h2>.*?href="(http.*?)".*?</h2>'
            items = (re.findall(regex,content))
            for item in items:
                if 'id=' in item:
                    if '&amp;' in item:
                        item = item.replace('&amp;','&')
                    #links.append(item)
                    yield item
