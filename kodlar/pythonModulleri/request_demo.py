import requests
import json

api_key = "4ae7e1f5f00fac753e94e79e"
base_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü: ").upper()  # USD
alinan_doviz = input("Alınan döviz türü: ").upper()  # TRY
miktar = float(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsun? "))

# API'den döviz kurlarını çek
response = requests.get(base_url + bozulan_doviz)

if response.status_code == 200:
    data = response.json()
    if alinan_doviz in data["conversion_rates"]:
        kur = data["conversion_rates"][alinan_doviz]
        sonuc = miktar * kur
        print(f"1 {bozulan_doviz} = {kur} {alinan_doviz}")
        print(f"{miktar} {bozulan_doviz} = {sonuc:.2f} {alinan_doviz}")
    else:
        print("Hata: Alınan döviz türü geçersiz!")
else:
    print("Hata: API'den veri alınamadı!")
