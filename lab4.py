


def summ(list, pos):
    s = 0
    for i in list:
        s+=i[pos]
    return s
answers = []
def permutations(list, clear, ans):

    for i in range(len(list)):
        if clear >= list[i][0]:
            t= summ(ans+[list[i]],1 )
            if t > 205 - t - 15:
                answers.append(ans+[list[i]])
            permutations(list[:i]+list[i+1:], clear- list[i][0], ans+[list[i]])


items = [
    [1, 25, 't'],
    [3, 25, 'r'],
    [2, 20, 'm'],
    [2, 20, 's'],
    [2, 20, 'c'],
    [3, 20, 'x'],
    [1, 15, 'k'],
    [1, 15, 'f'],
    [2, 15, 'p'],
    [2, 15, 'a'],
    [1, 10, 'd'],
    [1, 5, 'i']
]





permutations(items[:-1], 8, [items[-1]])
check = set()
right_ans = []
for i in answers:
    s = sorted(i, key=lambda x:x[2])
    t = ''.join(r[-1] for r in s)
    if t not in check:
        check.add(t)
        right_ans.append(sorted(i, reverse=True, key=lambda x:x[0]))
ans = max(right_ans, key=lambda x:sum(t[1] for t in x)) if right_ans else []
inv_x = [0,0,0,0,0,0,0,0,0]

for item in ans:
    r1= inv_x.index(0)
    
    if r1//3 == (r1+item[0] - 1)//3:
        
        for i in range(r1,r1+item[0]):
            inv_x[i] = item[2]
    else:
        r1 = (r1//3 + 1)*3
        for i in range(r1,r1+item[0]):
            inv_x[i] = item[2]
for i in range(0,len(inv_x), 3):
    print(inv_x[i:i+3])