from __future__ import print_function #Python 2.X/3.X compatibility
from modules.contains_yield import Iters

if __name__ == '__main__':
    X = Iters([1,2,3,4,5])      #Make instance
    print(3 in X)               #Membership
    for i in X:                 #For loops
        print(i, end=' | ')
    print()
    print([i ** 2 for i in X])  #Other iteration objects
    print(list(map(bin, X)))

    I = iter(X)                 #Manual iteration (what other contexts do)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
