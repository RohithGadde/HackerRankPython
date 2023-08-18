if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    avg_score = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        avg_score[name] = sum(scores)/len(scores) 

query_name = input()
print("%.2f" %avg_score[query_name])