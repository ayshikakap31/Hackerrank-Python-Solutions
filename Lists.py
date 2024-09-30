if __name__ == '__main__':
    N = int(input())
    l = [] #List to perform commands
    for temp in range(N):
        command = input() #Read the input commands
        input_extract = command.split()
        if input_extract[0] == 'insert':
            e = int(input_extract[2])
            i = int(input_extract[1])
            l.insert(i,e)
        elif input_extract[0] == 'print':
            print(l)
        elif input_extract[0] == 'remove':
            e = int(input_extract[1])
            for temp1 in range(len(l)):
                if l[temp1] == e:
                    l.remove(e)
                    break
        elif input_extract[0] == 'append':
            e = int(input_extract[1])
            l.append(e)
        elif input_extract[0] == 'sort':
            l.sort()
        elif input_extract[0] == 'pop':
            l.pop()
        elif input_extract[0] == 'reverse':
            l.reverse()
            