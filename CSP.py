#zum kopieren des Arrays
import numpy as np
#zum messen der Zeit
import time
#Verkettung zum ausführen aller Sudokus
from Ausarbeitung.Ausarbeitung.spiders.Backtracking import sudoku_array
#berechnet das Kartesische Produkt
from itertools import product
#Damit änderungen nicht das Orginal verändern
from copy import deepcopy


def solve(sudoku):
    """
    Löst das Sudoku und gibt dieses dann zurück
    :param sudoku: das Sudoku welches gelöst werden soll
    :return: gelöstes Sudoku
    """
    local_sudoku = np.array(sudoku)
    # Initialisierung
    pre_values = {key:list(range(1,10)) for key in product(range(9), range(9)) if local_sudoku[key]==0} #Erstellt ein dictonary mit den für jede Einheit Möglichen Werten
    value_scope = {key:calculate_scope(local_sudoku, *key) for key in product(range(9), range(9))}# Wir bekommen die Werte die von der entsprechenden Einheit "gesehen" werden
    for key in product(range(9), range(9)):
        if local_sudoku[key]:
            delete(pre_values, value_scope, local_sudoku[key], key, start=True)
    deep = 0
    solved_sudoku = False
    copy_sudoku = []

    while True:
        changes = False
        for key in set(pre_values.keys()):
            if len(pre_values[key]) > 1 and deep:
                pre_values[key] = check_scope(pre_values, value_scope, key)
            if len(pre_values[key]) == 1:
                changes = True
                local_sudoku[key] = pre_values.pop(key)[0]
                delete(pre_values, value_scope, local_sudoku[key], key)
            elif not pre_values[key]: # Kollision
                if len(copy_sudoku) > 0: #zurück zum letzten Zustand
                    local_sudoku, pre_values, value_scope = copy_sudoku.pop()
                elif solved_sudoku: #Lösung gefunden
                    return solved_sudoku

        if not changes:
            if deep > 1:
                temp, pre_values[key] = pre_values[key][0], pre_values[key][1:]
                copy_sudoku.append((local_sudoku.copy(), deepcopy(pre_values), deepcopy(value_scope)))
                pre_values[key] = [temp]
            else:
                deep += 1
        else:
            deep = 0

        if not pre_values:

                return local_sudoku.tolist()


def calculate_scope(locale_sudoku, n, m):
    """
    Berechne die Koordinaten der Zeile, Spalte und Reihe

    :param locale_sudoku: Das Sudoku welches gelöst werden soll
    :param n: Index
    :param m: Index
    :return: Koordinaten der Zeile Spalte und Gitter
    """
    dk = ((0,1,2),(3,4,5),(6,7,8))
    row = [(n,j) for j in range(9) if locale_sudoku[n, j] == 0 and (n, j) != (n, m)]
    column = [(i,m) for i in range(9) if locale_sudoku[i, m] == 0 and (i, m) != (n, m)]
    grid = [(i,j) for i in dk[n//3] for j in dk[m//3] if locale_sudoku[i, j] == 0 and (i, j) != (n, m)]
    return (row, column, grid)


def delete(possible_values, value_scope, x, key, start=False):
    """
    Lösche Werte für 3x3 Grid, Zeile und Spalte sowie für die entsprechenden Einheiten im value_scope
    :param possible_values: dict mit möglichen Werten
    :param value_scope: "gesehene" Werte
    :param x: index
    :param key: dict
    :param start: False
    :return:
    """
    row, column, grid = value_scope.pop(key)
    for k in set(row+column+grid):
        if x in possible_values[k]:
            possible_values[k].remove(x)
        if not start:
            if k in row:
                value_scope[k][0].remove(key)
            if k in column:
                value_scope[k][1].remove(key)
            if k in grid:
                value_scope[k][2].remove(key)



def check_scope(possible_values, value_scope, key):
    """
    Überprüfen ob wir nur noch einen möglichen Wert haben

    :param possible_values: gleiche
    :param value_scope: gleiche
    :param key: dict
    :return:gefundenen Wert
    """
    row, column, grid = value_scope[key]
    digits = possible_values[key]
    pot1 = sum([possible_values[k] for k in row], [])
    pot2 = sum([possible_values[k] for k in column], [])
    pot3 = sum([possible_values[k] for k in grid], [])
    found1 = list(filter(lambda x: pot1.count(x)==0, digits))
    found2 = list(filter(lambda x: pot2.count(x)==0, digits))
    found3 = list(filter(lambda x: pot3.count(x)==0, digits))
    found = max(found1, found2, found3)
    if len(found) > 1: #zurück zum voherigen
        return []
    elif len(found) == 1:
        return found

    return digits



#Ausgabe und Zeitmessung
sudoku= np.copy(sudoku_array)
print("Algorithmus CSP: ")
start_clock = time.clock()
test=solve(sudoku)
ende= time.clock()
for i in range(9):
    singleitem = test[i]
    print(singleitem)
print('Zeit: '+ str((ende - start_clock))+' Sekunden')
print()

