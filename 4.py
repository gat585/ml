# 1️⃣ Import libraries
import pandas as pd                # For reading and handling datasets (tables)
import sklearn as sk               # ML library (all models, metrics, and tools under 'sk')
import matplotlib.pyplot as plt    # For plotting graphs and visualizations

# 2️⃣ Load dataset
pima = pd.read_csv("diabetes.csv")  
# pd.read_csv() → Reads a CSV file and converts it into a DataFrame (table)
# 'pima' → Variable storing the whole dataset

# 3️⃣ Select features (inputs) and target (output)
feature_cols = [
    'Pregnancies', 
    'Insulin', 
    'BMI', 
    'Age', 
    'Glucose',
    'BloodPressure',
    'DiabetesPedigreeFunction'
]  # These are the column names we will use as input features

X = pima[feature_cols]  # Extract the input features from the DataFrame
y = pima['Outcome']     # Extract the target variable (0 = No Diabetes, 1 = Diabetes)

# 4️⃣ Split dataset into training and testing sets
X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(
    X, y, test_size=0.3, random_state=0
)
# train_test_split() → Splits data into train and test sets
# X_train, y_train → Data used to train the model
# X_test, y_test → Data used to test the model’s accuracy
# test_size=0.3 → 30% of data for testing
# random_state=0 → Ensures reproducible results

# 5️⃣ Create and train the Decision Tree model
clf = sk.tree.DecisionTreeClassifier()  # Initialize a Decision Tree classifier
clf = clf.fit(X_train, y_train)         # Train the model using training data
# fit() → Learns patterns from the input features and target

# 6️⃣ Make predictions on test data
y_pred = clf.predict(X_test)  
# predict() → Uses the trained model to predict outcomes for given inputs

# 7️⃣ Evaluate model accuracy
accuracy = sk.metrics.accuracy_score(y_test, y_pred)
# accuracy_score() → Compares predicted values (y_pred) with true values (y_test) to calculate accuracy
print("Accuracy:", accuracy)

# 8️⃣ Predict on a new single sample
new_sample = pd.DataFrame({
    'Pregnancies': [2],
    'Insulin': [100],
    'BMI': [30],
    'Age': [25],
    'Glucose': [100],
    'BloodPressure': [70],
    'DiabetesPedigreeFunction': [0.57]
})
# pd.DataFrame() → Creates a table from given data, needed for sklearn predict()

prediction = clf.predict(new_sample)[0]  
# clf.predict() → Returns the predicted label (0 or 1)
# [0] → Extract the single prediction from the returned array

if prediction == 1:
    print("The new sample is predicted to have diabetes (label = 1)")
else:
    print("The new sample is predicted to not have diabetes (label = 0)")

# 9️⃣ Visualize the trained Decision Tree
  # Set size of the plot
sk.tree.plot_tree(
    clf,
    feature_names=feature_cols,             # Names of input features for labeling nodes
    class_names=['No Diabetes', 'Diabetes'], # Class labels for tree nodes
    filled=True                             # Color nodes based on class
)
plt.show()  # Display the tree
