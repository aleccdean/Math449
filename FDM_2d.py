#Build A matrix
import numpy as np

def toy_problem(x,y):
    return np.sin(np.pi * x) * np.sin(np.pi * y)

def FDM(n, h):
    #Same as main but returns A, b and does not print
    U = np.zeros(n**2, dtype=object)
    x = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            U[x] = (j, i)
            x += 1
    index_map = {tuple(U[k]): k for k in range(U.shape[0])}
    A = np.zeros((U.shape[0], U.shape[0]))
    y = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            center_idx = index_map[(j, i)]
            A[y, center_idx] = 4

            if 1 <= j+1 <= n:
                A[y, index_map[(j+1, i)]] = -1
            if 1 <= j-1 <= 4:
                A[y, index_map[(j-1, i)]] = -1
            if 1 <= i+1 <= 4:
                A[y, index_map[(j, i+1)]] = -1
            if 1 <= i-1 <= 4:
                A[y, index_map[(j, i-1)]] = -1
            y += 1

    #Calculate b vec
    b = np.zeros(n**2)
    i = 0
    for node in index_map:
        b[i] = toy_problem(node[0],node[1])
        i +=1
    
    return A, b

def main(n,h):
    U = np.zeros(n**2, dtype=object)
    x = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            U[x] = (j, i)
            x += 1
    index_map = {tuple(U[k]): k for k in range(U.shape[0])}
    print(index_map)
    A = np.zeros((U.shape[0], U.shape[0]))
    y = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            center_idx = index_map[(j, i)]
            A[y, center_idx] = 4

            if 1 <= j+1 <= n:
                A[y, index_map[(j+1, i)]] = -1
            if 1 <= j-1 <= 4:
                A[y, index_map[(j-1, i)]] = -1
            if 1 <= i+1 <= 4:
                A[y, index_map[(j, i+1)]] = -1
            if 1 <= i-1 <= 4:
                A[y, index_map[(j, i-1)]] = -1
            y += 1

    print(A)

    #Calculate b vec
    b = np.zeros(n**2)
    i = 0
    for node in index_map:
        b[i] = toy_problem(node[0],node[1])
        i +=1
    
    print(f"b: {b}")

    #solve for solution vector
    sol_vec = np.linalg.solve(A, b*(h**2))
    print(f"solution vector: {sol_vec}")

def error_chart():
    return
    

if __name__ == '__main__':
    n = 4
    h = 1/n
    main(4, h)