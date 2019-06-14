n = int(input())
ar = list(map(int,input().split()))
list2 = set(ar)
list3=[]
for i in list2:
    list3.append(ar.count(i))   
sum=0
for i in list3:
    sum=sum+(i//2)   
  
print("the number of pairs of shocks are : ",sum)    
