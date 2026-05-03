import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

def decision_tree_plot(df):
        X = df[['Credit amount', 'Duration', 'Age', 'Installment rate in % income']]
        y = df['Risk']

        clf = DecisionTreeClassifier()
        clf.fit(X, y)

        plt.figure(figsize = (100,100))
        plot_tree(clf, feature_names=X.columns, class_names=['No Risk', 'Risk'], filled=True)
        plt.show()

def random_forest(df, size, random_state):
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = size, random_state = random_state)
        clf = RandomForestClassifier(n_estimators = 100, random_state = random_state)
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)
        score = clf.score(X_test, y_test)

        importances = clf.feature_importances_

        cm = confusion_matrix(y_test, y_pred)
        cost_matrix = (cm[0,1] * 1 + cm[1,0] *5)

        print(f'Score {round(score, 4) * 100}%, Misclassifications {cost_matrix}, Good when bad weighted: {cm[1,0] * 5} Bad when good weighted: {cm[0,1] * 1}')

        # score, cost matrix, good when bad, bad when good, importances
        return score, cost_matrix, {cm[1,0] * 5}, {cm[0,1] * 1}, importances

def forest_feature_importance(df, size, random_state):
    score,cost_matrix,neg_weight,pos_weight,importances = random_forest(df, size, random_state)
    attributes = list(range(len(importances)))

    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
    plt.bar(attributes, importances, color=bar_colors, edgecolor='g', align='center')
    plt.xlabel('Feature number')
    plt.ylabel('Importance')
    plt.title(f'Feature importance\nScore {round(score, 2) * 100}% Test {size} Random States 2^{round(np.log2(random_state))}')
    plt.show()


def forest_comparison(min_size, max_size, change_by, df):
    plt.figure(figsize=(10, 6))
    while min_size <= max_size:
        forrest_maps = []
        for i in range(16):
            forrest_maps.append(random_forest(df, min_size, 2 ** i))

        forest_scores = [item[0] for item in forrest_maps]
        forrest_cost = [item[1] for item in forrest_maps]
        forrest_iterations = list(range(len(forrest_maps)))

        plt.plot(forrest_iterations, forest_scores, alpha=0.6, label=f'Test size:{round(min_size * 100)}%\nMean:{round(np.mean(forest_scores) * 100, 2)}±{round(np.std(forest_scores ) * 100, 2)}\nCV:{round((np.std(forrest_cost) / np.mean(forrest_cost)) * 100, 2)}%')

        min_size = min_size + change_by

    plt.xlabel('2^n random state')
    plt.ylabel('Score')
    plt.title(f'Score vs Iterations')
    plt.legend(fontsize='x-small', loc='lower right')
    plt.show()
