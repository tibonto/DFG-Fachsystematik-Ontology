# DFG Fachsystematik Ontology / DFG Classification of Subject Areas Ontology

[DFG](https://www.dfg.de/en) (The Deutsche Forschungsgemeinschaft - German Research Foundation) *Classification of Scientific Disciplines, Research Areas, Review Boards and Subject Areas* is published as a PDF or HTML (see links below). 
[Jakob Voß (@nichtich)](https://github.com/nichtich) has published a [CSV](https://github.com/gbv/jskos-data/blob/master/dfg/dfg-2020.concepts.csv) with the classification system organized in tabular data.

We decided to build upon this work and build and RDF based ontology, for the *DFG Classification of Subject Areas*, so that browsing, searching and mapping (of subject number and its label) could be easy achieved by ontology/RDF processing software, such as ontology-lookup systems and tripe-stores.

## DFG Classification of Scientific Disciplines Links
* [PDF(en)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_en_grafik.pdf)
* [PDF(de)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_de_grafik.pdf)
* [HTML page](https://www.dfg.de/en/dfg_profile/statutory_bodies/review_boards/subject_areas/index.jsp)
* [dfg-2020.concepts.csv](https://github.com/gbv/jskos-data/blob/master/dfg/dfg-2020.concepts.csv)


# How To
* add [jskos-data](https://github.com/gbv/jskos-data) git repository as submodule(shouldn't be need as it is already there)
    * `git submodule add -b master --depth 1 git@github.com:gbv/jskos-data.git`
* update [jskos-data](https://github.com/gbv/jskos-data) submodule
    * `git submodule update  --remote --merge` 
* locate [jskos-data/dfg/dfg-2020.concepts.csv](./jskos-data/dfg/dfg-2020.concepts.csv)
