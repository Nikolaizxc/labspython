import xml.dom.minidom
import csv
dom = xml.dom.minidom.parse("currency.xml")
valutes = dom.getElementsByTagName("Valute")
res = {
    v.getElementsByTagName("CharCode")[0].firstChild.nodeValue.strip(): 
    int(v.getElementsByTagName("Nominal")[0].firstChild.nodeValue)
    for v in valutes 
}
for i,z in res.items():
    print(i,z)
def search(text, res):
    
    cnt = 0
    for i in range(len(text)):
        if i >= len(res):
            break
        if text[i] == res[i]:
            cnt+=1
        else:
            break
    return cnt

with open("books-en.csv", "r", encoding='utf-8', errors='ignore') as f:
    file = csv.reader(f, delimiter=';')
    header = next(file)
    cnt = 0
    end = ""
    for i in file:
        
        if len(i[1]) > 30:
            cnt+=1
            if cnt < 21:
                end += f"{cnt} <{i[2]}>. <{i[1]}> - <{i[3]}> \n"
    
    print(cnt)
with open("books-en.csv", "r", encoding='utf-8', errors='ignore') as f:
    file = csv.reader(f, delimiter=';')
    cnt1 = 0
    cnt0 = 0
    izd = list()
    a = []
    src = input("Введите имя автора: ").lower()
    s = next(file)
    itog1 = ['','','']
    itog0 = ['','','']
    for i in file:
        a.append([i[2], int(i[-2])])
        if i[4].strip() not in izd:
            izd.append(i[4].strip())
        if not(i[3].isdigit()):
            continue
        if 1997 <= int(i[3]) <= 2003:
            if src in i[2].lower():
                cnt0+=1
                itog0 = max(itog0, i, key=lambda x:len(x[2]))
            if search(src, i[2].lower()) + search(src[::-1], i[2].lower()[:len(src)][::-1]) + 1 >= len(src):
                #это поиск с одной ошибкой

                cnt1+=1
                itog1 = max(itog1, i, key=lambda x:len(x[2]))
            

    print("Всего результатов бeз ошибок:" + str(cnt0))
    if len(itog0[0]):
        print("самый релевантный: ")
        print(f"{itog0} \n")
    else:
        print()
    print("Всего результатов с одной ошибкой:" + str(cnt1))
    if len(itog1[0]):
        print("самый релевантный: ")
        print(itog1)


with open("file.txt", "w", encoding='utf-8') as f:
    f.write(end)
input("нажмите любую клавишу для продолжения")
print('Самые популярные 20 книг.')
a.sort(reverse=True, key=lambda x:x[1])
for i in a[:21]:
    print(i[0])
input("нажмите любую клавишу для продолжения")
for i in izd:
    print(i)