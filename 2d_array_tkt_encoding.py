inputString="Paris:Delhi:9945672345,Berlin:Brussels:9456723456"
tickets = inputString.split(',')
sumnum=0
print(tickets)
for i in range(len(tickets)):
    details=tickets[i].split(':')
    print(details)
    for j in range(len(details[2])):
        if j % 2 == 0:
#            print(details[2][i])
            sumnum+=int(details[2][j])
            
    tktcode=details[0][:2]+details[1][-2:]+str(sumnum)+str(i+1)
    sumnum=0
    print(tktcode)
