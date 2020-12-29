import datetime

bugun = datetime.datetime.now()
print (bugun)

print ( " Ülkemize göre biçimlendirilmiş hali : " + bugun.strftime("%d.%m.%Y") ) 
