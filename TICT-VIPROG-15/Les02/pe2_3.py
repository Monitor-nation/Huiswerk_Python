""""
Voeg haakjes toe zodat de volgende expressies naar True evalueren
a. 0 == 1 == 2
b. 2 + 3 == 4 + 5 == 7
c. 1 < -1 == 3 > 4
"""

a = 0 == (1 == 2)
print(a)

b = 2 + (3 == 4) + 5 == 7
print(b)

c = (1 < -1) == (3 > 4)
print(c)