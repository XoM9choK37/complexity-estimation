from random import randint

from inner_prod import inner_prod
from matrix_prod import matrix_prod
from sorts import insertion_sort, selection_sort, bubble_sort

def main():
    n = int(input())
    u = [randint(-10, 10) for i in range(n)]
    v = [randint(-10, 10) for i in range(n)]
    print(u, v, inner_prod(u, v, n), sep='\n')
    
    a = [[randint(-10, 10) for i in range(n)] for j in range(n)]
    b = [[randint(-10, 10) for i in range(n)] for j in range(n)]
    print(a, b, matrix_prod(a, b, n), sep='\n')
    
    x = [randint(-10, 10) for i in range(n)]
    y = [randint(-10, 10) for i in range(n)]
    z = [randint(-10, 10) for i in range(n)]
    print(x, y, z)
    print(x, y, z, insertion_sort(x, n), selection_sort(y, n), bubble_sort(z, n), sep='\n')



if __name__ == "__main__":
    main()
