str1='PAS'
str2='ILIKECODE'
k=0
str3 = str1 + str2
str4=''
rows = int(len(str2) / len(str1) + 1)
cols = int(len(str1))

mat = [''] * rows
for i in range(rows):
    mat[i] = [''] * cols
#print(mat)
for i in range(rows):
    for j in range(cols):
        mat[i][j] = str3[k:k+1] 
        k+=1
        
print('mat:', mat)

mat1 = [list(i) for i in zip(*mat)]
print(mat1)
mat1.sort()
print('mat1:',mat1)

for i in range(cols):
    for j in range(rows):
        str4+=mat1[i][j]
print(str4)
