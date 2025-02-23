import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 9, 20)  # -10 ile 9 arasında 20 eşit aralıklı sayı oluştur.
y = x**3                     # x'in küpü olan y değerleri.
z = x**2                     # x'in karesi olan z değerleri.


"""
figure = plt.figure()

axes = figure.add_axes([0.1, 0.1, 0.9, 0.9])  # Büyük grafik için alan belirlenir.
axes.plot(x, y, 'b')                          # Büyük grafikte x ve y çizilir (mavi renk).
axes.set_xlabel("X Axis")
axes.set_ylabel("Y Axis")
axes.set_title("Cube")

axes2 = figure.add_axes([0.15, 0.6, 0.15, 0.3])  # Küçük grafik için alan belirlenir.
axes2.plot(x, z, 'r')                            # Küçük grafikte x ve z çizilir (kırmızı renk).
axes2.set_xlabel("X Axis")
axes2.set_ylabel("Y Axis")
axes2.set_title("Square")
"""


"""
figure = plt.figure()

axes = figure.add_axes([0, 0, 1, 1])  # Tam boyutlu bir grafik alanı oluşturulur.
axes.plot(x, z, label="Square")       # x ve z verileri çizilir, "Square" etiketi eklenir.
axes.plot(x, y, label="Cube")         # x ve y verileri çizilir, "Cube" etiketi eklenir.
axes.legend(loc=2)                    # Legend (açıklama kutusu) sol üst köşeye yerleştirilir.
"""


fig, axes = plt.subplots(nrows=2, ncols=1)  # 2 satır ve 1 sütundan oluşan alt grafikler oluşturulur.

axes[0].plot(x, y)              # İlk alt grafik: x ve y verileri çizilir.
axes[0].set_title("Cube")       # İlk grafiğin başlığı ayarlanır.

axes[1].plot(x, z)              # İkinci alt grafik: x ve z verileri çizilir.
axes[1].set_title("Square")     # İkinci grafiğin başlığı ayarlanır.

plt.tight_layout()              # Grafiklerin düzenlemesi için boşluklar optimize edilir.
fig.savefig("figure1.png")      # Grafikler "figure1.png" olarak kaydedilir.

plt.show()                      # Grafiklerin ekranda gösterilmesi sağlanır.
