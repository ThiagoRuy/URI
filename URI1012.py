A,B,C =input().split()
A = float(A)
B = float(B)
C = float(C)
AT = (A*C)/2
AC = 3.14159*C**2
ATP = (A+B)*C/2
AQ = B**2
AR = A*B
print("TRIANGULO: {:.3f}".format(AT))
print("CIRCULO: {:.3f}".format(AC))
print("TRAPEZIO: {:.3f}".format(ATP))
print("QUADRADO: {:.3f}".format(AQ))
print("RETANGULO: {:.3f}".format(AR))
