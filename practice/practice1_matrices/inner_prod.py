def inner_prod(u, v, n):
    prod = 0
    for i in range(n):
        prod += u[i] * v[i]
    return prod
