import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

acd = pd.read_excel("C:\\Users\\korad\\Desktop\\python examples\\modules\\seaborn\\Academic.xlsx")

sns.countplot(x='Roll No.',data=acd)


