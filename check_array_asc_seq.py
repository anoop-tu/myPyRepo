def Check_array(list4):
    count=0
    
    for i in range(len(list4)-1):
        
       if list4[i] < list4[i+1]:
           count += 1
       else:
           list5.append(count)
           count=0
    list5.append(count)       
    print(list4)
    print(list5)
    print("max sorted elements: ",max(list5)+1)
    print("Array length: ",len(list4))
    return 0

list1=[1,2,3,4,5,6]
list2=[11,2,13,4,5,6,7]
list3=[11,2,13,4,15,6]
list5=[]
Check_array(list3)
