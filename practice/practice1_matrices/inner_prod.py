from random import randint

def main():
    n = int(input())
    u = [0 for i in range(n)]
    v = [0 for i in range(n)]
    for i in range(n):
        u[i] = randint(-10, 10)
        v[i] = randint(-10, 10)
    print(u, v, inner_prod(u, v, n), sep='\n')
    
    m = int(input())
    p = int(input())
    n = int(input())
    a = [[0 for i in range(p)] for j in range(m)]
    b = [[0 for i in range(n)] for j in range(p)]
    for i in range(m):
        for j in range(p):
            a[i][j] = randint(-10, 10)
    for i in range(p):
        for j in range(n):
            b[i][j] = randint(-10, 10)
    print(a, b, matrix_prod(a, b, m, p, n), sep='\n')



def inner_prod(u, v, n):
    prod = 0
    for i in range(n):
        prod += u[i] * v[i]
    return prod

def matrix_prod(a, b, m, p, n):
    c = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]
    return c



if __name__ == "__main__":
    main()
