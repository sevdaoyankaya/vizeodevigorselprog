# Soru 2.
# string func. kullanilmayacagi icin regular expression kullanildi.
import re

exp = '^(http[s]?:\/\/)?([w]{3}\.)?[a-z0-9\._-]+[.]\w{2,3}([.]\w{2})?$'
def validateURL(url):
    if (re.search(exp, url)):
    	print("URL doğrulandı")
    else: 
    	print("URL hatalı!")

validateURL("www.alierbey")