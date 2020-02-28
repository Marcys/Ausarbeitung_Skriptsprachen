import numpy as np
from Ausarbeitung.Ausarbeitung.spiders.CSP import sudoku_array
import time

class Root:
	def __init__(self):
		self.R=None
		self.L=None

class Column:
	def __init__(self):
		self.R=None
		self.L=None
		self.U=None
		self.D=None
		self.S=0
		self.N=""

class Node:
	def __init__(self):
		self.R=None
		self.L=None
		self.U=None
		self.D=None
		self.C=None

def mat2linklist(A, column_names=None):
	"""
	Verkettete Liste erstellen
	:param A: Grid der Constraints
	:param column_names: lokale verwendung
	:return: root Objekt
	"""
	root = Root()
	tmp1 = root
	r_n,c_n = A.shape
	nodes = [None] * c_n
	for j in range(c_n):
		column_header = Column()
		if column_names:
			column_header.N = column_names[j]
		else:
			column_header.N = j
		tmp2 = column_header
		tmp1.R = column_header
		column_header.L = tmp1
		tmp1 = column_header
		column = [None] * r_n
		for i in range(r_n):
			if A[i,j] == 1:
				column_header.S += 1
				node = Node()
				column[i] = node
				node.C = column_header
				tmp2.D = node
				node.U = tmp2
				tmp2 = node
		nodes[j] = column
		tmp2.D = column_header
		column_header.U = tmp2

	tmp1.R=root
	root.L=tmp1

	for i in range(r_n):
		for j in range(c_n):
			if A[i,j] == 1:
				tmp = nodes[j][i]
				# keeps searching the next 1 on the right
				for k in range(1, c_n+1):
					if A[i, np.mod(j+k, c_n)]==1:
						node_r = nodes[np.mod(j+k,c_n)][i]
						tmp.R = node_r
						node_r.L = tmp
						tmp = node_r
				break
	return root


temp_solutions=[] # verübergehende Lösungen
solutions = [] # Finale Lösung

def cover_column(column_header):
	"""
	verdeckt den Spalten kopf
	:param column_header: Spalten_kopf
	:return:
	"""
	column_header.R.L = column_header.L
	column_header.L.R = column_header.R

	i = column_header.D
	while i is not column_header:
		j = i.R
		while j is not i:
			j.D.U = j.U
			j.U.D = j.D
			j.C.S -= 1
			j = j.R
		i = i.D


def uncover_column(column_header):
	"""
	uncovert den Spalten kopf
	:param column_header: spalten Kopf
	:return:
	"""
	i = column_header.U
	while i is not column_header:
		j = i.L
		while j is not i:
			j.D.U = j
			j.U.D = j
			j.C.S += 1
			j = j.L
		i = i.U
	column_header.R.L = column_header
	column_header.L.R = column_header



def search(root):
	"""
	Rekursive Suche nach der Lösung
	:param root: Root Objekt
	:return: 0
	"""
	global solutions
	if root.R is root:
		for O in temp_solutions:
			solution = [O.C.N]
			node = O.R
			while node is not O:
				solution.append(node.C.N)
				node = node.R
			solutions.append(solution)
			# print(solution)
		return 0

	c = root.R
	cover_column(c)
	r = c.D
	while r is not c:
		temp_solutions.append(r)
		j = r.R
		while j is not r:
			cover_column(j.C)
			j = j.R
		search(root)
		r = temp_solutions.pop()
		c = r.C
		j = r.L
		while j is not r:
			uncover_column(j.C)
			j = j.L
		r = r.D
	uncover_column(c)
	return 1




def sudoku2exact_cover(A):
	"""
	Darstellen als exact cover
	:param A: Grid der Constraints
	:return:exact cover
	"""
	exact_cover_mat = []
	for i in range(N):
		for j in range(N):
			if A[i,j] != 0:
				exact_cover_mat.append(row_generator(A[i,j], i, j))
			else:

				for n in valid_list(A, i, j):
					exact_cover_mat.append(row_generator(n, i, j))
	exact_cover_mat = np.array(exact_cover_mat)
	print(exact_cover_mat)
	return exact_cover_mat

def row_generator(n, i, j):
	"""
	Generiert eine Zeile
	:param n: Werte
	:param i: index
	:param j: index
	:return: Zeile
	"""
	row = [0]*4*N*N
	index1 = i*N+j
	index2 = N*N-1 + N*j + n
	index3 = 2*N*N-1 + N*i + n
	index4 = 3*N*N-1 + N*block(i, j) + n
	row[index1] = 1
	row[index2] = 1
	row[index3] = 1
	row[index4] = 1
	return row

def block(i, j):
	"""
	berechnet det block Index
	:param i:index
	:param j: index
	:return: block index
	"""
	return int(i/N_sqrt)*int(N_sqrt)\
		+int(j/N_sqrt)

def valid_list(A,i,j):
	"""
	erfasst gültige und ungültige Liste
	:param A: Grid der Constraints
	:param i:index
	:param j: index
	:return: Gibt eine Liste zurück welche sich nicht in nonvalid befindet
	"""
	nonvalid = []
	for x in A[i,:]:
		if x != 0:
			nonvalid.append(x)
	for x in A[:,j]:
		if x != 0:
			nonvalid.append(x)

	b = block(i, j)
	jb = np.mod(b, N_sqrt) * N_sqrt
	ib = int(b/N_sqrt) * N_sqrt

	all_ii = [ib+x for x in range(N_sqrt)]
	all_jj = [jb+x for x in range(N_sqrt)]
	for ii in all_ii:
		for jj in all_jj:
			nonvalid.append(A[ii,jj])
	return [x for x in range(1,N+1) if x not in nonvalid]

def translateback(row):
	"""
	übernimmt formatierung um Werte zuzuweisen
	:param row: Zeile
	:return: Wert im Sudoku
	"""
	index = row[0]
	i = int(index/N)
	j = np.mod(index, N)
	n = row[1] - N*N+1 - N*j
	return (i, j, index, n)




print("Algorithmus DancingLinks: ")
start_clock = time.clock()
Sudoku  = np.copy(sudoku_array)
N=len(Sudoku) # N*N sudoku
N_sqrt = int(np.sqrt(N))
A = sudoku2exact_cover(Sudoku)
root = mat2linklist(A)
search(root)
ende= time.clock()

k=1
ans = Sudoku[:]
for row in solutions:
    i,j,index, n = translateback(row)
    ans[i,j]=n


print(ans)
print('Zeit: '+ str((ende - start_clock))+' Sekunden')
print()
