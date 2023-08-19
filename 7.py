records1 = []
score_set = []
for i in range(int(input())):
    name = input()
    score = float(input())
    records1.append([name,score])
    score_set.append(score)

records1.sort()
score_set.sort()
min = score_set[0]    
for i in score_set:
        if i == min:
            pass
        else:
             new_min = i
             break

for a,b in records1:
    if b == new_min:
        print(a)
    else:
         pass

