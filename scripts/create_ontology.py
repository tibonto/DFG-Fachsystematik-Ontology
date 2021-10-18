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
dfg_onto_metadata_fn = Path(__file__).parent.parent / 'metadata.ttl'
dfg_onto_fn = Path(__file__).parent.parent / 'dfgfo.ttl' 
dfg_csv_en = Path(__file__).parent.parent / 'csv' / 'Fachsystematik_2020-2024.csv'
print(dfg_csv_en)

g_metadata = Graph()
g_metadata.parse(str(dfg_onto_metadata_fn.absolute()))

g_classes = Graph()
ns_str = 'https://github.com/tibonto/dfgfo/'
namespace = Namespace(ns_str)

g_classes.namespace_manager.bind('owl', 'http://www.w3.org/2002/07/owl#', override=False)
g_classes.namespace_manager.bind('dfgfo', ns_str, override=False)


def split_id_label(id_n_label:str) -> Tuple[str, str]:
    id, label = id_n_label.split('\n')
    id = id.replace(' ', '') # remove spaces
    return id, label


def create_class(graph, ns, node_name, labels, parent):
    uri_str = f'{ns_str}{node_name}'
    node = URIRef(uri_str)
    print(f'Class: {uri_str} labels: {labels}')

    # type
    graph.add((node, RDF.type, OWL.Class))
    # class 
    if parent is None:
        graph.add((node, RDFS.subClassOf, OWL.Thing))
    else:
        parent_uri_str = f'{ns_str}{parent}'
        parent_node = URIRef(parent_uri_str)
        graph.add((node, RDFS.subClassOf, parent_node))
    # labels
    graph.add((node, RDFS.label, Literal(f'{labels[0]}', lang='en')))
    graph.add((node, RDFS.label, Literal(f'{labels[1]}', lang='en')))
    # obo:IAO_0000111 # editor preferred term

    ns.node_name
    # print(f'GRAPH NODE: {node} ------')


tree_hierarchy = ['Scientific Discipline', 'Subject Area', 'Review Board', 'Subject']
header_en_de_mapping = {
    'Scientific Discipline': 'Wissenschaftsbereich',
    'Subject Area': 'Fachgebiet', 
    'Review Board': 'Fachkollegium',
    'Subject':'Fach'}

# de_tree_hierarchy = [
  # top to bottom 
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
            en_key = (tree_hierarchy)[index]
            de_key = header_en_de_mapping[en_key]
            cell=row[en_key]
            cell_de=row[de_key]
            # print(f'EN: {cell}\nDE:{cell_de}')
            print(f'\nSECTION: {index} {collumn}')
            print(f'INDEX: {index} COL:{collumn} CELL: {cell}')

            # current 
            if index == 3: 
                cell_id = row['Subject Number']
                cell_label = cell 
                cell_label_de = cell_de
            else:
                cell_id, cell_label = split_id_label(id_n_label=row[tree_hierarchy[index]])
                cell_label_de = 'DE'
                cell_id_de, cell_label_de = split_id_label(id_n_label=cell_de)
            current = f'{cell_id} - {cell_label}'
            print(f'CEL ID: <<<<{cell_id}>>>')
             # parent
            if index == 0:
                parent_id = None
            else:
                parent_id, parent_label = split_id_label(id_n_label=row[(tree_hierarchy)[index - 1]]) 
            print(f'CURRENT: {current}')
            print(f'PARENT: <<<{parent_id}>>>')

            create_class(graph=g_classes, 
                         ns=namespace, 
                         node_name=cell_id, 
                         labels=[cell_label, cell_label_de],
                         parent=parent_id)


# join g_metadata + g_classes graphs into g_joint
g_joint = Graph() # after the g_classes
g_joint = g_metadata + g_classes

print('\n\nSERIALIZE\n\n')
print(g_joint.serialize())
with open(dfg_onto_fn, 'w') as dfg_onto:
    dfg_onto.write(g_joint.serialize())