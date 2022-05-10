import pandas as pd

df = pd.read_json('https://data.nasa.gov/resource/gh4g-9sfh.json')
#sprawdzenie spójności danych i ich ewentualna modyfikacja:
# print(df.info())
# print(df.isnull().sum())
# df = df.fillna('Unknown')
# df = df.replace(',', '.')
# df[['date', 'time']] = df['year'].str.split('T', expand=True)
# odrzuecenie powtarzających się wartości koordynatów geograficznych oraz w większości pustych kolumn
# df.drop(labels=["geolocation", ":@computed_region_cbhk_fwbd", ":@computed_region_nnqa_25f4", "year"], axis=1, inplace=True)
df.to_csv('meteorites.csv', index=None)