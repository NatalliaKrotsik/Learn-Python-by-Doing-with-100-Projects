import pandas as pd

input = pd.read_excel('input.xlsx')
print(input)

input['Total'] = input['Price'] + input['Quantity']
input.to_excel('output.xlsx', index=False)

