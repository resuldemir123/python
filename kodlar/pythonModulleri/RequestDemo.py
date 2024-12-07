import request 
import json

api_key="4ae7e1f5f00fac753e94e79e"
api_url=f"https://v6.exchangerate-api.com/{api_key}/latest/"

bozulan_doviz=input("Bozulan dözviz türü:") #   usd
alianan_döviz=input("Alinan döviz türü:") # try
miktar=input(f"Ne kadar{bozulan_doviz} bozdurmak istiyorsun:")

sonuc=request.get(api_url + bozulan_doviz)
sonuc=json.loads(sonuc.text())
#print(sonuc_json("conversetion_rates")[alianan_döviz])

print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc.json["converseion_rates"][alianan_döviz],alianan_döviz))