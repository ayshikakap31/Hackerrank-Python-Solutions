def print_formatted(number):
    # your code goes here
    max_width = len("{0:b}".format(number))
    
    for i in range(number):
        print('{:>{width}} {:>{width}o} {:>{width}x} {:>{width}b}'.format(i+1,i+1,i+1,i+1, width=max_width).upper())
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)