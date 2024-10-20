# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
S = input()
l = [int(i) for i in S]
p = itertools.groupby(l)
result = []
for key, value in p:
    vals = list(value)
    X = len(vals)
    res = (X,vals[0])
    result.append(res)
new_str = ''
for i in result:
    new_str += str(i) + " "
print(new_str)
    