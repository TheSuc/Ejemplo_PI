"""
Calculando PI  3.14159265358979323846
"""
sum = 0
a = 0
# Problema de Basilea****
for i in range(1,10000000):
	a = 1/((i)**2)
	sum = sum + a
#***********************
pi = (sum*6)**0.5
print(pi)