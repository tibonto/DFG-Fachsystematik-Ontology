
[![Ontology testing](https://github.com/tibonto/DFG-Fachsystematik-Ontology/actions/workflows/main.yml/badge.svg)](https://github.com/tibonto/DFG-Fachsystematik-Ontology/actions/workflows/main.yml)

# DFG Fachsystematik Ontology / DFG Classification of Subject Areas Ontology

[DFG](https://www.dfg.de/en) (The Deutsche Forschungsgemeinschaft - German Research Foundation) *Classification of Scientific Disciplines, Research Areas, Review Boards and Subject Areas* is published as a PDF or HTML (see links below). 

We decided to build upon this work and build and RDF based ontology, for the *DFG Classification of Subject Areas*, so that browsing, searching and mapping (of subject number and its label) could be easy achieved by ontology/RDF processing software, such as ontology-lookup systems and tripe-stores.


![WebOwl visualization of ontology classes(detail)](docs/webowl_viz_detail.png)



## Ontology

* **Ontology TTL**: [dfgfo.ttl](./dfgfo.ttl)
* **Ontology PURL**: <https://w3id.org/dfgfo/2024>
* **ontology prefix/id**: `dfgfo`

![screen capture of classes hierarchy in protege](./docs/dfgfo-hierarchies.png)


## Create/update ontology

**[dfgfo.ttl](./dfgfo.ttl) ontology file is created, by [scripts/create_ontology.py](./scripts/create_ontology.py) python script**, which

* parses the DFG classification system encoded in csv/Fachsystematik_20XX-20XX.csv (in EN/DE) (cf. directory [csv/](/csv/) and [csv/README.md](/csv/README.md))
* encodes each of the DFG's classification subjects (in .csv cells) into RDF graph triples
  * of type `owl:Class`
  * with `rdfs:label` in EN and skos:altLabel in DE
  * subsumed to parent subject with `rdfs:subClassOf` accordinng to DFG Classification hierarchy
* parses the metadata triples from [metadata.ttl](./metadata.ttl) into a graph
* joins metadata and DFG classification graphs into [dfgfo.ttl](./dfgfo.ttl)

### Run

Create a python3 Virtual Environment

Install requirements `pip install -r scripts/requirements.txt`

Run script to create ontology `python scripts/create_ontology.py`. Make sure to use end of line sequence `LF` in the csv file used to create the ontology (for example when working on Windows).

## Other scripts

* [scripts/parse_csv.py](./scripts/parse_csv.py) parses the CSV and ensures that the columns `Subject Number` and `Fachnummer` have the same values

## Ontology contributions

Contributions are welcome.

At every push or pull_request a [ROBOT report](http://robot.obolibrary.org/report) and  [ROBOT validate OWL DL profile](http://robot.obolibrary.org/validate-profile) test will be run from [.github/workflows/main.yml](.github/workflows/main.yml).

## DFG Classification of Scientific Disciplines 

* [HTML page](https://www.dfg.de/en/research-funding/proposal-funding-process/interdisciplinarity/subject-area-structure)
* PDFs
  * 2016-2019
    * [PDF (en)](/pdf/fachsystematik-2016-2019-en-data.pdf) (local copy)
    * [PDF (de)](/pdf/fachsystematik-2016-2019-de-data.pdf) (local copy)
  * 2020-2024
    * [PDF (en)](/pdf/fachsystematik-2020-2024-en-data.pdf) (local copy)
    * [PDF (de)](/pdf/fachsystematik-2020-2024-de-data.pdf) (local copy)
    * [Highlighted Changes (de)](/pdf/fachsystematik-2019-de-aenderungen.pdf) (local copy)
  * 2024-2028
    * [PDF (en)](/pdf/fachsystematik-2024-2028-en-data.pdf) (local copy)
    * [PDF (de)](/pdf/fachsystematik-2024-2028-de-data.pdf) (local copy)
    * [Highlighted Changes (de)](/pdf/fachsystematik-2023-de-aenderungen.pdf) (local copy)
* Edited CSV - combining both German and English labels
  * [2020-2024](/csv/2020-2024/Fachsystematik_2020-2024.csv) (this repo)
  * [2024-2028](/csv/2024-2028/Fachsystematik_2024-2028.csv) (this repo)

## Releases

For previous versions (2020-2024) see https://github.com/tibonto/DFG-Fachsystematik-Ontology/releases

## Use Cases

*Are you or your institution using the DFG-Fachsystematik-Ontology? We would like to hear from you (via an [issue](https://github.com/tibonto/DFG-Fachsystematik-Ontology/issues/)), and include your use-case in this section.*

* [DaRUS - the data repository of the University of Stuttgart](https://darus.uni-stuttgart.de/): DFGFO is used to classify datasets according to topic, see example [10.18419/darus-3988](https://darus.uni-stuttgart.de/dataset.xhtml?persistentId=doi:10.18419/darus-3988)
