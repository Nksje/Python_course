import pandas as pd
# in order to export to excel
# pip install openpyxl
df = pd.read_csv('csv_files/2019.csv')
df.to_excel('output.xlsx')

