import csv
from pathlib import Path
from typing import Tuple
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, OWL, RDFS

'''
Creates the dfgfo.ttl ontology by parsing 
the DFG classification system in  csv/Fachsystematik_2020-2024_EN_20210621.csv

Each Subject is a owl:Class with:
* DFG Subject number as URI 
* labels in EN and DE.
* class subpeclass accordinng to DFG Classification hierarchy 
'''

g = Graph()
ns_str = 'https://github.com/tibonto/dfgfo/'
namespace = Namespace(ns_str)

dfg_onto_fn = Path(__file__).parent.parent / 'dfgfo.ttl' 
dfg_csv_en = Path(__file__).parent.parent / 'csv' / 'Fachsystematik_2020-2024_EN_20210621.csv'
print(dfg_csv_en)


def split_id_label(id_n_label:str) -> Tuple[str, str]:
    id, label = id_n_label.split('\n')
    id = id.replace(' ', '') # remove spaces
    return id, label


def create_class(graph, ns, node_name, labels, parent):
    print(labels)
    uri_str = f'{ns_str}{node_name}'
    node = URIRef(uri_str)
    # type
    graph.add((node, RDF.type, OWL.Class))
    # class 
    if parent is None:
        graph.add((node, RDFS.subClassOf, OWL.Thing))
    else:
        parent_uri_str = f'{ns_str}{parent}'
        parent_node = URIRef(parent_uri_str)
        graph.add((node, RDFS.subClassOf, parent_node))

    # label
    graph.add((node, RDFS.label, Literal(f'{labels[0]}@en')))
    # graph.add((node, RDFS.label, Literal(f'{labels[1]}@de')))
    ns.node_name
    print(f'GRAPH NODE: {node} ------')


tree_hierarchy = ['Scientific Discipline', 'Subject Area', 'Review Board', 'Subject']  # top to bottom 
# DFG Tree hierarchy:
# * Scientific Discipline
#   * Subject Area
#     * Review Board
#       * Subject
#       * Subject Number

with open(dfg_csv_en, newline='') as csvfile:
    csvfile = csv.DictReader(csvfile, delimiter=',')
    for row in csvfile:
        for index, collumn in enumerate(tree_hierarchy):
            cell=row[(tree_hierarchy)[index]]
            print(f'\nSECTION: {index} {collumn}')
            print(f'INDEX: {index} COL:{collumn} CELL: {cell}')

            # current 
            if index == 3: 
                cell_id = row['Subject Number']
                cell_label = cell 
            else:
                cell_id, cell_label = split_id_label(id_n_label=row[tree_hierarchy[index]]) 
            current = f'{cell_id} - {cell_label}'
            print(f'CEL ID: <<<<{cell_id}>>>')
             # parent
            if index == 0:
                parent_id = None
            else:
                parent_id, parent_label = split_id_label(id_n_label=row[(tree_hierarchy)[index - 1]]) 
            print(f'CURRENT: {current}')
            print(f'PARENT: <<<{parent_id}>>>')

            create_class(graph=g, 
                         ns=namespace, 
                         node_name=cell_id, 
                         labels=[cell_label],
                         parent=parent_id)

print(g.serialize())
with open(dfg_onto_fn, 'w') as dfg_onto:
    dfg_onto.write(g.serialize())
    


            # TODO: DE label

