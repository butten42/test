# -*- coding: cp936 -*-
#��ȡ��Ѹ����Ʒ��Ϣ
import urllib2
from bs4 import BeautifulSoup
def get_yixun(id):
    price_origin,price_sale = '0','0'
    url = 'http//:item.yixun.com/item-' + id + '.html'
    html=urllib2.urlopen(url).read().decode('utf-8')
    soup=BeautifulSoup(html)
    title=unicode(soup.title.text.strip().strip(u'���۸�_����_ͼƬ_���顿-��Ѹ��').replace(u'��','')),encode('utf-8').decode('utf-8'))
    print title
    try:
        soup_origin=soup.find("dl",{'class':'xbase_item xprice xprice_origin'})
        price_origin=soup_origin.find("span",{"class":"mod_price xprice_val"}).contents[1].text
        print u'ԭ��:'+price_origin

    except:
        pass
    try:
        soup_sale=soup.find('dl',{'class':'xbase_item xprice'})
