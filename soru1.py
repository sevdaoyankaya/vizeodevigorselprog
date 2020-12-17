# Soru 1.
# string func. kullanilmayacagi icin regular expression kullanildi.
import re

exp = '^[a-z0-9\._]+[@]\w+[.]\w{2,3}([.]\w{2})?$'
def validateEMail(eMail):
    if (re.search(exp, eMail)):
    	print("E-Posta adresi doğrulandı")
    else: 
    	print("E-Posta adresi hatalı!")

validateEMail("ali.erbey@usak.edu.tr")