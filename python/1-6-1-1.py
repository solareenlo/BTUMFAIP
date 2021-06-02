import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0, color='b', ls='-', lw=0.5) # x 軸 (直線 x=0)
plt.axvline(0, color='b', ls='-', lw=0.5) # y 軸 (直線 y=0)
x = np.linspace( -4, 3, 70)   # linspace(min, max, N) で範囲 min から max を N 分割します
y = 3 ** x

plt.plot(x, y)
plt.show()
