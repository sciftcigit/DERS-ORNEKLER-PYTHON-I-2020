import numpy as np

dizi = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(dizi):
  print(x)
