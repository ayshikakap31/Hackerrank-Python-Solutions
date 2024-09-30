N = input()
if __name__ == '__main__':
    students = []
    for _ in range(int(N)):
        student = []
        name = input()
        student.append(name)
        score = float(input())
        student.append(score)
        students.append(student)
    scores_save = []
    for i in range(len(students)):
        scores_save.append(students[i][1])
    scores_save_uni = list(set(scores_save))
    scores_save_uni.sort()
    scores_min = scores_save_uni[1]
    scores_min_names = []
    for i in range(len(scores_save)):
        if scores_save[i] == scores_min:
            scores_min_names.append(students[i][0])
    scores_min_names.sort()
    for i in scores_min_names:
        print(i)
        
    
