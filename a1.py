a = 2
print("a = ", a ,"\tid(a):",id(a))

b = 2
print("b = ", b ,"\tid(b):",id(b))

c = 1
print("c = ", c ,"\tid(c):",id(c))

a = 4
print("a = ", a ,"\tid(a):",id(a))

b = 4
print("b = ", b ,"\tid(b):",id(b))

c = 4
print("c = ", c ,"\tid(c):",id(c))

c = [1,2,3]
print("c = ", c ,"\tid(c):",id(c))

d = [1,2,3]
print("d = ", d ,"\tid(d):",id(d))

c = a
print("c = ", c ,"\tid(c):",id(c))

print("a is b",a is b)
print("a == b",a == b)
print("a is c",a is c)
print("a == c",a == c)