from re import findall, finditer
import csv
f1= open("task1-en.txt")
f=  ""

for i in f1:
    f+=i.strip()
f1.close()
reg_ex1 = r'Fig. #|\b(?:[a-zA-Z]){4}\b'

q1 = finditer(reg_ex1, f)
cnt = 0
for i in q1:
    if cnt > 10:break
    cnt+=1
    print(i.group(), i.start())


reg_ex2 = r'font-style:(?:[^\;])+|font-weight:(?:[^\;])+'
f1 = open("task2.html", "r", encoding="utf-8")
f=  f1.read()


f1.close()
q2 = findall(reg_ex2, f)
print(q2[:10])


f1 = open("task3.txt")
f= f1.read()
f1.close()
patterns_3 = [r' [0-9]+ ', r' [A-Z][a-zA-Z\-]+ ', r'[a-zA-Z0-9\-]+@[a-zA-Z0-9\-]+.[a-z]{3}', r'[0-9]{4}-[01][0-9]-[0-3][0-9]',r'(?:http:|https:)//[0-9\.a-zA-Z\-]+/']

id = findall(patterns_3[0], f)
suname = findall(patterns_3[1], f)
email = findall(patterns_3[2], f)
date = findall(patterns_3[3], f)
site = findall(patterns_3[4], f)
a= zip(id,suname, email, date, site)
with open("output.csv", "w", newline="", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerows(a) 

f1= open("task_add.txt")
f= f1.read()
f1.close
reg_ex4_tel = r'[^a-zA-Z0-9]+[0-9\-()]{10,15}[^a-zA-Z0-9]'
reg_ex4_date = r'[^0-9a-zA-Z][0-3][0-9][\.\-\/][0-1][0-9][\.\-\/][0-9]{1,4}[^0-9a-zA-Z]|[^0-9a-zA-Z][0-1][0-9][\.\-\/][0-3][0-9][\.\-\/][0-9]{1,4}[^0-9a-zA-Z]|[^0-9a-zA-Z][0-9]{1,4}[\.\-\/][0-1][0-9][\.\-\/][0-3][0-9][^0-9a-zA-Z]'
reg_ex4_fname = r'[^a-zA-Z0-9][0-9a-zA-Z\_\-()]+\.[0-9a-zA-Z]*[a-zA-Z]+[0-9a-zA-Z]*[^a-zA-Z0-9]'
print(findall(reg_ex4_fname, f))