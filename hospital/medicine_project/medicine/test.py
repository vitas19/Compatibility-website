import pandas as pd
medicine_data = pd.read_excel('../mysite/lista_farmacos.xlsx')
l_uniques = list(medicine_data["Donación"].unique())
print(l_uniques)
print(len(l_uniques))