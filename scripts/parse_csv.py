import csv
from pathlib import Path
from typing import Tuple



dfg_csv_en = Path(__file__).parent.parent / 'csv' / 'Fachsystematik_2020-2024_EN_20210621.csv'
print(dfg_csv_en)


def split_id_label(id_n_label:str) -> Tuple[str, str]:
    id, label = id_n_label.split('\n')
    id = id.replace(' ', '') # remove spaces
    return id, label


# def create_triple(row, level, tree_hierarchy):
#     level_key = tree_hierarchy[level]
#     # parent cell
#     if level == 0:
#         parent = 'OWL:THING'
#     else:
#         # parent is the level above
#         parent = row[tree_hierarchy[level-1]]

#     if level != 3: 
#         id, label_en = split_id_label(id_n_label=row[level_key])
#     else:
#         id = row['Subject Number']
#         label_en = row['Subject']

    

#     print(row[level_key], level)
#     print(f'level:{level} label_en:{label_en}, ID:{id}, PARENT:{parent}')

# def row2triple():

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

        # print(row)

        for index, collumn in enumerate(tree_hierarchy):
            cell=row[(tree_hierarchy)[index]]
            print(f'\nSECTION: {index} {collumn}')
            print(f'INDEX: {index} COL:{collumn} CELL: {cell}')

            # current 
            if index == 3: 
                cell_id = row[(tree_hierarchy)[index - 1]]
                cell_label = cell 
            else:
                cell_id, cell_label = split_id_label(id_n_label=row[tree_hierarchy[index]]) 
            current = f'{cell_id} - {cell_label}'

             # parent
            if index == 0:
                parent = 'OWL:THING'
            else:
                parent_id, parent_label = split_id_label(id_n_label=row[(tree_hierarchy)[index - 1]]) 
                parent= f'{parent_id} - {parent_label}'
            print(f'CURRENT: {current}')
            print(f'PARENT: {parent}')

            


            # TODO: check if triple already exists before create_triple
            # create_triple(row=row, level=index, tree_hierarchy=tree_hierarchy)

