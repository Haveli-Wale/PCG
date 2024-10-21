# Generate all possible combinations in only 6 digits
a = "0983"
from itertools import product

combinations = [''.join(p) for p in product('0123456789', repeat=6)]
for combination in combinations:
    b = combination
    c = b+a
    if c[0]=="6":
        print(c)
    elif c[0]=="7":
    elif c[0]=="7":
        print(c)
    elif c[0]=="8":
        print(c)
    elif c[0]=="9":
        print(c)
    else:
        pass