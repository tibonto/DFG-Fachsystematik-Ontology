# CSV creation from DFG's XLSXs 

## For each of the Excel (.xlsx) files 

1. remove rows 1,2 (title, empty)
2. remove empty columns A and G
5. save both DE and EN sheets into a CSV (to allow the following operations) 
    5.1 CSV export: Check "Quote all text cells" so that we avoid issues with commas within the cells
    5.2 **from this point onward we shall only work on the CSVs and not the .xlsx)**

## in CSVs (easier to edit and see errors)

1. add  headers EN: `Subject Number` and  `Subject`  for column A, B . DE: `Fachnummer`, `Fach` 
3. add to header (row 1) "Subject Area" and "Scientific Discipline" in columns D, E 
4. remove header rows (except row 1): 57, 137, 169
5. remove empty rows (search in column A)
6. fill-in the missing values (in Review Board, Subject Area, Scientific Discipline columns) - this is tedious but important, as we cannot reply on merged cells in the CSV. And it is at the core of the tree structure (@SArndt-TIB let me knows if this needs clarification)

## Join both CSVs

* just a copy-pasta
* ensure that EN comes before the DE terms
* headers should be in the following sequence: 
```
Subject Number
Subject
Review Board
Subject Area
Scientific Discipline
Fachnummer
Fach
Fachkollegium
Fachgebiet
Wissenschaftsbereich
```

