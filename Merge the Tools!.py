def merge_the_tools(string, k):
    # your code goes here
    sub_str = [string[i:i+k] for i in range(0,len(string),k)]
    sub_sub_str=[]
    for i in sub_str:
        l = [j for j in i]
        prev_let = ""       
        for temp in range(k):
            if l[temp] not in prev_let:
                prev_let += l[temp]
        sub_sub_str.append(prev_let)
    for temp in sub_sub_str:
        print(temp)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)