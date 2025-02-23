import matplotlib.pyplot as plt

# Örnek veri seti
veri = [12, 15, 14, 19, 20, 18, 22, 24, 25, 30, 35]

# Histogram çizimi
plt.hist(veri, bins=5, color='blue', edgecolor='black')
plt.title('Histogram Örneği')
plt.xlabel('Değer Aralıkları')
plt.ylabel('Frekans')
plt.show()
