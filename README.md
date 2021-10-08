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

## From CSV to RDF


in [dfg-2020.concepts.csv](https://github.com/gbv/jskos-data/blob/master/dfg/dfg-2020.concepts.csv)


| level | notation | prefLabel@de | prefLabel@en |
|-------|----------|--------------|--------------| 
|0|3|Naturwissenschaften|Natural Sciences|
|0|1|Geistes- und Sozialwissenschaften|Humanities and Social Sciences|
|2|101|Alte Kulturen|Ancient Cultures|
|3|101-01|Ur- und Frühgeschichte (weltweit)|Prehistory and World Archaeology|
|1|32|Physik|Physics|
|1|33|Mathematik|Mathematics|
|1|34|Geowissenschaften|Geosciences|
|1|31|Chemie|Chemistry|
|2|321|Molekülchemie|Molecular Chemistry|
|3|321-01|"Anorganische Molekülchemie - Synthese, Charakterisierung"|Inorganic Molecular Chemistry - Synthesis and Characterisation|
|3|321-02|"Organische Molekülchemie- Synthese, Charakterisierung"|Organic Molecular Chemistry - Synthesis and Characterisation|

From the table and [PDF(en)](https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_en_grafik.pdf), I gather that the levels create a tree structure

* Humanities and Social Sciences (1)
    * Ancient Cultures (11)
        * Prehistory and World Archaeology (101-01)
* Natural Sciences (3)
    * Chemistry (31)
        * Molecular Chemistry (321)
            * Inorganic Molecular Chemistry - Synthesis and Characterisation (321-01)
            * Organic Molecular Chemistry - Synthesis and Characterisation (321-02)
    * Physics (32)
    * Mathematics (33)
    * Geosciences (34)

**Trying to understand the logic (from a machine point of view):**
* Q: How do I know that Chemistry (31) is a child of Natural Sciences (3)?
    * A: because the 1st digit of Chemistry (31) is 3 -> Natural Sciences (3)
* Q: do the subject from level 0 go only up to 9 (single digit)? 
    * A: Yes. there are only 4: 
        * 0,1,Geistes- und Sozialwissenschaften,Humanities and Social Sciences
        * 0,2,Lebenswissenschaften,Life Sciences
        * 0,3,Naturwissenschaften,Natural Sciences
        * 0,4,Ingenieurwissenschaften,Engineering Sciences
* Q: How do I know that Molecular Chemistry (321) is a child of Chemistry (31)?
    * A: impossible to assert it by the numbers, but in  [dfg-2020.concepts.csv](https://github.com/gbv/jskos-data/blob/master/dfg/dfg-2020.concepts.csv) **order** the level 2 disciplines that are children of Chemistry (31) follow it. 

```    
1,31,Chemie,Chemistry` 
2,321,Molekülchemie,Molecular Chemistry
2,322,Chemische Festkörper- und Oberflächenforschung,Chemical Solid State and Surface Research
2,323,Physikalische Chemie,Physical Chemistry
2,324,Analytische Chemie,Analytical Chemistry
2,325,Biologische Chemie und Lebensmittelchemie,Biological Chemistry and Food Chemistry
2,326,Polymerforschung,Polymer Research
2,327,Theoretische Chemie,Theoretical Chemistry
``` 

**Conclusions**

**[dfg-2020.concepts.csv](https://github.com/gbv/jskos-data/blob/master/dfg/dfg-2020.concepts.csv) is ordered hierachically for level 0,1,2** 
* start at `0,1,Geistes- und Sozialwissenschaften,Humanities and Social Sciences`
* followed by `1,11,Geisteswissenschaften,Humanities`
* wich is followed by `2,101,Alte Kulturen,Ancient Cultures`, `2,102,Geschichtswissenschaften,History`, etc (there is a but there that needs correction)



