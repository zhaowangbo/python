import torch
from torch.nn import functional as F
import numpy as np


x = np.array([[1, 2],
              [2, 1],
              [1, 2],
              [1, 2],
              [2, 1],
              [1, 2]]).astype(np.float32)
y = np.array([1, 1, 0, 1, 0, 0])
x = torch.from_numpy(x)
y = torch.from_numpy(y).long()

print(x.shape)
print(y.shape)
print(x)
print(y)
loss = F.cross_entropy(x, y)
print(loss)