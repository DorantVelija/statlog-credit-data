import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

def decision_tree_plot(df):
    X = df[['Credit amount', 'Duration', 'Age', 'Installment rate in % income']]
    y = df['Risk']

    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    plt.figure(figsize = (100,100))
    plot_tree(clf, feature_names=X.columns, class_names=['No Risk', 'Risk'], filled=True)
    plt.show()