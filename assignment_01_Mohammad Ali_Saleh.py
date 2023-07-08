#function that takes an integer from the user and gives its factorial#

import math #import math library to use its methods

def factorialFunction(): #define function to calculate factorial
  
    n=input("please enter an integer to calculate its factorial: ") # take an integer as input from the user as string
  
    if n.lstrip('-').isdigit(): # lstrip method to remove a negative sign,  isdigit method to check if the input is a digit
       x=int(n) #int function to change the string entered to integer
      
       if x>=0:
          print(math.factorial(x)) # factorial function if x was positive or equal to zero
       elif x<0:             
          print(math.factorial(-x)) # factorial function if x was positive or equal to zero
         
    else: 
      print("invalid value") # print invaild if the input was not an integer
      factorialFunction() # call the function to let the user renter a valid value
      
factorialFunction() # call the function to show results

print("\n")
print("\n")
print("\n")

#function that takes an integer from the user and gives its divisors#

def divisorsFunction(): #define a function that takes an integer from the user and gives its divisors
  
   list_Divisors=[] #create a new list to store divisors in it
   n=input("please enter an integer to calculate its divisors: ") # take an integer as input from the user as string
  
   if n.lstrip('-').isdigit(): # lstrip method to remove a negative sign,  isdigit method to check if the input is a digit
       x=int(n) #int function to change the string entered to integer
      
       for i in range (1,x+1): #loop starts at 1 and ends at x+1
         if x % i == 0: #checks if the remainder of the division of entered integer by i in each iteration is equal to zero
           list_Divisors.append(i) # add i if above condition is true to the new list
    
       print(list_Divisors)  #print the list
     
   else:
    print("invalid value") # print invaild if the input was not an integer
    divisorsFunction() # call the function to let the user renter a valid value
    
divisorsFunction() # call the function to show results

print("\n")
print("\n")
print("\n")
        
#function that takes a string from the user and returns the string reversed#

def reverseString(): #define a function that takes a string from the user and reverses it.
  
  str1=input("please enter a string to reverse it: ") #takes a string from the user as input
  str2="" #create a string with space character
  
  for i in str1: #loop to iterate i in the entered string
      str2=i+str2 #add i in each iteration before str1 and then assign its value to str2 

  return str2 #return the new value of str2


reversed=reverseString() # assign the function to a variable
print(reversed) # print the variable

print("\n")
print("\n")
print("\n")
#function that takes a list of integers from the user and returns a new list of the even numbers in the same order#

def evenListFunction(): #define the required function
  
   list_numbers=[] #create a new list to store entered number in it
   list_even=[] #create a new list to store the even number in it
   
   n=input("how many numbers do you want to add to the original list: ") #takes the numbers of the list items from the user as input
  
   if n.lstrip('-').isdigit(): # lstrip method to remove a negative sign,  isdigit method to check if the input is a digit
       x=int(n) #int function to change the string entered to integer
     
   if x>0: #if condition x is greater than zero is true
        
        for i in range (1,x+1): #loop will iterate i in from 1 to the number enterd added by 1
            y=int(input("add your number:")) # at each iteration the user will add a number as input
            list_numbers.append(y) # at each iteration each number is added to the list
    
      
        for i in list_numbers:  # loop will iterate i in the list of entered number
          if i % 2 == 0: #check if the condition is true regarding remainder of the division of each i at each iteration by 2 is equal to zero
            list_even.append(i) #add i if condition true to another list for even numbers
            
        
        return(list_even)  #return the new even list list
        
                
   else:
    print("invalid value") # print invaild if the input was not an integer
    evenListFunction()  # call the function to let the user renter a valid value
    
even=evenListFunction() # assign the function to a variable
print(even) # print the variable


print("\n")
print("\n")
print("\n")

#function that takes a string password from the user and checks it as a strong or weak#

def lenChecking(strx): # check if the password consists of 8 or more characters
  
    if len(strx) >= 8:
      return True
    else:
      return False

def upperChecking(strx): # check if the password contains at least one uppercase character
  flag=0
  
  for i in (strx):
      if i.isupper() == True:
         flag=1
         break
        
  if flag==1:
      return True
  else:
      return False
      
def lowerChecking(strx): # check if the password contains at least one lowercase character
  flag=0

  for i in (strx):
      if i.islower() == True:
         flag=1
         break
        
  if flag==1:
      return True
  else:
      return False

def digitChecking(strx): # check if the password contains at least one digit
  flag=0
  
  for i in (strx):
      if i.isdigit() == True:
         flag=1
         break
        
  if flag==1:
      return True
  else:
      return False
        

def specChecking(strx): # check if the password contains at least one special character
  list_spec= ["?","#","$","!"]
  flag=0
  
  for i in strx:
       if i in list_spec:
          flag=1
          break
         
  if flag==1:
      return True
  else:
      return False
   
def spaceChecking(strx): # check if the password does not contain any space
  flag=0
  
  for i in (strx):
      if i.isspace() == True:
         flag=1
         break
        
  if flag==1:
      return False
  else:
      return True
    
def passwordVerification(): 
  
  str1=input("please enter your password: ") #take the password from the user as input

  #call all the functions to check above conditions and assign each to a variable

  l=lenChecking(str1) 
  u=upperChecking(str1)
  lw=lowerChecking(str1)
  d=digitChecking(str1)
  s=specChecking(str1)
  sp=spaceChecking(str1)

  if (l and u and lw and d and s and sp ) == True:
    print("strong password") # if all conditions are true it will print a strong password
  else:
    print("weak password") # if at least one condition is false it will print a weak password
    

result=passwordVerification() # call the main function to show the result 
        
print("\n")
print("\n")
print("\n")       
#function that takes a string as input and checks wether it is a valid IPv4 address# 


def numChecking(x): # checks if each octet is not greater than 255 or is not less than 0 
  flag=0
  if len(x) ==4:
      
      for i in x:
        if i=="":
           flag=1
           break
          
      if flag==1:
        return False
      else:
  
          flag=0
  
          for i in x:
              if int(i)>255 or int(i)<0:
               flag=1
               break
        
          if flag==1:
            return False
          else:
            return True
  else:
      return False
def lenConsChecking(x): # checks if there are no 2 consective periods
    flag=0
  
    if len(x) ==4:
      
      for i in x:
        if i=="":
           flag=1
           break
          
      if flag==1:
        return False
      else:
        return True
        
    else:
      return False  

def lengthChecking(x): # checks the number of octet is equal to 4
  if len(x) <4 or len(x) >4:
      return False

  
def zeroChecking(x): # checks if the number in each octet does not start with 0 and ends with another number
  flag=0
  if len(x) ==4:
      
      for i in x:
        if i=="":
           flag=1
           break
          
      if flag==1:
        return False
      else:
  
          flag=0   

          for i in x:
             if i[0]=="0"and len(i)>1:
                 flag=1
                 break
         
             if flag==1:
                return False
             else:
                return True
  else:
      return False
  
    
  





def IpChecking(): 
  
  str1=input("please enter a string to check wether it is a valid IPv4 address: ") # take the ip from the user as input
  
  y= str1.split(".") # The split() function returns the strings as a list using the period as a sperator to split.
  print(y)
  # call all functions and assign them to variables
  n=numChecking(y) 
  l=lenConsChecking(y)
  z=zeroChecking(y)

  if n or l or z==False:
         print ("Invalid Ip") # print invalid it one condition is not satisified
  elif n and l and z==True:
         print ("Valid Ip") # print valid it all conditions are satisified
    
validity=IpChecking() # call the main function




