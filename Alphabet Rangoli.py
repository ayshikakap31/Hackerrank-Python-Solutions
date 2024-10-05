def print_rangoli(size):
    lines = int(size*2)-1
    all_lines = [None]*lines
    chars_indexes = {}
    temp = 'a'
    indexes = [i for i in range(1,27)]
    for index in indexes:
        chars_indexes[index] = temp
        temp = chr(ord(temp) + 1)
    max_char = chars_indexes[size]
    mid_line = [max_char]
    for temp in range(1,size):
        mid_line.append('-')
        mid_line.append(chars_indexes[size-temp])
    if mid_line[-1] == 'a':
        for temp in range(2,size+1):
            mid_line.append('-')
            mid_line.append(chars_indexes[temp])
    
    mid_str = "".join(mid_line)
    all_lines[size-1] = mid_str
    total_len = len(mid_str)
    for temp in range(total_len):
        ch = mid_str[temp]
        if ch == 'a':
            centre_pos = temp
    sub = 2
    counter=1
    for temp in range(size-2,-1,-1):
        
        other_temp = temp+(2*counter)
        new_list = [None]*total_len
        centre_str = chars_indexes[size-temp]
        sub -= 2
        new_list[centre_pos] = centre_str
        new_list[centre_pos+1] = '-'
        new_list[centre_pos-1] = '-'
        loop_n = (size-temp)+1
        temp1 = centre_pos+2
        temp2 = centre_pos-2
        while(loop_n<=size):
            new_list[temp1] = chars_indexes[loop_n]
            new_list[temp2] = chars_indexes[loop_n]
            temp1 += 1
            temp2 -= 1
            new_list[temp1] = '-'
            new_list[temp2] = '-'
            loop_n += 1
            temp1 += 1
            temp2 -= 1
        for temp3 in range(0,total_len,1):
            if new_list[temp3] == None:
                new_list[temp3] = '-'
        #print(new_list)
        new_str = "".join(new_list)
        all_lines[temp] = new_str
        all_lines[other_temp] = new_str
        counter += 1
    for i in range(0,lines,1):
        print(all_lines[i])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)