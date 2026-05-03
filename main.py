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
df_numerical = pd.read_csv('german.data-numeric', sep=r'\s+', header=None)

cluster_plot(df)
decision_tree_plot(df)


forest_comparison(0.20, 0.40, 0.05, df_numerical)
forest_comparison(0.25, 0.35, 0.01225, df_numerical)

forest_feature_importance(df_numerical, 0.35, 2**8)
forest_feature_importance(df_numerical, 0.32, 2**8)
forest_feature_importance(df_numerical, 0.25, 2**7)