from functools import *
lst = [ 2, 3, 8, 4, 1, 6, 9, 7]
evens = list (filter (lambda n : n % 2 == 0, lst))
doubles = list (map (lambda n : n * 2, evens))
sum = reduce (lambda a, b : a + b, doubles)
print (evens)
print (doubles)
print (sum)

