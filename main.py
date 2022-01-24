#create a chat bot that responds to certain keywords
#imports
import random
from wrdBank_Class import wrdBank #import word bank class from class fi

#Global variables
quit_chat = "exit"
user_input = " "

if user_input == 'exit':
    print("Thank you for chatting with me.")
    exit()

#functions
#list of topics for user :checked
def list():
  a = 1
  topic_list = ["Household", "School", "Religion", "Politics"]

  for item in topic_list:
    print("{}. {}\n".format(a, item))
    a += 1
""" 
  print("1. Household")
  print("2. School")
  print("3. Religion")
  print("4. Politics")
"""

# check people feelings through response
def check_response(user_input):
  response = wrdBank(user_input)
  
  return response.getMood()
  #checks for the users mood (happy, sad, angry or netrual and responds to them with either Positive/Negative) responds with "thats cool" if netrual


#sad story interation
def sad_story(user_input):
  reply = ["Dam",
           "wow...", "intersting",
           "I could never... maybe",
           "holy smokes", ":("]
  #if user what's you to listen to their story
  if user_input == "y":
    user_input  = input("ok lets hear it...(type 'switch' to change subject)\n")

    #continue in a loop responding to each line of the story entered
    while user_input != "switch" :
      user_input = input(sad_story(user_input) + "\n")
  else:
    print("Well sorry to hear about that.") 
  
  return random.choice(reply)

#happ story interaction
def happy_story(user_input):
  reply = ["Dam",
           "wow...", "intersting",
           "cool. What happened next?",
           "holy smokes", ":)"]
   #if user what's you to listen to their story
  if user_input == "y" or user_input == "yes":
    user_input  = input("ok lets hear it...(type 'switch' to go to mainMenu)\n")

    #continue in a loop responding to each line of the story entered
    while (user_input != "switch"):
      user_input = input(happy_story(user_input) + "\n")
      if user_input == 'exit':
        print("Thank you for chatting with me.")
        exit()
  if user_input == "switch" :
    print("Well thanks for sharing, that was interesting.\n \n loading...\n loading..\n \n") 
      
  #elif user_input == "n":
   # mainMenu_chat()
  #else:
    #"invalid statment"
  
  return random.choice(reply)

# othertopic chat interation
def mainMenu_chat() :
  print("\nWell, heres a list of potential topics we could talk about today.")
  list()
  
# response to chat topic
def response_to_topic(user_input):
  usIn = user_input
  if usIn == "1":
    # equals husehold
    print("\nyou have choosen household")
    # call household bot
    user_input = input("what would you like to talk about in the household(...finances)\n")
    while user_input != "main" :
      print("type 'main' to go back to menu")
      user_input = input(household_bot(user_input)+ "\n")
  elif usIn == "2":
    # equals school
    return print("COMING SOON\n")
    # call school bot
  elif usIn == "3":
    # equals religion
    print("COMING SOON\n")
  elif usIn == "4":
    # equals politics
    print("COMING SOON\n")
  #elif usIn == "q":
    print("Thanks for chatting with us")
 # else:
  #  print("Please pick a valid topic.\n" + "\n")

#household bot
def household_bot(usIn):
  household_bot_responses = ["How interesting!",
                            "You don't say!.. let me check that",
                            "Very cool!", "Got that down..", "..Taking note of that",
                            "Programming is fun!"]
  return random.choice(household_bot_responses)

def users_story(r): #r states user's response
  if (r == "Positive"): 
      # ask user about their story
      user_input = input("Awesome, mind sharing the good news??(y/n)\n")
      happy_story(user_input)

  elif (r == "Negative"): 
    # ask user about their story
    user_input = input("Oh lord, want to talk about it??(y/n)\n I'm so sorry about that.\n")
    sad_story(user_input)

# start bot chat
def start_chat():
  #instruction for users to quit chat
  print("Input 'exit' to quit the chat")
  
  user_input = input("Hello, how are you?\n")

  # userResponse is either Positive or Negative else response doesn't contain mood keywords
  userResponse = check_response(user_input) 
  #print(check_response(user_input))

  #Ask the user for more input, then use that in your response
  while user_input != quit_chat:
    
    # if the response  contain key word "fine" from checker move on to mainMenu_chat
    if (userResponse != "fine"):
      users_story(userResponse)
    #else:
    #print("Thats nice.\n")
    mainMenu_chat() 
    userResponse = "fine"
    user_input = input("What would you like to talk about?(1, 2, 3, 4)\n")
    user_input = input(response_to_topic(user_input))

  if user_input == 'exit':
    print("Thank you for chatting with me.")
    exit()
      

"""
------------------------
    Start program
------------------------
"""  
if __name__ == ('__main__')  : 
  start_chat()
