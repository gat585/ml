import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
y = pd.DataFrame(iris.target, columns=['target'])

scaler = preprocessing.StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

gmm = GaussianMixture(n_components=3)
gmm.fit(X_scaled_df)
gmm_labels = gmm.predict(X_scaled_df)

plt.figure(figsize=(14, 14))
colormap = np.array(['red', 'green', 'blue'])

plt.subplot(2, 2, 1)
plt.scatter(
    X['petal_length'],
    X['petal_width'],
    c=colormap[y['target']],
    s=40
)
plt.title("Real Clusters")
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.subplot(2, 2, 2)
plt.scatter(
    X['petal_length'],
    X['petal_width'],
    c=colormap[gmm_labels],
    s=40
)
plt.title("GMM Clustering (EM Algorithm)")
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.tight_layout()
plt.show()
