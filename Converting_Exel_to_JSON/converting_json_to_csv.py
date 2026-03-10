import pandas
df = pandas.read_json('europe.json')
df.to_csv('europe.csv', index=False)