if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    l1 = list(integer_list)
    t = tuple(l1)
    print(hash(t))
    