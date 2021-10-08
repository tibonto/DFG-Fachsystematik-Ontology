import csv
from pathlib import Path
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, OWL, RDFS
g = Graph()
ns_str = 'https://github.com/tibonto/dfgfo/'
namespace = Namespace(ns_str)

dfg_csv = Path(__file__).parent.parent / 'jskos-data' / 'dfg'/ 'dfg-2020.concepts.csv'
print(dfg_csv)


def create_class(graph, ns, node_name, labels, parent):
    print(labels)
    uri_str = f'{ns_str}{node_name}'
    node = URIRef(uri_str)
    # type
    graph.add((node, RDF.type, OWL.Class))
    # class 
    if parent is None:
        graph.add((node, RDFS.subClassOf, OWL.Thing))

    # label
    graph.add((node, RDFS.label, Literal(f'{labels[0]}@en')))
    graph.add((node, RDFS.label, Literal(f'{labels[1]}@de')))
    ns.node_name
    print(node)
    
    # uri = URIRef(uri_str)


with open(dfg_csv, newline='') as csvfile:
    csvfile = csv.DictReader(csvfile, delimiter=',')
    for row in csvfile:
        # print(row)
        if int(row['level']) == 0: # parent classes
            print(row)
            this_node_parent = None

            create_class(graph=g, 
                            ns=namespace, 
                            node_name=row["notation"], 
                            labels=[row['prefLabel@en'], row['prefLabel@de']],
                            parent=this_node_parent)

print(g.serialize())
# print(dir(g))

# TODO:
# * labels DONE
# * OWL.Thing DONE
# * class parent: RDFS.subClassOf 
# variables such as namespace and metadata from metadata.yml
