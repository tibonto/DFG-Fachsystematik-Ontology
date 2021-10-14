import csv
from pathlib import Path
from typing import Dict
from pprint import pprint
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

def defcsv2nestedlists(csv_f):
    dfg_subjects = []
    with open(csv_f, newline='') as csvfile:
        csvfile = csv.DictReader(csvfile, delimiter=',')
        for row in csvfile:
            current_level = int(row['level'])
            if current_level == 0:
                dfg_subjects.append([row])
    return dfg_subjects

def index_str2list(index_str: str) -> list:
    index_list = index_str.split('.')
    index_list = [int(i) for i in index_list]    
    return index_list

def index_list2str(index_list: list) ->  str:
    index_str = ('.').join(index_list)
    return index_str

def index_str2int(index_str: str) -> int:
    index_list = index_str.split('.')
    index_str = ('').join(index_list)
    index_int = int(index_str)
    return index_int


def add_to_index(index:str, level:int)-> str:
    # print(f'index: {index} level: {level}')
    # if index == '2.5.5.0':
    #     import pdb; pdb.set_trace()
    index_list = index_str2list(index_str=index)
    # print(f'index_list before addition: {index_list}')
    # print(f'index_list after addition: {index_list}')
    # print(f'added: {added_to_level} to level:{level - 1} in list: {index_list}')
    # reset higher levels to 0
    if level == 0:
        index_list = [(index_list[0] + 1)] + ([0] * 3)
    else:
        index_list[(level - 1)] = index_list[(level - 1)] + 1  
        index_list_left = index_list[:(level)] 
        index_list_right = index_list[(level):] 
        index_list = index_list_left + (['0'] * len(index_list_right))
    new_index_str = ".".join([str(i) for i in index_list])
    return new_index_str



# def build_parent_index(current_index:str, level=int(row['level'])) -> str:
#     if level == 1:
#         parent_index = None
#         return parent_index
#     else: 
#         current_index_list = index_str2list(index_str=current_index)


#     current_index_list_parent = (current_index.split('.'))[:-1]
#     current_index_list_parent = ".".join(current_index_list_parent)
#     return current_index_list_parent


def csv2dict(csv_f:str) -> Dict:
    prev_index =  "0.0.0.0"
    dfg_subjects = {}
    indeces = []
    with open(csv_f, newline='') as csvfile:
        csvfile = csv.DictReader(csvfile, delimiter=',')
        for i, row in enumerate(csvfile):
            if i:
                index = add_to_index(index=prev_index, level=int(row['level']))
                indeces.append(index)
                dfg_subjects[index] = row


                index_list = index_str2list(index_str=index)
                index_int = index_str2int(index_str=index)
                # index_set = set(index_list[1:])

                if int(row['level']) == 1:
                # if index_int % 1000 == 0:  # cases: 1.0.0.0, 2.0.0.0 #len(index_set) == 1
                    print('ROOT NODE')
                    parent_key = None
                else:
                    parent_key = 'TODO parent' # prev_index
                dfg_subjects[index]['parent_key'] = parent_key
                print(f'prev:{prev_index}, current:{index} - {index_int}, {row}')

                prev_index = index
    return dfg_subjects, indeces


# Step 1: create dfg_subjects_dict with hierarchy numbers ie. 2.1.2.0
# Todo: Step 2: add parents to the dfg_subjects_dict v 

dfg_subjects_dict,indeces = csv2dict(csv_f=dfg_csv)
pprint(dfg_subjects_dict)

# TESTS

assert len(indeces) == len(set(indeces)) # test for repeated indeces(keys)

prev_key = '0.0.0.0' 
for key, val in dfg_subjects_dict.items(): # test for always increasing key values
    prev_key_int = int("".join([i for i in prev_key.split('.')]))
    key_int = int("".join([i for i in key.split('.')]))
    assert key_int > prev_key_int
# print(indeces, '\n')

# Todo: Step 3: iterate over dfg_subjects_dict and create RDF triples


# with open(dfg_csv, newline='') as csvfile:
#     csvfile = csv.DictReader(csvfile, delimiter=',')
#     for row in csvfile:
#         # print(row)
#         current_level = int(row['level'])

#         if current_level == 0: # parent classes
#             print(row)
#             this_node_parent = None

#             create_class(graph=g, 
#                             ns=namespace, 
#                             node_name=row["notation"], 
#                             labels=[row['prefLabel@en'], row['prefLabel@de']],
#                             parent=this_node_parent)
        
#         else:  # all other levels

# print(g.serialize())
# print(dir(g))

# TODO:
# * labels DONE
# * OWL.Thing DONE
# * class parent: RDFS.subClassOf 
# variables such as namespace and metadata from metadata.yml
