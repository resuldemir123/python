import matplotlib.pyplot as plt
import numpy as np
"""
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y, "o--r")          # x ve y verilerini kırmızı (r), daire işaretli (o--), kesikli çizgi ile çiz.
plt.axis([0, 6, 0, 20])         # Grafik eksenlerini [xmin, xmax, ymin, ymax] olarak ayarla.

plt.title("Grafik Başlığı")     # Grafik başlığı.
plt.xlabel("x label")           # X ekseni etiketi.
plt.ylabel("y label")           # Y ekseni etiketi.
"""

"""
x = np.linspace(0, 2, 100)      # 0 ile 2 arasında 100 eşit aralıklı sayı üret.

plt.plot(x, x, label="linear")        # Doğrusal fonksiyon (y=x).
plt.plot(x, x**2, label="quadratic")  # Kuadratik fonksiyon (y=x^2).
plt.plot(x, x**3, label="cubic")      # Kübik fonksiyon (y=x^3).

plt.legend()                    # Grafiğe etiketleri gösteren bir legend ekle.
plt.title("Simple Plot")        # Grafik başlığı.
plt.show()                      # Grafiği ekranda göster.
"""


"""
x = np.linspace(0, 2, 100)      # 0 ile 2 arasında 100 eşit aralıklı sayı üret.
fig, axs = plt.subplots(3)      # Üç alt grafik oluştur.

axs[0].plot(x, x, color="red")       # İlk alt grafik: y=x.
axs[0].set_title("linear")           # İlk grafiğin başlığı.

axs[1].plot(x, x**2, color="green")  # İkinci alt grafik: y=x^2.
axs[1].set_title("quadratic")        # İkinci grafiğin başlığı.

axs[2].plot(x, x**3, color="yellow") # Üçüncü alt grafik: y=x^3.
axs[2].set_title("cubic")            # Üçüncü grafiğin başlığı.

plt.tight_layout()                   # Grafiklerin düzenli görünmesi için boşlukları optimize et.
"""

"""
x = np.linspace(0, 2, 100)      # 0 ile 2 arasında 100 eşit aralıklı sayı üret.
fig, axs = plt.subplots(2, 2)   # 2x2 düzeninde dört alt grafik oluştur.
fig.suptitle("Grafik Başlığı")  # Ana grafik başlığı.

axs[0, 0].plot(x, x, color="red")       # Birinci grafik: y=x (üst sol).
axs[0, 1].plot(x, x**2, color="brown")  # İkinci grafik: y=x^2 (üst sağ).
axs[1, 0].plot(x, x**3, color="blue")   # Üçüncü grafik: y=x^3 (alt sol).
axs[1, 1].plot(x, x**4, color="black")  # Dördüncü grafik: y=x^4 (alt sağ).
"""


import pandas as pd

df = pd.read_csv("nba.csv")                  # "nba.csv" dosyasını okuyarak bir DataFrame oluştur.
df = df.drop(["Number"], axis=1).groupby("Team").mean()  # "Number" sütununu sil, takımlara göre grupla ve ortalama al.
df.plot(subplots=True)                       # Her sütun için ayrı bir grafik oluştur.
plt.legend()                                 # Her grafikte bir açıklama kutusu göster.
plt.show()                                   # Grafiklerin ekranda gösterilmesi.

