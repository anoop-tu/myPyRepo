alph='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz'
stng='AAcAbbbbCACC'
arr=[]
for k in alph:
    a=stng.count(k)
#    print(k,':',a)
    arr.append([a,k])

arr.sort()
#print(arr)
cnt = 0
for i in arr:
    if i[0] % 2 !=  0:
        if i[0] > cnt:
            cnt = i[0]
            char = i[1]
        
print(char,':',ord(char))
