L = list(range(100))
print(L[1:10])
for ch in 'ABC':
   print(ch)
for x, y in [(1, 1), (2, 4), (3, 9)]:  
      print(x, y)
L=[]
for x in range(1,11):
    L.append(x)
print(L)
Y = [x*x for x in range(1)]
print(Y)
Z=[m + n for m in 'ABC' for n in 'XYZ']
print(Z)
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

