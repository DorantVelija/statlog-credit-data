import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# pd.set_option('display.width', 1000)
# pd.set_option('display.max_columns', 24)
#
# df = pd.read_csv('german.data', sep=r'\s+', header=None, names=headers)
# map_codes(df)
#
#
# plt.scatter(df['Age'], df['Credit amount'], c=df['Risk'], s=df['Age'])
# plt.xlabel('Age')
# plt.ylabel('Credit amount')
# plt.colorbar(label="Risk")
#
# plt.show()

def cluster_plot(df):
    X = df[['Credit amount', 'Duration']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    risk_analysis = pd.crosstab(df['Cluster'], df['Risk'])
    print(risk_analysis)

    plt.scatter(df['Duration'], df['Credit amount'], c=df['Cluster'], s=df['Installment rate in % income']*100, alpha=0.7, edgecolor='w')
    plt.xlabel('Duration')
    plt.ylabel('Credit amount')
    plt.title('Credit amount vs Duration \nRisk analysis')

    plt.text(20, 16000, f'DANGER ZONE\n{round(abs(risk_analysis.loc[0, 2] / (risk_analysis.loc[0, 1] + risk_analysis.loc[0, 2])) * 100, 0)}% Default Rate', bbox=dict(facecolor='red', alpha=0.5), fontsize=10, fontweight='bold')

    plt.text(10, 2000, f'SAFE CORE\n{round(abs(risk_analysis.loc[1, 2] / (risk_analysis.loc[1, 1] + risk_analysis.loc[1, 2])) * 100, 0)}% Default Rate', bbox=dict(facecolor='green', alpha=0.5), fontsize=10, fontweight='bold')

    plt.text(40, 7000, f'GRAY AREA\n{round(abs(risk_analysis.loc[2, 2] / (risk_analysis.loc[2, 1] + risk_analysis.loc[2, 2])) * 100, 0)}% Default Rate', bbox=dict(facecolor='orange', alpha=0.5), fontsize=10, fontweight='bold')

    plt.colorbar(label="Cluster")

    plt.show()