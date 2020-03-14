import pandas as pd

read_file = pd.read_excel ('labs_list.xlsx')
read_file.to_csv ('us_labs.csv', index = None, header=True)