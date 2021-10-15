# DFG Fachsystematik Ontology / DFG Classification of Subject Areas Ontology

[DFG](https://www.dfg.de/en) (The Deutsche Forschungsgemeinschaft - German Research Foundation) *Classification of Scientific Disciplines, Research Areas, Review Boards and Subject Areas* is published as a PDF or HTML (see links below). 

We decided to build upon this work and build and RDF based ontology, for the *DFG Classification of Subject Areas*, so that browsing, searching and mapping (of subject number and its label) could be easy achieved by ontology/RDF processing software, such as ontology-lookup systems and tripe-stores.



## Ontology (in progress)
* [dfgfo.ttl](./dfgfo.ttl)


## Create ontology

[scripts/create_ontology.py](./scripts/create_ontology.py) Creates the dfgfo.ttl ontology by parsing 
the DFG classification system in [csv/Fachsystematik_2020-2024_EN_20210621.csv](./csv/Fachsystematik_2020-2024_EN_20210621.csv)

Each DFG Subject is a owl:Class with:
* DFG Subject number as URI 
* labels in EN and DE.
* class subpeclass accordinng to DFG Classification hierarchy 

**Run**

Create a python Virtual Environment

Install requirements `pip install -r scripts/requirements.txt`

Run script to create ontologu `python scripts/create_ontology.py`


## DFG Classification of Scientific Disciplines 

* [PDF(en)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_en_grafik.pdf)
* [PDF(de)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_de_grafik.pdf)
* [HTML page](https://www.dfg.de/en/dfg_profile/statutory_bodies/review_boards/subject_areas/index.jsp)
* [Edited CSV](./csv/Fachsystematik_2020-2024_EN_20210621.csv) (this repo)

