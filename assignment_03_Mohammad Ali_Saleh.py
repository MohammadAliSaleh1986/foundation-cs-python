def tupsum(tup1,tup2):
  list1=[]
  list2=[]
  listsum=[]
  for i in tup1:
    list1.append(i)

  for i in tup2:
    list2.append(i)
    
  for i in range (0,len(list1)):
    for j in range(0,len(list2)):
      if i==j:
        x=list1[i]+list2[j]
        listsum.append(x)
  return tuple(listsum)
t1=(1,2,3)
t2=(4,5,6)
print(tupsum(t1,t2))