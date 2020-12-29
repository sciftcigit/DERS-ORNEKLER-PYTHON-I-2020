# module kulladık
# geometri. py dosyasını çağırıyoruz. 
import geometri as ge

r = input("Yarıçap giriniz: ")
islem = input("işlem  (çevre için 'ç' alan için 'a' giriniz: ")

if (islem == "ç") : 

    sonuc = ge.cevreHesapla(r)
    print(" Sonuç : " + str(sonuc))

elif (islem == "a") : 

    sonuc = ge.alanHesapla(r)
    print(" Sonuç : " + str(sonuc))

else :
    
    print(" Geçerli bir işlem seçmediniz! ")

