# DFG Fachsystematik Ontology / DFG Classification of Subject Areas Ontology

[DFG](https://www.dfg.de/en) (The Deutsche Forschungsgemeinschaft - German Research Foundation) *Classification of Scientific Disciplines, Research Areas, Review Boards and Subject Areas* is published as a PDF or HTML (see links below). 

We decided to build upon this work and build and RDF based ontology, for the *DFG Classification of Subject Areas*, so that browsing, searching and mapping (of subject number and its label) could be easy achieved by ontology/RDF processing software, such as ontology-lookup systems and tripe-stores.



## Ontology 
* **Ontology TTL**: [dfgfo.ttl](./dfgfo.ttl)
* **Ontology IRI**: https://github.com/tibonto/dfgfo/
* **Ontology PURL**: <https://raw.githubusercontent.com/tibonto/DFG-Fachsystematik-Ontology/main/dfgfo.ttl>
* **ontology prefix/id**: `dfgfo`


## Create/update ontology 

* Ontology metadata is stored in [metadata.ttl](.metadata.ttl)

[scripts/create_ontology.py](./scripts/create_ontology.py) Creates the dfgfo.ttl ontology by parsing 
the DFG classification system in [csv/Fachsystematik_2020-2024.csv](./csv/Fachsystematik_2020-2024.csv)

Each DFG Subject is a owl:Class with:
* DFG Subject number as URI 
* labels in EN and DE.
* class subpeclass accordinng to DFG Classification hierarchy 

**Run**

Create a python Virtual Environment

Install requirements `pip install -r scripts/requirements.txt`

Run script to create ontologu `python scripts/create_ontology.py`

## Other scripts

* [scripts/parse_csv.py](./scripts/parse_csv.py) parses the CSV and ensures that the collumns ` `Subject Number` and `Fachnummer` have the same values


## DFG Classification of Scientific Disciplines 

* [PDF(en)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_en_grafik.pdf)
* [PDF(de)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_de_grafik.pdf)
* [HTML page](https://www.dfg.de/en/dfg_profile/statutory_bodies/review_boards/subject_areas/index.jsp)
* [Edited CSV - combining both German and English labels](./csv/Fachsystematik_2020-2024.csv) (this repo)


## TODO: robots test in github actions