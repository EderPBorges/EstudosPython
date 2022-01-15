#!python3

from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))

getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print(Decimal.max(Decimal(1), Decimal(7)))
print(dir(Decimal))

1.1 + 2.2
getcontext().prec = 5
print(Decimal(1.1) + Decimal(2.2))