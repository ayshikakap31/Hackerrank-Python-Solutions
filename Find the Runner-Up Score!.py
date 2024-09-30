if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    scores_unique = list(set(scores))
    scores_unique.sort()
    print(scores_unique[len(scores_unique)-2])
