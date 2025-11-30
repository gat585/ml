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
-----------------------------------------------------


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
