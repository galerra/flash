file = open('24_1.txt').readlines()
c = 0
for i in range(1, len(file), 2):
    st = file[i].replace('\n', '').replace('Z', '')
    if len(st) >= 100 and 'MANUL' in st:
        c += 1
print(c)
