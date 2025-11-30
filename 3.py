import pandas as pd
import numpy as np

data = pd.read_csv("enjoysport1.csv")
concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]

    for i, instance in enumerate(concepts):
        if target[i] == "yes":
            for x in range(len(specific_h)):
                if instance[x] != specific_h[x]:
                    specific_h[x] = "?"
                    general_h[x][x] = "?"
        else:
            for x in range(len(specific_h)):
                if instance[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = "?"
  
    indices = [i for i, val in enumerate(general_h) if val == ["?" for _ in range(len(specific_h))]]
    for i in reversed(indices):
        del general_h[i]

    return specific_h, general_h

S_final, G_final = learn(concepts, target)
print("\nFinal S:", S_final, sep="\n")
print("\nFinal G:", G_final, sep="\n")
