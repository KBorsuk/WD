def arytm(a1= 1, r=1, ile=10):
    return sum([a1+i*r for i in range(ile)])

print(arytm())
print(arytm(3,6,8))
print(arytm(ile=40,a1=61))