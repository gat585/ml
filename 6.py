import numpy as np
import pandas as pd

data = pd.read_csv("enjoysport.csv")
df = pd.DataFrame(data)

prior_prob_yes = (df['EnjoySport'] == "Yes").mean()
prior_prob_no  = (df['EnjoySport'] == "No").mean()

print("\nPrior Probabilities (Before seeing any feature):")
print("P(EnjoySport = Yes) =", prior_prob_yes)
print("P(EnjoySport = No)  =", prior_prob_no)

df_yes = df[df['EnjoySport'] == "Yes"]
df_no  = df[df['EnjoySport'] == "No"]

likelihood_yes = {
    col: df_yes[col].value_counts(normalize=True).to_dict()
    for col in ['Outlook', 'Temperature', 'Humidity', 'Wind']
}

likelihood_no = {
    col: df_no[col].value_counts(normalize=True).to_dict()
    for col in ['Outlook', 'Temperature', 'Humidity', 'Wind']
}

print("\nLikelihood Values when EnjoySport = YES:")
for feature, values in likelihood_yes.items():
    for value, prob in values.items():
        print(f"{feature}: {value} -> {prob}")

print("\nLikelihood Values when EnjoySport = NO:")
for feature, values in likelihood_no.items():
    for value, prob in values.items():
        print(f"{feature}: {value} -> {prob}")

def naive_bayes_classifier(test_instance, prior_prob, likelihood_yes, likelihood_no):
    poster_yes = np.log(prior_prob['Yes'])
    poster_no  = np.log(prior_prob['No'])

    for feature, value in test_instance.items():
        poster_yes += np.log(likelihood_yes[feature].get(value, 1e-6))
        poster_no  += np.log(likelihood_no[feature].get(value, 1e-6))

    print("\nPosterior Probabilities after Updating with Features:")
    print("Posterior(Yes) =", poster_yes)
    print("Posterior(No)  =", poster_no)

    return "Yes" if poster_yes > poster_no else "No"

test_instance = {
    "Outlook": "Sunny",
    "Temperature": "Cool",
    "Humidity": "Normal",
    "Wind": "Weak"
}

prior_prob = {"Yes": prior_prob_yes, "No": prior_prob_no}

prediction = naive_bayes_classifier(test_instance, prior_prob, likelihood_yes, likelihood_no)

print("\nFinal Prediction for given instance:", prediction)
