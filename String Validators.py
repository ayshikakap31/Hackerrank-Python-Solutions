if __name__ == '__main__':
    s = input()
    l = list(s)
    ans = False
    for i in l:
        ans = i.isalnum()
        if ans == True:
            print(True)
            break
    if ans == False:
        print(False)
    ans = False        
    for i in l:
        ans = i.isalpha()
        if ans == True:
            print(True)
            break         
    if ans == False:
        print(False)
    ans = False  
    for i in l:
        ans = i.isdigit()
        if ans == True:
            print(True)
            break
    if ans == False:
        print(False)
    ans = False  
    for i in l:
        ans = i.islower()
        if ans == True:
            print(True)
            break
    if ans == False:
        print(False)
    ans = False  
    for i in l:
        ans = i.isupper()
        if ans == True:
            print(True)
            break
    if ans == False:
        print(False)