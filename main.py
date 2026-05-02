import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from maps import *
from cluster import *
from tree import *


pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 24)

df = pd.read_csv('german.data', sep=r'\s+', header=None, names=headers)

map_codes(df)
cluster_plot(df)
decision_tree_plot(df)