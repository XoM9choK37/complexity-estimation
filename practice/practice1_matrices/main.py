from random import randint

from inner_prod import inner_prod
from matrix_prod import matrix_prod
from sorts import insertion_sort, selection_sort, bubble_sort

def main():
    n = int(input())
    u = [randint(-10, 10) for i in range(n)]
    v = [randint(-10, 10) for i in range(n)]
    print(u, v, inner_prod(u, v, n), sep='\n')
    
    m = int(input())
    p = int(input())
    n = int(input())
    a = [[randint(-10, 10) for i in range(p)] for j in range(m)]
    b = [[randint(-10, 10) for i in range(n)] for j in range(p)]
    print(a, b, matrix_prod(a, b, m, p, n), sep='\n')
    
    n = int(input())
    x = [randint(-10, 10) for i in range(n)]
    y = [randint(-10, 10) for i in range(n)]
    z = [randint(-10, 10) for i in range(n)]
    print(x, y, z)
    print(x, y, z, insertion_sort(x), selection_sort(y), bubble_sort(z), sep='\n')



if __name__ == "__main__":
    main()
