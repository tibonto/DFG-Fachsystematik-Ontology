# CSV Parsing Errors & Fixes

## Error in `11 Humanities`


`python scripts/create_ontology.py csv/2024-2028/Fachsystematik_2024-2028.csv`

```python
SECTION: 0 Scientific Discipline
INDEX: 0 COL:Scientific Discipline CELL: 1 
Humanities and Social Sciences
CELL ID: <<<<1>>>
CURRENT: 1 - Humanities and Social Sciences
PARENT: <<<None>>>
Class: https://github.com/tibonto/dfgfo/1 labels: ['Humanities and Social Sciences', 'Geistes- und Sozialwissenschaften']

SECTION: 1 Subject Area
INDEX: 1 COL:Subject Area CELL: 11 Humanities
Traceback (most recent call last):
  File "/home/acastro/Documents/external_projects/DFG-Fachsystematik-Ontology/scripts/create_ontology.py", line 96, in <module>
    cell_id, cell_label = split_id_label(id_n_label=row[tree_hierarchy[index]])
  File "/home/acastro/Documents/external_projects/DFG-Fachsystematik-Ontology/scripts/create_ontology.py", line 34, in split_id_label
    id, label = id_n_label.split('\n')
ValueError: not enough values to unpack (expected 2, got 1)
```

**Issue:**
Unlike other "Subject Area" values that seperate `NN Subject` with a line break, `11 Humanities` only uses space as a separator:

**Fix:**
Search & Replace in CSV `11 Humanities` for `"11\nHumanities"`

**Commit:** b857e8c8dfb980fb2407a8b3d92bd6cb64d67fc9

## Error on 2.31

```python
SECTION: 2 Review Board
INDEX: 2 COL:Review Board CELL: 2.31
Agriculture, Forestry and Veterinary Medicine
id_n_label: 2.31
Agriculture, Forestry and Veterinary Medicine
id_n_label: 2.31
Agrar-, Forstwissenschaften 
und Tiermedizin
Traceback (most recent call last):
  File "/home/acastro/Documents/external_projects/DFG-Fachsystematik-Ontology/scripts/create_ontology.py", line 99, in <module>
    cell_id_de, cell_label_de = split_id_label(id_n_label=cell_de)
  File "/home/acastro/Documents/external_projects/DFG-Fachsystematik-Ontology/scripts/create_ontology.py", line 35, in split_id_label
    id, label = id_n_label.split('\n')
ValueError: too many values to unpack (expected 2)
```

**Issue:** 2.31 has 2 line breaks, when it should only have 1, between number and term
```
2.31
Agrar-, Forstwissenschaften 
und Tiermedizin
```

**Fix:**
Search & Replace in CSV `Agrar-, Forstwissenschaften\nund Tiermedizin` for `"Agrar-, Forstwissenschaften und Tiermedizin"`

**commit:** 3c4448653f8ed0a5570a53c66a7675b7194b6088


## Error on 34 Geowissen-schaften

**Issue:**

```python
SECTION: 1 Subject Area
INDEX: 1 COL:Subject Area CELL: 34
Geosciences 
id_n_label: 34
Geosciences 
id_n_label: 34
Geowissen-
schaften 
Traceback (most recent call last):
  File "/home/acastro/Documents/external_projects/DFG-Fachsystematik-Ontology/scripts/create_ontology.py", line 99, in <module>
    cell_id_de, cell_label_de = split_id_label(id_n_label=cell_de)
  File "/home/acastro/Documents/external_projects/DFG-Fachsystematik-Ontology/scripts/create_ontology.py", line 35, in split_id_label
    id, label = id_n_label.split('\n')
ValueError: too many values to unpack (expected 2)
```

Same issue as previous. Extra line break between words.

**Fix:**

Remove line break between words.

`"34\nGeowissen-\nschaften "`  replaced with `"34\nGeowissen-schaften "` 

# terms ending in space

replaced:
* `Geosciences "` with `Geosciences"`
* `Privatrecht ` with `Privatrecht`