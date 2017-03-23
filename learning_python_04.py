
#virker
#L = ['abc', 'ABD', 'aBe']
#L.sort()
#print(L)
#virker ikke
#D# = ['abc', 'ABD', 'aBe']
#D = D.sort(key=str.lower)
#print(D)
#virker ikke
#L = ['abc', 'ABD', 'aBe']
#L = L.sort(reverse=True)
#print(L)
#virker
#L = ['abc', 'ABD', 'aBe']
#print(sorted([x.lower() for x in L], reverse=True)
##virker ikke
#rint (L.reverse())
#virker
#L.pop()
#L.insert(1, 'toast')
#print L
#print list(reversed(L))
#del L[1:]
#print L
#pop method LIFO (Last In First Out)
#dictionary.update virker paa samme maate som list.append(ting)
#D = {'eggs': 3, 'spam': 2, 'ham': 1}
#D2 = {'toast': 4, 'muffin': 5}
#D.update(D2)
#print D

# ///Dictionary///
table = {'1975': 'Holy Grail',
        '1979': 'Life of Brian',
        '1983': 'The Meaning of Life'}
year = '1983'
movie = table[year]
#print movie

#for key in dictionary
for year in table:
    print(year + '\t' + table[year])
#printer verdiene
#print list(table.items())
#print list(table.keys())
#print list(table.values())

#virker ikke
print([title for (title, year) in table.items() if year == '1975'])
c = [title for (title, year) in table.items() if year == '1975']
V = '1975'
[key for key in table.keys() if table[key] == V]
[key for (key, value) in table.items() if value == V]
Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99
X = 2; Y = 3; Z = 4
print(Matrix[(X, Y, Z)])
if (2,3,6) in Matrix:
    print(Matrix[(2,3,6)])
else:
    print(0)
try:
    print(Matrix[(2,3,6)])
except KeyError:
    print(0)
print(Matrix.get((2,3,6), 0))

rec = {'name': 'Bob',
    'jobs': ['developer', 'manager'],
    'web': 'wwww.bobs.org/bob',
    'home': {'state': 'Overworked', 'zip': 12345}
    }

print(rec ['jobs'][1])
print(rec['home']['zip'])
print(dict.fromkeys(['a', 'b'], 0))
L =['Bob', 40.5, ['dev', 'mgr']]
print(L[0])
print(L[1])
print(L[2][1])
D = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
print(D['name'])
print(D['age'])
print(D['jobs'][1])

D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(D['name'])
D['jobs'].remove('mgr')
print(D)
print({x: x**2 for x in [1,2,3,4]})
print({c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']})
C = dict(a=1, b=2, c=3)
print(list(C.items())[0]) #('c', 3)
print(list(C.values())[0])#3
print(list(C.keys())[0])#c
for k in C.keys():
    print(k)
K = C.keys()
V = D.values()
print(K | {'x': 4})
#print(V & {'x': 4}.values())

print(C.keys() & {'b': 1})
