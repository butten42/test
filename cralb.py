# -*- coding: cp936 -*-
#爬取易迅网商品信息
import urllib2
from bs4 import BeautifulSoup
def get_yixun(id):
    price_origin,price_sale = '0','0'
    url = 'http//:item.yixun.com/item-' + id + '.html'
    html=urllib2.urlopen(url).read().decode('utf-8')
    soup=BeautifulSoup(html)
    title=unicode(soup.title.text.strip().strip(u'【价格_报价_图片_行情】-易迅网').replace(u'】','')),encode('utf-8').decode('utf-8'))
    print title
    try:
        soup_origin=soup.find("dl",{'class':'xbase_item xprice xprice_origin'})
        price_origin=soup_origin.find("span",{"class":"mod_price xprice_val"}).contents[1].text
        print u'原价:'+price_origin

    except:
        pass
    try:
        soup_sale=soup.find('dl',{'class':'xbase_item xprice'})
