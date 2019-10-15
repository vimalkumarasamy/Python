# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer, , the number of students. 
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

if __name__ == '__main__':
    scores={}
    to_remove=[]
    names=[]
    for x in range(int(input())):
        name = input()
        score = float(input())
        scores[str(name)]=score
    min_val=scores[min(scores.keys(), key=(lambda k: scores[k]))]
    for n in scores:
        if scores[n]==min_val:
            to_remove.append(n)
    
    for r in to_remove:
        del scores[r]
        
    min_val_treated=scores[min(scores.keys(), key=(lambda k: scores[k]))]
    for m in scores:
        if scores[m]==min_val_treated:
            names.append(m)      
    
    names.sort()
    for pr in names:
        print(pr)





# Another elegant solution

a = [[input(), float(input())] for i in range(int(input()))]
s = sorted(set([x[1] for x in a]))
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print (name)