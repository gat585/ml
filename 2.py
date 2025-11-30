import csv

print("\nThe most general hypothesis: ['?', '?', '?', '?', '?', '?']\n")
print("\nThe most specific hypothesis: ['0', '0', '0', '0', '0', '0']\n")

a = []

with open('enjoysport1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)

print("\nInitial value of hypothesis:")

num_attributes = len(a[0]) - 1
hypothesis = ['0'] * num_attributes
print(hypothesis)

for j in range(num_attributes):
    hypothesis[j] = a[1][j]

print("\nFind-S: Finding Maximally Specific Hypothesis\n")

for i in range(1, len(a)):
    if a[i][num_attributes].lower() == 'yes':
        for j in range(num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]

        print("For training example no: {}, the hypothesis is: {}".format(i, hypothesis))

print("\nThe maximally specific hypothesis for the given examples is:\n")
print(hypothesis)
