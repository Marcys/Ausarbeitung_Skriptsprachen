#Quelle: https://github.com/philipperoubert/sudokuSolver/blob/master/sudoku.py




#Möglichkeit um einen Randomisierungsfaktor einzubringen z.B. beim Offspring erstellen
from random import choice, random, randint
#Zur erweiterten funktionalit#t für Arrays unternaderem der möglichketi zu kopieren
import numpy as np
#zum Zeitmessen
import time
#für sysexit
import sys

from Ausarbeitung.Ausarbeitung.spiders.Dancing_Links import sudoku_array


sudoku = np.copy(sudoku_array)
ende=0
def initialisePop(grid, popNumber):
	"""
	Initalisieren der Population
	:param grid: gegebenes Gitter, welches das Programm benötigt um daraus aeine Population zubilden
	:param popNumber: Gegebene Populationsgröße
	:return: Eine Liste aller Gitter in der Population
	"""
	return [makeInd(grid) for _ in range(popNumber)]

def calculateFitnessPop(population, generation=0):
	"""
	Berechne den Fitness Score der Population
	:param population: Liste aller Gitter die die Population repräsentieren
	:param generation: Generation welche aktuell bearbeitet wird
	:return: Eine Liste aller Fitness Scores der Population
	"""
	return [calculateFitness(fitness, generation) for fitness in population]

def selectPop(population, fitness_population, populationSize):
	"""
	Wählt die ELtern für die nächste Generation
	:param population: Liste aller Gitter die die Population repräsentieren
	:param fitness_population: Eine Liste aller Fitness Scores der Population
	:param populationSize: gegeben Populaitonsgröße
	:return: Eine Liste alle Parents
	"""
	sortedPopulation = sorted(zip(population, fitness_population), key = lambda ind_fit: ind_fit[1])
	return [ individual for individual, fitness in sortedPopulation[int(populationSize * 0.5):]]

def crossoverPop(population, populationSize):
	"""
	Makes offsprings using a uniform crossover
	:param population: LListe aller Gitter die die Population repräsentieren
	:param populationSize: Dei gegeben Populaitonsgröße
	:return: Eione Liste alle neuen Offsprings
	"""
	return [ crossoverInd(choice(population), choice(population)) for _ in range(populationSize) ]

def crossoverInd(individual1, individual2):
	"""
	Wendet den Crossover Operator an um aus zwei Eltern einen Offspring jzu erstellen
	:param individual1: Parent 1
	:param individual2: Parent 2
	:return: den Offspring
	"""
	return [ list(choice(ch_pair)) for ch_pair in zip(individual1, individual2) ]

def mutatePop(population, grid):
	"""
	Mutiert jedes offspring der Population
	:param population: Liste aller Gitter die die Population repräsentieren
	:param grid: gegebenes Gitter welches das Programm lösen soll
	:return: mutierte Population
	"""
	return [ mutateInd(individual, grid) for individual in population ]

def mutateInd(individual, grid):
	"""
	Mutiert das gegebene Gitter
	:param individual: Das Gitter welches mutiert werden soll
	:param grid: Das gegebene Gitter welches das Programm lösen soll
	:return: Das mutierte Gitter
	"""
	for i in range(9):
		if (random() < 0.1):
			hasMutated = False
			while(hasMutated == False):
				rand1 = randint(0,8)
				rand2 = randint(0,8)
				if (grid[i][rand1] == 0 and grid[i][rand2] == 0):
					individual[i][rand1], individual[i][rand2] = individual[i][rand2], individual[i][rand1]
					hasMutated = True
	return list(individual)


def calculateFitness(grid, generation):
	"""
	berechnet den Fitnessscore
	:param grid: Das Grid von welchem der Score berechnet werden muss
	:param generation: aktuelle generation
	:return: The grid's fitness
	"""
	fitness = 0

	#Fitness für jede Spalte
	for i in range(9):
		L = []
		for j in range(9):
			L.append(grid[j][i])
		for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1

	#Fitness für jede Box
	L = []
	for i in range(3):
		for j in range(3):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3,6):
		for j in range(3):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(6,9):
		for j in range(3):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3):
		for j in range(3,6):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3,6):
		for j in range(3,6):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(6,9):
		for j in range(3,6):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3):
		for j in range(6,9):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3,6):
		for j in range(6,9):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(6,9):
		for j in range(6,9):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1

	#Überprüft ob eine Lösung gefunden wurde
	if (fitness/162 == 1.0):
		print()
		print("Genetic Algorithm: ")
		printSudoku(grid)
		print('Zeit: '+ str((ende - start_clock))+' Sekunden')
		sys.exit()

	return fitness/162

def makeInd(grid):
	"""
	Erstellt neues Individuum
	:param grid: Is the given grid the program needs to solve
	:return: Das Individuum
	"""
	L = []
	for i in range(9):
		possibleInt = [1,2,3,4,5,6,7,8,9]
		L.append(list(grid[i]))
		for j in range(9):
			if (L[i][j] == 0):
				hasFoundInt = False
				while(hasFoundInt == False):
					pickedInt = choice(possibleInt)
					if(pickedInt not in L[i]):
						L[i][j] = pickedInt
						possibleInt.remove(pickedInt)
						hasFoundInt = True
					else:
						possibleInt.remove(pickedInt)
	return L

def printSudoku(grid):
	global ende
	ende= time.clock()
	iteration = 0
	for i in grid:
		print(i)
		iteration += 1
	print("")

def evolve(grid, populationSize):
	"""
	Versucht eine Lösung durch weiterentwicklung zu finden
	:param grid: gegebenes Sudoku welches gelöst werden soll
	:param populationSize: Populationsgröße
	"""
	iteration = 0
	minimaFixer = 0
	population = initialisePop(grid, populationSize)
	fitnessPop = calculateFitnessPop(population)
	while (iteration < 10000):
		iteration += 1
		parentsPop = selectPop(population, fitnessPop, populationSize)
		offspringPop = crossoverPop(parentsPop, populationSize)
		population = mutatePop(offspringPop, grid)
		lastFitness = sorted(fitnessPop)[-1]
		fitnessPop = calculateFitnessPop(population, iteration)
		if (lastFitness == sorted(fitnessPop)[-1]):
			minimaFixer += 1
			if minimaFixer == 25:
				print("Minima detected... Restarting")
				population = initialisePop(grid, populationSize)
				fitnessPop = calculateFitnessPop(population)
				minimaFixer = 0
				iteration = 0
		else:
			minimaFixer = 0

start_clock = time.clock()
evolve(sudoku, 1000)

