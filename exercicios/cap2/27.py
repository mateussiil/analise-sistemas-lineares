import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(-1000,1000,1)
y = []
for i in t:
  try:
    h = i*(i-1) + abs(i) + math.cos(1 + 2*i)
  except:
    h = i + abs(i) + math.cos(1 + 2*i)
  y.append(h)

print(y)
plt.plot(t, y)
plt.show()