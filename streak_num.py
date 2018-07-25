num1 = 98979
str1 = str(num1)
len1 = int(len(str1))
a=[0]
E=0
for i in range(len1):
    if i % 2 == 0:
        if (int(str1[i:i+1])*2) < len1:
            a.append(int(str1[i:i+1])*2)
    else:
        E=E+(int(str1[i:i+1]))
        
S = E + a[0]
print(a,E,S)

for K in range(100):
    if (S+K) % (K+1) != 0:
        print(K)
        break
