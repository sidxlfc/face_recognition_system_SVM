import numpy
from cvxopt import solvers, matrix, mul
from PIL import Image

print "ho gaya import"

corpusroot = "./att_faces"

X = []

Z = [1. for i in range(0, 200)]

def fetch_image(path) :
	image = Image.open(path)	
	image_array = list(image.getdata())
	return image_array

def get_Z(start, end) :
	for i in range(0, 200) :
		if i < start or i > end :
			Z[i] = -1.
			continue
		Z[i] = 1.

def get_X() :
	import os
	files = [str(i) + ".pgm" for i in range(1, 6)]
	for folder in os.listdir(corpusroot) :
		for f in files :
			X.append(fetch_image(os.path.join(corpusroot + "\\" + folder, f)))
	with open('./X.txt', 'w') as f :
		f.write(str(X))

def pretty_print(object) :
	import pprint
	pp = pprint.PrettyPrinter(indent=1)
	pp.pprint(object)

get_X()

get_Z(0, 4)

B = [[0. for i in range(200)] for j in range(200)]

for i in range(0, 200) :
	B[0][i] = Z[i]

"""X = numpy.matrix(X)
X = X.astype(numpy.double)
Xt = numpy.matrix.transpose(X)
Xt = Xt.astype(numpy.double)

Z = numpy.matrix(Z)
Z = Z.astype(numpy.double)
Zt = numpy.matrix.transpose(Z)
Zt = Zt.astype(numpy.double)

A1 = X * Xt
A1 = A1.astype(numpy.double)
B1 = Z * Zt
B1 = B1.astype(numpy.double)

H = numpy.multiply(A1, B1)
H = H.astype(numpy.double)

f = -numpy.ones((200 ,1))
f = numpy.transpose(f)
f = f.astype(numpy.double)

A = -numpy.eye(200)
A = A.astype(numpy.double)

a = numpy.zeros((200, 1))
a = numpy.transpose(a)
a = a.astype(numpy.double)

B = numpy.matrix(B)
#B = B.astype(numpy.double)

b = numpy.zeros((200, 1))
b = numpy.transpose(b)
b = b.astype(numpy.double)

H = H + numpy.eye(200)*0.001
H = H.astype(numpy.double)
"""
X = matrix(X, tc = 'd')
Xt = X.trans()

Z = matrix(Z, tc = 'd')
Zt = Z.trans()

A1 = X * Xt
B1 = Z * Zt

B1 = B1.trans()

H = mul(A1, B1)

f = -matrix(1.0, (200 ,1))
f = f.trans()

A = matrix(0.0, (200, 200))
A[::4] = -1.0

a = matrix(0.0, (200, 1))
a = a.trans()

B = matrix(B)
#B = B.astype(numpy.double)

b = matrix(0.0, (200, 1))
b = b.trans()

H = H + numpy.eye(200)*0.001
H = H.astype(numpy.double)

"""print H
print f
print A
print a
print B
print b"""

Q = matrix(0.0,(3,3))
#Q[::4] = 2.0
r = matrix(0.0, (3,1))

A = matrix([[1,0],[1,1],[1,0]],(2,3),tc='d')
b = matrix([6.0, 0.0])
C = matrix([1.0, 0.0, 0.0],(1,3))
d = matrix(1.0)

sol=solvers.qp(Q, r, C, d, A, b)
print("\nSolution =\n" + str(sol['x']))



alpha = solvers.qp(matrix(H.tolist()), matrix(f.tolist()), matrix(A.tolist()), matrix(a.tolist()), matrix(B.tolist()), matrix(b.tolist()))

print alpha