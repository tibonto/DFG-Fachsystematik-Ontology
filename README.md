# DFG Fachsystematik Ontology / DFG Classification of Subject Areas Ontology

[DFG](https://www.dfg.de/en) (The Deutsche Forschungsgemeinschaft - German Research Foundation) *Classification of Scientific Disciplines, Research Areas, Review Boards and Subject Areas* is published as a PDF or HTML (see links below). 

We decided to build upon this work and build and RDF based ontology, for the *DFG Classification of Subject Areas*, so that browsing, searching and mapping (of subject number and its label) could be easy achieved by ontology/RDF processing software, such as ontology-lookup systems and tripe-stores.

## Ontology (in progress)
* [dfg.ttl](./dfg.ttl)
## Create ontology
`pip install -r scripts/requirements.txt`

`python scripts/parse_csv.py`

## DFG Classification of Scientific Disciplines Spreadsheet 
* [CSM)](./csv/Fachsystematik_2020-2024_EN_20210621.csv)



