from modules.adder import Number as numb, Callee, Prod, CallBack, Comparisons as c

x = numb(4)
x += 1
x += 1
print(x.data)

y = numb([4])
y += [1]
print(y.data)

x = Callee()
x(1,2,3,4)
x(*[1,2], **dict(c=3, d=4))
print(x)

x = Prod(3)
x(4)
print(x)
print(x(4))

x = CallBack('blue')
cb4 = (lambda color='red': 'turn '+ color)
print(cb4())

x = c()
print(x < 'ham')
print(x > 'ham')
