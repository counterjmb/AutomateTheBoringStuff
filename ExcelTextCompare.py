#python -m pip install pandas
#python -m pip install openpyxl

import pandas as pd

# read the Excel spreadsheet into a DataFrame
df = pd.read_excel('qp-java-restarts.xlsx')

# read the contents of the text file into a list
with open('213.txt', 'r') as file:
    txt_contents = [line.strip() for line in file.readlines()]

# compare the two lists and print any differences
for index, row in df.iterrows():
    cell_contents = row['School'] # replace 'Column1' with the name of the column you want to compare
    if cell_contents not in txt_contents:
        print(f"{cell_contents} not found in text file")