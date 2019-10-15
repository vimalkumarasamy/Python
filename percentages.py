if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sel_scores=student_marks[query_name]
    sel_avg=sum(sel_scores)/3
    print('%.2f' % sel_avg)