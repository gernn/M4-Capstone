import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pas_readings = pd.read_csv("pas_torque.csv", delimiter=",")

plt.figure()
sns.scatterplot(data=pas_readings, x="TIME", y='TORQUE', alpha=0.3)
plt.figure()
sns.scatterplot(data=pas_readings, x="TIME", y="PASD", alpha=0.3)
sns.scatterplot(data=pas_readings, x="TIME", y="PASP", alpha=0.3)
plt.show()
