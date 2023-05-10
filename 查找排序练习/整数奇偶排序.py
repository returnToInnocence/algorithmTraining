n = input().split()
ji = []
ou = []
for i in range(len(n)):
    if int(n[i]) % 2 == 1:
        ji.append(int(n[i]))
    else:
        ou.append(int(n[i]))
ji.sort(reverse = True)
ou.sort()
pri = ji + ou
for i in range(len(pri)):
    print(pri[i], end=" ")