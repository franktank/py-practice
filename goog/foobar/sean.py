''' Doomsday Fuel =============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the
exotic matter involved. It starts as raw ore, then during processing, begins
randomly changing between forms, eventually reaching a stable form. There may be
multiple stable forms that a sample could ultimately reach, not all of which are
useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation
efficiency by predicting the end state of a given ore sample. You have carefully
studied the different structures that the ore can take and which transitions it
undergoes. It appears that, while random, the probability of each structure
transforming is fixed. That is, each time the ore is in 1 state, it has the same
probabilities of entering the next state (which might be the same state).  You
have recorded the observed transitions in a matrix. The others in the lab have
hypothesized more exotic forms that the ore can become, but you haven't seen all
of them.

Write a function answer(m) that takes an array of array of nonnegative ints
representing how many times that state has gone to the next state and return an
array of ints for each terminal state giving the exact probabilities of each
terminal state, represented as the numerator for each state, then the
denominator for all of them at the end and in simplest form. The matrix is at
most 10 by 10. It is guaranteed that no matter which state the ore is in, there
is a path from that state to a terminal state. That is, the processing will
always eventually end in a stable state. The ore starts in state 0. The
denominator will fit within a signed 32-bit integer during the calculation, as
long as the fraction is simplified regularly.

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
'''

import fractions

def answer(m):
	'''
	Markov Abosrbing Chain method:

	To apply this method, we first get a matrix split into four sections:
	[ identity matrix | zero matrix
	  R matrix		| Q matrix ]

	We want to find a limiting matrix, FR. where F = (I-Q)^-1
	'''
	if len(m) == 1:
		return [1,1]

	ordering = []
	terminal_states, non_terminal_states = find_terminal_nonterminal_states(m)
	ordering += terminal_states + non_terminal_states

	identity_matrix = construct_identity_matrix(len(terminal_states))
	zero_matrix = construct_zero_matrix(len(non_terminal_states))
	R_matrix, Q_matrix = construct_R_Q_matrix(non_terminal_states, m, ordering)
	F_matrix = construct_F_matrix(Q_matrix)

	limiting_matrix = multiply_matrix(F_matrix, R_matrix)
	print('lol')
	answer = limiting_matrix[0]
	for i in range(len(answer)):
		answer[i] = fractions.Fraction(answer[i]).limit_denominator()

	common_denominator = gcd(answer).denominator

	for i in range(len(answer)):
		curr_denom = answer[i].denominator
		answer[i] = answer[i].numerator * (common_denominator/curr_denom)

	answer.append(common_denominator)
	return answer

def gcd(my_list):
	'''
	computes gcd of a set of numbers
	'''
	return reduce(fractions.gcd, my_list)

def multiply_matrix(matrix_a, matrix_b):
	'''
	multiply matrix A with matrix B
	'''

	cols_a = len(matrix_a[0])
	cols_b = len(matrix_b[0])

	result = [[float(0)] * cols_b for _ in range(len(matrix_a))]

	for i in range(len(matrix_a)):
		for j in range(cols_b):
			for k in range(cols_a):
				result[i][j] += matrix_a[i][k] * matrix_b[k][j]

	return result

def subtract_matrix(matrix_a, matrix_b):
	'''
	Subtraction: matrix_a - matrix_b
	'''
	result = [[float(0)] * len(matrix_a) for _ in range(len(matrix_a))]

	for i in range(len(matrix_a)):
		for j in range(len(matrix_a[i])):
			result[i][j] = matrix_a[i][j] - matrix_b[i][j]

	return result


def construct_F_matrix(Q_matrix):
	identity_matrix = construct_identity_matrix(len(Q_matrix))
	F_matrix = subtract_matrix(identity_matrix, Q_matrix)
	F_matrix = get_matrix_inverse(F_matrix)
	return F_matrix

def construct_R_Q_matrix(non_terminal_states, m, ordering):
	'''
	Use splicing and mapping to get R and Q matrices
	'''
	bottom_half_matrix = []
	for non_terminal_state in non_terminal_states:
		curr_row = [float(0)] * len(m)
		paths = m[non_terminal_state] # get original mapping of what paths this state will take

		# using the new ordering, create new rows/rearrange indices from old paths
		for i in range(len(ordering)):
			order_index = ordering[i]
			curr_row[i] = paths[order_index]

		bottom_half_matrix.append(curr_row)

	for i in range(len(bottom_half_matrix)):
		row = bottom_half_matrix[i]
		row_total = float(sum(row))
		for j in range(len(row)):
			bottom_half_matrix[i][j] /= row_total

	terminal_state_count = len(m) - len(non_terminal_states)
	non_terminal_state_count = len(non_terminal_states)

	R_matrix = [bottom_half_matrix[i][0:terminal_state_count] for i in range(non_terminal_state_count)]
	Q_matrix = [bottom_half_matrix[i][terminal_state_count:] for i in range(non_terminal_state_count)]

	return R_matrix, Q_matrix


def construct_zero_matrix(size):
	'''
	Create a zero matrix given a size
	'''
	zero_matrix = [[float(0)] * size for _ in range(size)]
	return zero_matrix


def construct_identity_matrix(size):
	'''
	Create an identity matrix given a size
	'''
	identity_matrix = []
	for i in range(size):
		curr_row = [float(0)] * size
		curr_row[i] = 1

		identity_matrix.append(curr_row)

	return identity_matrix


def find_terminal_nonterminal_states(m):
	'''
	find indices of terminal/nonterminal states
	'''
	terminal_states = []
	non_terminal_states = []

	for i in range(len(m)):
		state = m[i]
		if all(value == 0 for value in state):
			terminal_states.append(i)
		else:
			non_terminal_states.append(i)

	return terminal_states, non_terminal_states


'''
helper functions to get matrix inversion
Steps to get matrix inversion from: mathisfun.com
Credit for matrix inversion without numpy: https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
'''
def get_matrix_determinant(m):
	#base case for 2x2 matrix
	if len(m) == 2:
		return m[0][0]*m[1][1]-m[0][1]*m[1][0]

	determinant = 0
	for c in range(len(m)):
		determinant += ((-1)**c)*m[0][c]*get_matrix_determinant(get_matrix_minor(m,0,c))
	return determinant


def transpose_matrix(m):
	'''
	take transpose of matrix
	'''
	t = []
	for r in range(len(m)):
		tRow = []
		for c in range(len(m[r])):
			if c == r:
				tRow.append(m[r][c])
			else:
				tRow.append(m[c][r])
		t.append(tRow)
	return t


def get_matrix_minor(m, i, j):
	return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def get_matrix_inverse(m):
	determinant = get_matrix_determinant(m)
	#special case for 2x2 matrix:
	if len(m) == 2:
		return [[m[1][1]/determinant, -1*m[0][1]/determinant],
				[-1*m[1][0]/determinant, m[0][0]/determinant]]

	#find matrix of cofactors
	cofactors = []
	for r in range(len(m)):
		cofactorRow = []
		for c in range(len(m)):
			minor = get_matrix_minor(m,r,c)
			cofactorRow.append(((-1)**(r+c)) * get_matrix_determinant(minor))
		cofactors.append(cofactorRow)
	cofactors = transpose_matrix(cofactors)
	for r in range(len(cofactors)):
		for c in range(len(cofactors)):
			cofactors[r][c] = cofactors[r][c]/determinant

	return cofactors


m = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]

print(answer(m))
