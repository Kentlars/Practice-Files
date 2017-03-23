#squares_nonyield
#skipper_yield

from squares_nonyield import Squares

def pF():
    return print('-' * 30)


for i in Squares(1,5): print(i, end=' ')
else: print()
pF()

S = Squares(1, 5)
I = iter(S)
print(next(I), next(I))
J = iter(S)
print(next(J))
print(next(I))
pF()

S = Squares(1, 3)
pF()
for i in S:
    for j in S:
        print('%s:%s' % (i, j), end=' ')
    else: pF()
else: pF()


from skipper_yield import SkipObject  #This skip class has yield and iter in it
skipper = SkipObject('abcdef')
I = iter(skipper)
print(next(I), next(I), next(I))

for e in skipper:
    for y in skipper:
        print(e, y, end=' ')
else: print()
pF()
