import fractions
def answer(m):
	if len(m) == 1:
		return [1,1]

	new_order = []
	ts, nts= get_terminal_and_nonterminal_states(m)
	new_order += ts + nts
	r_matrix, q_matrix = get_r_and_q_matrices(nts, m, new_order)
	f_matrix = get_f_mat(q_matrix)
	limiting_matrix = multiply_matrix(f_matrix, r_matrix)

	res = limiting_matrix[0]
	for i in range(len(res)):
		res[i] = fractions.Fraction(res[i]).limit_denominator()

	cd = reduce(fractions.gcd, res).denominator

	for i in range(len(res)):
		curr_denom = res[i].denominator
		res[i] = res[i].numerator * (cd/curr_denom)

	res.append(cd)
	return res

def get_terminal_and_nonterminal_states(m):
	'''
	find indices of terminal/nonterminal states
	'''
	ts = []
	nts = []

	for i in range(len(m)):
		state = m[i]
		if all(value == 0 for value in state):
			ts.append(i)
		else:
			nts.append(i)

	return ts, nts

def gcd(l):
	return reduce(fractions.gcd, l)

def multiply_matrix(matrix_a, matrix_b):
	cols_a = len(matrix_a[0])
	cols_b = len(matrix_b[0])

	result = [[float(0)] * cols_b for _ in range(len(matrix_a))]

	for i in range(len(matrix_a)):
		for j in range(cols_b):
			for k in range(cols_a):
				result[i][j] += matrix_a[i][k] * matrix_b[k][j]

	return result

def subtract_matrix(matrix_a, matrix_b):
	result = [[float(0)] * len(matrix_a) for _ in range(len(matrix_a))]

	for i in range(len(matrix_a)):
		for j in range(len(matrix_a[i])):
			result[i][j] = matrix_a[i][j] - matrix_b[i][j]

	return result


def get_f_mat(Q_matrix):
	identity_matrix = get_identity(len(Q_matrix))
	f_matrix = subtract_matrix(identity_matrix, Q_matrix)
	f_matrix = get_matrix_inverse(F_matrix)
	return f_matrix

def get_r_and_q_matrices(nts, m, new_order):
	nts_side_matrix = []
	for non_terminal_state in nts:
		curr_row = [float(0)] * len(m)
		paths = m[non_terminal_state]

		for i in range(len(new_order)):
			order_index = new_order[i]
			curr_row[i] = paths[order_index]

		nts_side_matrix.append(curr_row)

	for i in range(len(nts_side_matrix)):
		row = nts_side_matrix[i]
		row_total = float(sum(row))
		for j in range(len(row)):
			nts_side_matrix[i][j] /= row_total

	ts_length = len(m) - len(nts)
	nts_length = len(nts)

	r_matrix = [nts_side_matrix[i][0:ts_length] for i in range(nts_length)]
	q_matrix = [nts_side_matrix[i][ts_length:] for i in range(nts_length)]

	return r_matrix, q_matrix


def get_zeros(size):
	zero_m = [[float(0)] * size for _ in range(size)]
	return zero_m


def get_identity(size):
	identity_m = []
	for i in range(size):
		curr_row = [float(0)] * size
		curr_row[i] = 1

		identity_m.append(curr_row)

	return identity_m

"""
Obtained code from https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
"""
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
