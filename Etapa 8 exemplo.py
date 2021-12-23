import matplotlib.pyplot as plt

eixo_x = [1872, 1890, 1900, 1920, 1940, 1950, 1960, 1970, 1980, 1991, 2000, 2010]
eixo_y = [9.9, 14.3, 17.4, 30.6, 41.1, 51.9, 70, 93.1, 119, 146.8, 169.8, 190.75]
plt.plot(eixo_x, eixo_y)
plt.xlabel('Ano')
plt.ylabel('População residente no Brasil (milhões)')
plt.title('Censos realizados no Brasil (1872-2010)')
plt.show()