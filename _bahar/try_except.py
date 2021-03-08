

try:
  print("aaaa")
except NameError:
  print("Name Error oldu ")
except :
  print("başka bir hata oluştu")
finally : 
  print("nihai olarak burası çalışacak")