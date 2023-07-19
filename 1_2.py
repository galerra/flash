a = []
def generation_prime_numbers():
    for i in range(2, 10000 + 1):
        f = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                f = False
                break
        if f: a.append(str(i))
generation_prime_numbers()
file = open('24_1.txt').readline()
d = {x:0 for x in a}
for i in a:
    d[i] = file.count(i)
maxi_value = max(d.values())
mini_x = 10 ** 6
for i in d.keys():
    if d[i] == maxi_value: mini_x = min(mini_x, int(i))
print(mini_x)
