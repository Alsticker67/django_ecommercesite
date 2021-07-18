 case=list()
for i in range(0,6):
    num=input("Enter the number of cases:")
    case.append(float(num))
avg=sum(case)/len(case)
print('Average:-',avg)