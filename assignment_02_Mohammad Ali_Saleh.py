
def displayMenu():
  print("1. Count Digits\n"+"2. Find Max\n"+"3. Count Tags\n"+"4. Exit\n"+"------------------\n")
  choice=int(input("Enter a choice:"))

def choiceOne():
 n=int(input("please enter your integer to count its digits"))

div1=[]
def recursiveCount(num):
  
  if (num%10) == num:
    div1.append(1)
 
  else:
    div1.append(1)
    recursiveCount(num//10)
  
    
  
  return sum(div1)

x=recursiveCount(900000)
print(x,"digits")

#n=int(input("please enter your number of list items"))
#list2=[]
#for i in range (0,n):
  #item=int(input("please enter your list item"))
  #list2.append(item)



def find_max(my_list, max):
    if len(my_list) <= 1:
        return max
    else:
        if my_list[0] > max:
            return find_max(my_list[1:], my_list[0])
        else:
            return find_max(my_list[1:], max)


my_list = [1, 5, 16, 9, 20, 40, 5]                                           
print(find_max(my_list, my_list[0]))


i=0
listcount=[]
def multiString(str1,tag):
  
  if tag  not in str1:
    return
 
  else:
    
    i=str1.index(tag)
    listcount.append(1)
    multiString(str1[i+1:],tag)
    print(i,str1[i+1:])
   
  return sum(listcount)

str2="<html><li><html><li><html>"
tag2="<li>"
x=multiString(str2,tag2)
print(x)