import pandas as pd

csv_file_path = r'enjoysport.csv'
df = pd.read_csv(csv_file_path)
print("Imported CSV Data")
print(df.head())

df['NewValue'] = df['Humidity']
print("\nProcessed Data")
print(df.head())

df.to_csv('exported_data.csv', index=False)
print("\nData exported to 'exported_data.csv'")

df1 = pd.read_csv('exported_data.csv')
print(df1.head())


excel_file_path = r'Untitled spreadsheet.xlsx generate content.xlsx'
df = pd.read_excel(excel_file_path)
print("Imported Excel Data")
print(df.head())

df['Total'] = df.sum(axis=1)
print("\nData with Rows Totals:")
print(df)

df.to_excel('modified_data.xlsx', index=False)
print("\nData exported to 'modified_data.xlsx'")

df = pd.read_excel(excel_file_path)
print(df.head())

//----


import pandas as pd

csv_file_path = r'enjoysport.csv'
df = pd.read_csv(csv_file_path)
print("Imported CSV Data")
print(df.head())

df['NewValue'] = df['Humidity']
print("\nProcessed Data")
print(df.head())

df.to_csv('exported_data.csv', index=False)
print("\nData exported to 'exported_data.csv'")

df1 = pd.read_csv('exported_data.csv')
print(df1.head())


excel_file_path = r'Untitled spreadsheet.xlsx generate content.xlsx'
df = pd.read_excel(excel_file_path)
print("Imported Excel Data")
print(df.head())

df['Total'] = df.sum(axis=1)
print("\nData with Rows Totals:")
print(df)

df.to_excel('modified_data.xlsx', index=False)
print("\nData exported to 'modified_data.xlsx'")

df = pd.read_excel(excel_file_path)
print(df.head())

//part2 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('sheet1.csv') 
print("Original Dataset")
print(df)

missing_data = df.isnull().sum()
print("Missing Data")
print(missing_data)

imputer = SimpleImputer(strategy='mean')
df['Salary'] = imputer.fit_transform(df[['Salary']])
df['Age'] = imputer.fit_transform(df[['Age']])

label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
print(df)

ct = ColumnTransformer(
    transformers=[('one-hot', OneHotEncoder(), ['Department'])],
    remainder='passthrough'
)

df_encoded = ct.fit_transform(df)
df_encoded = pd.DataFrame(df_encoded, columns=['HR', 'IT', 'Finance', 'Marketing', 'ID', 'Name', 'Age', 'Gender', 'Salary'])

print(df_encoded)

