
def displayAdminMenu():
  print("please enter your choice:\n 1- Display Statistics\n 2- Book a Ticket\n 3- Display all Tickets\n 4- Change Tickets Priority\n 5- Disable Ticket\n 6- Run Events\n 7- Exit  ")

def displayDiffMenu():
  print("please enter your choice:\n 1- Book a Ticket\n 2- Exit  ")


count=1
def loginForm():
  global count
  print("Greetings to you please enter your username and password")
  username=input("username: ")
  password=input("password: ")
  if username=="admin" and password=="admin123123":
    displayAdminMenu()
  elif username=="admin" and password=="":
    displayDiffMenu()
  elif  count<=4:
    count+=1
    print("incorrect username or password")
    loginForm()
  else:
    print("you exceeded the maximum number of login attempts")

loginForm()

def ticketList():
  with open("test.txt", "r") as a_file:
    list_of_lists = [
        [ for x in line.strip().split(',')]
        for line in a_file
    ]
print(list_of_lists)