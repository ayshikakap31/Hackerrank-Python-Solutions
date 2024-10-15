# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
com_inp = complex(input())
angle = cmath.phase(com_inp)
r = abs(com_inp)
print(r)
print(angle)