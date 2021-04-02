import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

outcomes = []

for i in range(10000):
    flips = np.random.choice(['head', 'tail'], size=10, p=[0.5, 0.5])
    num_heads = np.sum(flips == 'head')
    outcomes.append(num_heads)

plt.hist(outcomes)
plt.show()

