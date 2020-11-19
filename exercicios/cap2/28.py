import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(-100,100,1)
y = []
print(sum(t))

for i in t:
  y.append(math.cos(i))

print(sum(y))
plt.plot(t, 2*1*1)
plt.show()