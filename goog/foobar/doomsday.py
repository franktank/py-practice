import numpy as np
from functools import reduce
def answer(m):
"""
Find terminal and non terminal states
Build identity matrix
Build R, Q matrix
Build F matrix
Caluclate limiting matrix with F and R matrix
"""
m = np.array(m)
ts = np.where(~m.any(axis=1))[0]
nts = np.where(m.any(axis=1))[0]
new_order = np.concatenate((ts,nts))
rearrange_m = m[:, new_order][new_order]
r_matrix = rearrange_m[len(rearrange_m)-len(nts):, :len(ts)]
q_matrix = rearrange_m[len(rearrange_m)-len(nts):, len(ts):]
identity_m = np.identity(len(q_matrix))
f = np.linalg.inv(identity_m - q_matrix)
limiting_matrix = np.dot(f,r_matrix)
res = []
for i in range(len(limiting_matrix[0])):
	res.append(fractions.Fraction(limiting_matrix[0][i]).limit_denominator())

cd = reduce(fractions.gcd, res).denominator
for i in range(len(res)):
	curr_denom = res[i].denominator
	res[i] = res[i].numerator * (common_denominator/curr_denom)

res.append(cd)
return res
