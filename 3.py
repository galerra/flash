file = open('24_3.txt').readline()
count = 0
for i in range(len(file)):
    e = file[i]
    if e == 'K':
        for j in range(i + 1, i + 12):
            if file[j] == '/':
                break
            elif file[j] == 'M':
                count += 1
                break
    elif e == 'M':
        for j in range(i + 1, i + 12):
            if file[j] == '/':
                break
            elif file[j] == 'K':
                count += 1
                break
print(count)
