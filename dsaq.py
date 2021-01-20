with open('dataset_3363_2.txt', 'r') as fa:
    for line in fa:
        line = line.strip()

answ = ''
a = line
print(a)
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b+=a[i]
        a=a[:i]+"!"+a[i+1:]
c=a.split('!')[1:]
for i in range(len(b)):
    answ += b[i]*int(c[i])
print(answ)

with open('answ.txt', 'w') as an:
    an.write(answ)
