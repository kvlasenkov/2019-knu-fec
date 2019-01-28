# implementation of gflog and gfilog tables
from timeit import timeit

gf = 256
pol = 285

gflog = {}
gfilog = {}

b = 1
for i in range(0, gf-1):
    gflog[b] = i
    gfilog[i] = b
    b <<= 1
    if b&gf :
        b = b^pol


# implementation of basic operations: addition, multiplication and division in add, mult and div functions respectively

def add(a, b) :
    return a^b

def mult (a, b) :
    if a == 0 or b == 0 :
        return 0
    else :
        return gfilog[(gflog[a] + gflog[b])%gf]

def div(a, b) :
    if a == 0 :
        return 0
    elif b == 0 :
        raise ZeroDivisionError
    else:
        c = gflog[a] - gflog[b]
        if c < 0 :
            c += gf - 1
        return gfilog[c]

if __name__ == '__main__' :
    print('108^27 run 1000000 times', timeit('add(108, 27)', 'from gf_operations import add'))
    print('108*27 run 1000000 times', timeit('mult(108, 27)', 'from gf_operations import mult'))
    print('108/27 run 1000000 times', timeit('div(108, 27)', 'from gf_operations import div'))