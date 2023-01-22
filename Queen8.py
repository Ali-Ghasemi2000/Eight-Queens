import random as rn

rows = list(range(1, 9))
k = 0
n = 1000

while k<n:
    c = [0] * 8
    r = rows.copy()
    for i in range(8):
        r = rows.copy()
        for j in range(i):
            y = c[j]
            if y in r:
                del r[r.index(y)]
            d = i-j
            if (y - d) in r:
                del r[r.index(y - d)]
            if (y + d) in r:
                del r[r.index(y + d)]
        if r == []:
            break
        x = rn.choice(r)
        c[i] = x
    if 0 not in c:
        break
    k += 1
if 0 in c:
    flag = -1
else:
    flag = 1
print(c, '\n', 'optimal? = ', flag, '\n', 'nth iteration = ', k)

# ---------- Visualization ----------

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

mat = np.zeros((8,8))
for i in range(8):
    mat[c[i]-1, i] = 1
f = sns.heatmap(mat, linewidths=.5, cbar=False)
f.set(xticklabels=[])
f.set(yticklabels=[])

plt.show()
