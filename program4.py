from typing import List
import math

def add(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Helper function to add two matrices."""
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def sub(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Helper function to subtract two matrices."""
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def strassen_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    m = 2 ** math.ceil(math.log2(n))
    if m != n:
        A_pad = [[0] * m for _ in range(m)]
        B_pad = [[0] * m for _ in range(m)]
        
        for i in range(n):
            for j in range(n):
                A_pad[i][j] = A[i][j]
                B_pad[i][j] = B[i][j]
                
        C_pad = strassen_multiply(A_pad, B_pad)
        
        return [row[:n] for row in C_pad[:n]]

    mid = n // 2
    
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    P1 = strassen_multiply(add(A11, A22), add(B11, B22))
    P2 = strassen_multiply(add(A21, A22), B11)
    P3 = strassen_multiply(A11, sub(B12, B22))
    P4 = strassen_multiply(A22, sub(B21, B11))
    P5 = strassen_multiply(add(A11, A12), B22)
    P6 = strassen_multiply(sub(A21, A11), add(B11, B12))
    P7 = strassen_multiply(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(P1, P4), P5), P7)
    C12 = add(P3, P5)
    C21 = add(P2, P4)
    C22 = add(add(sub(P1, P2), P3), P6)

    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C


if __name__ == "__main__":
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    product = strassen_multiply(m1, m2) 
    print(f"ans: {product}")
    