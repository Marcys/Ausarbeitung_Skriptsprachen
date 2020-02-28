import time
import numpy as np


from Ausarbeitung.Ausarbeitung.spiders.Getter import sudoku_array
sudoku = np.copy(sudoku_array)


start=0
length = 9
def solve(index):
    """

    :param index: Index
    :return: rekursiver Aufruf oder gelöstes Sudoku
    """

    if (index >80):
        return sudoku

    rowIndex = int(index/length)
    columnIndex = index % length

    if  sudoku[rowIndex][columnIndex] != 0:
        return solve(index+1)

    for input in range (1,10):
        if checking(rowIndex, columnIndex, input):
            sudoku[rowIndex][columnIndex] = input
            if not solve(index + 1) is None:
                return sudoku
            sudoku[rowIndex][columnIndex]=0

    return None


def checking(row, column, value):
    """
    Überprüft ob Wert gültig ist
    :param row: Index der Zeile
    :param column:  Index der Spalte
    :param value:
    :return: True: wenn gültig andernfalls False
    """
    for i in range (9):

        if sudoku[row][i] == value:
            return False

        if (sudoku[i][column] == value):
            return False

        unit_row = row-row % 3
        unit_column = column - column % 3

        for rowIndex in range(unit_row,unit_row+3):
            for columnIndex in range(unit_column, unit_column +3):
                if(sudoku[rowIndex][columnIndex]) == value:
                     return False
    return True


print("Algorithmus einfaches Backtracking:")
start_clock = time.clock()
solve(start)
ende= time.clock()
print(sudoku)
print('Zeit: '+ str((ende - start_clock))+' Sekunden')
print()



