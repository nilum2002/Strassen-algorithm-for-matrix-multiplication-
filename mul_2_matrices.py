import numpy as np



def split(matrix):
    n = len(matrix)
    return  matrix[:n//2, :n//2],matrix[:n//2, n//2:], matrix[n//2:, :n//2], matrix[n//2:, n//2:]

def brute_force(A, B):
    res = np.array([[0]*B.shape[1] for i in range(A.shape[0])])
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[0]):
                res[i][j] += A[i][k]* B[k][j]
    return res
def strassen2(A, B):
    if (len(A)<= 2):
        return brute_force(A, B)
    a, b, c, d = split(A)
    e, f, g, h = split(B)
    AE = strassen2(a,e)
    BG = strassen2(b, g)
    AF = strassen2(a, f)
    BH = strassen2(b, h)
    CE = strassen2(c, e)
    DG = strassen2(d, g)
    CF = strassen2(c, f)
    DH = strassen2(d, h)
    
    C11 = AE + BG
    C12 = AF + BH
    C21 = CE+ DG
    C22 = CF + DH
    c = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return c
    
matrix01 = np.array([ [1,  2,  3,  4], 
                    [5,  6,  7,  8], 
                    [9, 10, 11, 12], 
                    [13, 14, 15, 16]
                    ])
matrix02 = np.array([ [0,  1,  2,  3], 
                    [4,  5,  6,  7], 
                    [8, 9, 10, 11], 
                    [12, 13, 14, 15]
                    ])

print("Matrix Multiplication is : ")
print(strassen2(matrix01, matrix02))
# Note that this method only works for only even numbers of row and column matrices. (It means this works for even square matrices)
# The new updated code will be soon... 


