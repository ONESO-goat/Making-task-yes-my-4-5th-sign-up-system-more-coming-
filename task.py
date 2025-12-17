import json


#--------the dicts-----------#
try:
  with open("the_users_entering_task.json", "r") as f:
    the_users_entering_task = json.load(f)
except:
  the_users_entering_task = {}

try:
  with open("The_tasks_made_by_the_users", 'r') as f:
    The_tasks_made_by_the_users = json.load(f)

except:
  The_tasks_made_by_the_users = {}


#---------------SPECIAL CHARACTERS----------------#
specialcharacters = '!@#$%^&*()_+-={[,./<>?}]\'|;":`~'

#-------------------------------------------------#


def SIGNUP():

  while True:

    username = input("insert a username: \n")


    if username.isdigit():
      print("names can't be number only, please add minium of 1 letter")


    elif username in the_users_entering_task:
      print("this user is already taken, please inset something else")


    else:
      while True:

        password_from_user = input("please enter a password: \n")

        if len(password_from_user) < 8:
          print("please add a minium of 8 characters.")

        elif not any(char in specialcharacters for char in password_from_user):
          print("please include atleast 1 special charcter")
        

        else:
          the_users_entering_task[username] = password_from_user

          with open("the_users_entering_task.json", 'w') as f:
            json.dump(the_users_entering_task, f)
          return username, password_from_user
        
        
#--------------------------LOG IN---------------------------#
#-----------------------------------------------------------#


def LOGIN():

  attempts_for_password = 0
  the_max_attempts_for_password = 6


  while True:

    username = input("insert a username: ")



    if username in the_users_entering_task:
      print("this user is already taken, please try again or sign up.")


    else:
      while True:

        password_from_user = input("please enter a password")

        if len(password_from_user) < 8:
          print("please add a minium of 8 characters.")


        if attempts_for_password == the_max_attempts_for_password:
          print("Too many attempts. Please try again later.")
          return None


        if password_from_user != the_users_entering_task[username]:
          attempts_for_password +=1 
          print("wrong password")

        


def TASK(username):
  while True:
    print("\nYOUR TASK\n")
    for i in range(1,10):

      text = The_tasks_made_by_the_users[username][str(i)]

      print("TASK " + [str(i) for i in range (1, 10)])
    #list_of_tasks_the_user_can_input = [str(i) for i in range (1, 10)]

    print("CHOOSE TASK: ")


    preview = text[:20] + ("..." if len(text) > 20 else "")

    print(f"{i}. {preview if preview else '[EMPTY]'}")

    print("\nPick a note number (1–9) or type 'exit' to log out.")
    choice = input("Choice: ")


    if choice.lower() == "exit":
      return

    if choice not in [str(i) for i in range(1, 10)]:
      print("Invalid choice.")
      continue

  
def EDITING_THE_TASK(username):
  print("make or check task")


  the_users_task = input()
  The_tasks_made_by_the_users[username] = the_users_task

  with open("the_tasks_made_by_the_users.json", "w") as f:
    json.dump(The_tasks_made_by_the_users, f)

    print("Note saved!")


def MAIN():
  #sl = ['sign up', 'sign in', '1', 'signin', 'signup', 'log in', '2', 'login']
  while True:
    print("--------THE FRONT PAGE--------")
    print("SIGN UP")
    print("LOG IN\n")


    sign_up_OR_log_in = input("PICK FROM ABOVE (1 - 2): \n").lower()
    
    
    

    if sign_up_OR_log_in.lower() == 'sign up' or sign_up_OR_log_in == 'signup' or sign_up_OR_log_in == 'signin' or sign_up_OR_log_in == 'sign in' or sign_up_OR_log_in == '1':
      username = SIGNUP()
      TASK(username)
      

    elif sign_up_OR_log_in.lower() == 'log in' or sign_up_OR_log_in == 'login' or sign_up_OR_log_in == '2':
      username = LOGIN()
      if username:
        TASK(username)

    else:
      print("please insert something vaild.")



MAIN()