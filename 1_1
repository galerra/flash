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
maxi_choice = 0
for i in a:
    k = file.count(i)
    if k >= maxi_choice:
        maxi_choice = k
        print(i, k)


