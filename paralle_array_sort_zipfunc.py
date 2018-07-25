len1=5
doll_id=[1001,1002,1003,1004,1005]
doll_ht=[800,300,500,200,100]
#id_ht=[]
#for i in range(len1):
#    id_ht.append(str(doll_id[i])+':'+str(doll_ht[i]))
#print(id_ht)
zipp=zip(doll_ht,doll_id)
#zipp.sort()
zipped=sorted(zipp)
print(zipped)
dollid,dollht=zip(*zipped)
print(dollht)
