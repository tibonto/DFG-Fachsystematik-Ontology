
[![Ontology testing](https://github.com/tibonto/DFG-Fachsystematik-Ontology/actions/workflows/main.yml/badge.svg)](https://github.com/tibonto/DFG-Fachsystematik-Ontology/actions/workflows/main.yml)

# DFG Fachsystematik Ontology / DFG Classification of Subject Areas Ontology

[DFG](https://www.dfg.de/en) (The Deutsche Forschungsgemeinschaft - German Research Foundation) *Classification of Scientific Disciplines, Research Areas, Review Boards and Subject Areas* is published as a PDF or HTML (see links below). 

We decided to build upon this work and build and RDF based ontology, for the *DFG Classification of Subject Areas*, so that browsing, searching and mapping (of subject number and its label) could be easy achieved by ontology/RDF processing software, such as ontology-lookup systems and tripe-stores.

![](./docs/dfgfo-hierarchies.png)



## Ontology 
* **Ontology TTL**: [dfgfo.ttl](./dfgfo.ttl)
* **Ontology IRI**: https://github.com/tibonto/dfgfo/
* **Ontology PURL**: <https://raw.githubusercontent.com/tibonto/DFG-Fachsystematik-Ontology/main/dfgfo.ttl>
* **ontology prefix/id**: `dfgfo`


## Create/update ontology 

**[dfgfo.ttl](./dfgfo.ttl) ontology file is created, by [scripts/create_ontology.py](./scripts/create_ontology.py) python script**, which
* parses the DFG classification system encoded [csv/Fachsystematik_2020-2024.csv](./csv/Fachsystematik_2020-2024.csv) (in EN/DE)
* encodes each of the DFG's classification subjects (in .csv cells) into RDF graph triples
    * of type `owl:Class`
    * with `rdfs:label` in EN and skos:altLabel in DE
    * subsumed to parent subject with `rdfs:subClassOf` accordinng to DFG Classification hierarchy 
* parses the metadata triples from [metadata.ttl](./metadata.ttl) into a graph
* parses handle triples from [handles-2020.ttl](./handles-2020.ttl) into a graph
* joins metadata, handles and DFG classification graphs into [dfgfo.ttl](./dfgfo.ttl)


**Run**

Create a python3 Virtual Environment

Install requirements `pip install -r scripts/requirements.txt`

Run script to create ontology `python scripts/create_ontology.py`. Make sure to use end of line sequence `LF` for  [/csv/Fachsystematik_2020-2024.csv](/csv/Fachsystematik_2020-2024.csv).


## Other scripts

* [scripts/parse_csv.py](./scripts/parse_csv.py) parses the CSV and ensures that the columns `Subject Number` and `Fachnummer` have the same values

## Ontology contributions:
Contributions are welcome.

At every push or pull_request a [ROBOT report](http://robot.obolibrary.org/report) and  [ROBOT validate OWL DL profile](http://robot.obolibrary.org/validate-profile)test will be run from [.github/workflows/main.yml](.github/workflows/main.yml).



## DFG Classification of Scientific Disciplines 

* [PDF(en)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_en_grafik.pdf)
* [PDF(de)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_de_grafik.pdf)
* [HTML page](https://www.dfg.de/en/dfg_profile/statutory_bodies/review_boards/subject_areas/index.jsp)
* [Edited CSV - combining both German and English labels](./csv/Fachsystematik_2020-2024.csv) (this repo)


