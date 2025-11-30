import sklearn as sk
import pandas as pd

# Load iris dataset directly using sk
iris = sk.datasets.load_iris()
print("Class Names:", iris.target_names)  # class directly printed from data

# X, y without separate import
X, y = sk.datasets.load_iris(return_X_y=True)

# Splitting dataset using sk
X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(
    X, y, test_size=0.30
)

# Converting into dataframe
data = pd.DataFrame({
    'sepallength': iris.data[:, 0],
    'sepalwidth': iris.data[:, 1],
    'petallength': iris.data[:, 2],
    'petalwidth': iris.data[:, 3],
    'species': iris.target
})

print(data.head())

# RandomForest using sk
clf = sk.ensemble.RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Predictions + Accuracy
y_pred = clf.predict(X_test)
print("ACCURACY OF THE MODEL =", sk.metrics.accuracy_score(y_test, y_pred))

# Predict unknown point
print("Prediction:", clf.predict([[3, 3, 2, 2.37]]))
