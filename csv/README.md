# Tabular input for ontology creation

The DFG Fächerklassifikation is published in .pdf format by DFG. Fortunately, the DFG also made available some tabular data in the form of two .xlsx files - one containing the German language version of the Fachsystematik, the other containing the English language version of the Fachsystematik. In order to create the ontology file, we need to process the data with a script that requires a .csv file as input.

## Creating the .csv input for [create_ontology.py](/scripts/create_ontology.py) - some irregularties explained

The ontology is created with [create_ontology.py](/scripts/create_ontology.py), which requires a .csv file as input. The .csv file is manually created from both .xlsx files provided by DFG. The .xlsx files contain line breaks and merged cells. To prepare the .csv file, merged cells need to be unmerged, and empty cells need to be filled down with the respective values.

The cells also contain line breaks and trailing white spaces. These may vary in between versions. This is a problem for [create_ontology.py](/scripts/create_ontology.py). The script may not be working with new versions of the Fachsystematik, unless the table is cleaned up, e.g. unexpected line breaks need to be removed, new trailing white spaces need to be removed, etc. until the script can parse through the whole file.

For more detailed info on the CSV creation see [./2024-2028/CVS_Creation_Process.md](./2024-2028/CVS_Creation_Process.md)

## Checking the alignment of German and English version in the .csv file

The ontology can only be created properly, if English and German version of the Fachsystematik align exactly in the .csv file. This can be tested with [parse_csv.py](/scripts/parse_csv.py).
