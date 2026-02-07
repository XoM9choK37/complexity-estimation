class Number:
    count = 0
    
    def __init__(self, num):
        self.num = num
    
    
        
    def __add__(self, other):
        Number.count += 1
        return Number(self.num + other.num)
    
    def __mul__(self, other):
        Number.count += 1
        return Number(self.num * other.num)
    
    
    
    def __repr__(self):
        return str(self.num)



def inner_prod(u, v):
    prod = Number(0)
    for i in range(min(len(u), len(v))):
        prod = prod + (u[i] * v[i])
    return prod

def matrix_prod(M, N):
    for i in range():
        for j in range():
            
        



u = [Number(1), Number(-3), Number(4)]
v = [Number(2), Number(5), Number(-1)]

print(inner_prod(u, v))

print(Number.count)
