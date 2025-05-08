#definition of functions
def login_hub():
  print("welcome to Rayzordian services")
  name=input("enter your name: ")
  while(True):
   password=input("please enter your password: ")
   if int(password)==120207:
    print("\nLogin successful")
    break
   else:
    print("\nLogin unsuccessful please try again")

def main_hub():
 print("Welcome to the main hub\nPlease select the service you want to access:")
 print("A:Account Management")
 print("B:Tinkering Hub")
 choice=input("Service: ")
 if(input=="A"):
  print("Accessing Account Management")
 else:
  print("Accessing Tinkering Hub")


def main():
 login_hub()
 main_hub()
#calling and execution of main function
main()