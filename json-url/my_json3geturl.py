import requests, json

url = 'https://reactnative.dev/movies.json'

webTalep = requests.get(url)

# print(webTalep.text)


veri = json.loads(webTalep.text)

# print("Başlık :" + veri["title"])
# print("Açıklama :" + veri["description"])

filmler = veri["movies"]

print("Toplam film sayısı :" + str(len(filmler)))

for satir in filmler:
  print("Film Adı : " + satir['title'] + " Yıl: " + satir['releaseYear'])

