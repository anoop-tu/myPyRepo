input_message = "I AM A SPY"
max_len = 0
strng=''
split1 = input_message.split()
print(split1)
rows = len(split1)
#print('number of words:' ,rows)
for i in split1:
    if max_len < len(i):
        max_len = len(i)
        max_split = i
#print('largest word: ',max_split)
max_len=len(max_split)
#print('length of ',max_split,': ',max_len)
mat = [' '] * rows #define 2D array i.e. array of lists - # rows
#print(mat)   
for i in range(rows):
    mat[i] = [' ']*max_len  #columns
#print(mat)
for i in range(rows):
    for j in range(max_len):
        if j >= len(split1[i]):
#            print(max_split[j-1],max_split[j])
#            print(i,j)
            mat[i][j]=ord(max_split[j-1])+ord(max_split[j])
        else:
#            print('x',i,j,split1[i][j],'-',mat[i][j])
            mat[i][j]=split1[i][j]
print(mat)
for k in range(max_len):
    for i in range(rows):
        strng=strng+str(mat[i][k])
#        print(mat[i][k])
print(strng)
