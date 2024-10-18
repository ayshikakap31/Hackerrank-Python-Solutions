def minion_game(string):
    # your code goes here  
    # vow = 'AEIOU'
    # stuart = 0
    # kevin = 0
    # for i in range(len(string)):
    #     for j in range(len(string)):
    #         st = string[j:j+i+1]
    #         if len(st)==i+1:
    #             if st[0] not in vow:
    #                 #stuart.append(st)
    #                 stuart += 1
    #             else:
    #                 #kevin.append(st)
    #                 kevin += 1
    # #stuart_score = len(stuart)
    # #kevin_score = len(kevin)
    # if stuart > kevin:
    #     print("Stuart {}".format(stuart))
    # elif stuart < kevin:
    #     print("Kevin {}".format(kevin))
    # else:
    #     print("Draw")
    vow = 'AEIOU'
    stuart = 0
    kevin = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vow:
            kevin += length - i  # Kevin scores if it's a vowel
        else:
            stuart += length - i  # Stuart scores if it's a consonant
    
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif kevin > stuart:
        print("Kevin {}".format(kevin))
    else:
        print("Draw")
              
if __name__ == '__main__':
    s = input()
    minion_game(s)