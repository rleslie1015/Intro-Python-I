x = 1

def mult2(x):
    return x * 2

print("mult2(x) = "+ str(mult2(x)))

print("x = "+ str(x)) # the value of x was never changed; x is 1. 

l = [1, 2, 3, 4]

def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2
        
print("l = "+ str(l))
print(f'l - {l}')