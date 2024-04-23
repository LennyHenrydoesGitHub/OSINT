import pandas as pd

f = pd.read_csv('./output.csv')
country_codes = pd.read_csv('./country_codes-ICB.csv')
country_codes2 = pd.read_csv('./country_codes-ISO.csv')

code_to_name = dict(zip(country_codes['Country codes'], country_codes['Name']))
name_to_code = dict(zip(country_codes2['Name'], country_codes2['ISO 3166-1']))

f['Country_name'] = f['Country_code'].map(code_to_name)
f['Country_code'] = f['Country_name'].map(name_to_code)

new_f = "./conversion.csv"

data = []
header = ["", "Year", "Country code", "Conflict", "Country Name"]

for i in range(f.shape[0]):
    data.append([i, f.loc[i][1], f.loc[i][0], f.loc[i][2], f.loc[i]['Country_name']])

with open(new_f, 'w', newline="") as file:
    for header in header:
        file.write(str(header) + ',')
    file.write('\n')
    for row in data:
        for x in row:
            file.write(str(x) + ',')
        file.write('\n')
