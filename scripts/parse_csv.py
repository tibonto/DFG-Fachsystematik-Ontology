import csv
from pathlib import Path
from pprint import pprint 


#dfg_csv = Path(__file__).parent.parent / 'csv' / '2020-2024' / 'Fachsystematik_2020-2024.csv'
dfg_csv = Path(__file__).parent.parent / 'csv' / '2024-2028' / 'Fachsystematik_2024-2028.csv'
print(dfg_csv)


with open(dfg_csv, newline='') as csvfile:
    csvfile = csv.DictReader(csvfile, delimiter=',')
    for row in csvfile:
        pprint(row)
        # test: EN and DE subject match
        assert row['Subject Number'] == row['Fachnummer']