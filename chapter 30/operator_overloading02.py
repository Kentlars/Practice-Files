from squares import Squares, gsquares, SquaresYield
from skipobject import SkipObject, gen

for i in Squares(1, 5):
    print(i, end=' ')
else: print()

X = Squares(1,5)
I = iter(X)
print(next(I), next(I))

X = Squares(1, 5)
print(list(X)[1])

for i in gsquares(1, 5):
    print(i, end=' ')

S = 'ace'
for x in S:
    for y in S:
        print(x + y, end='\n')
print('-' * 30)


if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha) #Make a container object
    I = iter(skipper) #Make an iterator on it
    print(next(I), next(I), next(I)) #Visit offsets 0,2,4

    for x in skipper: #for calles __iter__ automatically
        for y in skipper: #Nested fors call __iter__ again each time
            for c in skipper:
                print('%s%s%s' %(x, y, c), end='...') #Each iterator has its own state, offset
    else: print()


    S = 'abcdef' #We can achieve similar results with built-in tools
    for x in S[::2]:
        for y in S[::2]:
            print(x + y, end=' ')
    else: print()

S = SquaresYield(1, 5)
I = iter(S)
print(next(I), next(I))
J = iter(S)
print(next(J), next(I))
