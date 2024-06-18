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

**Commit:** 