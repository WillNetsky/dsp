# Matrix Algebra
# Work done by hand is in Scan.jpeg and Scan 1.jpeg

import numpy as np

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

# Part 1
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(w.shape)

# Part 2
print(u+v)
print(u-v)
print(6*u)
print(u.dot(v))
print(np.linalg.norm(u))

# Part 3
try:
    print(A + C)
except ValueError:
    print("Not defined")
print(A - C.T)
print(C.T + 3*D)
print(B.dot(A))
try:
    print(B.dot(A.T))
except ValueError:
    print("Not defined")

# Optional Part
try:
    print(B.dot(C))
except ValueError:
    print("Not defined")
print(C.dot(B))
print(B.dot(B).dot(B).dot(B))
print(A.dot(A.T))
print(D.T.dot(D))
