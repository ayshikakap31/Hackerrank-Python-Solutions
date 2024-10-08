## Using Counter():
from collections import Counter
X = int(input())  # Total number of shoes
sizes = list(map(int, input().split()))  # List of available shoe sizes
N = int(input())  # Number of customers

sizes_avail = Counter(sizes)

total = 0

for _ in range(N):
    size, price = map(int, input().split())  # Customer's requested size and price offered
    if sizes_avail[size] > 0:  # If the size is available
        total += price  # Add the price to total earnings
        sizes_avail[size] -= 1  # Reduce the stock of that size

print(total)

## Without using Counter():
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

X = int(input())
sizes = input()
N = int(input())
l = []
cust_size = []
cust_price = []
sizes_avail = []
total = 0
for i in range(N):
    l.append(input())
sizes_temp = sizes.split(' ')
for i in range(len(sizes_temp)):
    sizes_avail.append(int(sizes_temp[i]))
        
for i in range(N):
    cust = l[i]
    c_size,c_price = cust.split(' ')
    cust_size.append(int(c_size))
    cust_price.append(int(c_price))

for temp1 in range(N):
    cz = cust_size[temp1]
    for temp2 in range(len(sizes_avail)):
        if cz == sizes_avail[temp2]:
            total += cust_price[temp1]
            sizes_avail.remove(sizes_avail[temp2])
            break
print(total)
'''


    