#create a chat bot that responds to certain keywords
#imports
import random

#Global variables
quit_chat = "exit"
user_input = " "


#functions
#list of topics for user
def list():
  print("1. Household")
  print("2. School")
  print("3. Religion")
  print("4. Politics")

# check people feelings through response
def check_response(user_input):
  response = wrdBank(user_input)
  switcher = {
    "Positive": 1
    "Negative": 2
  }
  return switcher.get(response, "fine") 
  #checks for the users mood (happy, sad, angry or netrual and responds to them) respnds with "thats cool" if netrual


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
def happy_story():
  reply = ["Dam",
           "wow...", "intersting",
           "thats so cool. What happened next?",
           "holy smokes", ":)"]
   #if user what's you to listen to their story
  if user_input == "y":
    user_input  = input("ok lets hear it...(type 'switch' to change subject)\n")

    #continue in a loop responding to each line of the story entered
    while user_input != "switch" :
      user_input = input(happy_story(user_input) + "\n")
  else:
    print("Well thanks for sharing, that was interesting.") 
  
  return random.choice(reply)

# othertopic chat interation
def mainMenu_chat() :
  print("Well, heres a list of potential topics we could talk about today.")
  list()
  user_input = input("What would you like to talk about?(1, 2, 3, 4)\n")
  response_to_topic(user_input)

# response to chat topic
def response_to_topic(user_input):
  usIn = user_input
  if usIn == "1":
    # equals husehold
    print("you have choosen household")
    # call household bot
    user_input = input("what would you like to talk about in the household(...finances)\n")
    while user_input != "m" :
      print("type 'm' to go back to menu")
      user_input = input(household_bot(user_input)+ "\n")
  elif usIn == "2":
    # equals school
    print("COMING SOON\n")
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

def users_story(r): #r states user's response
  if (r == "Positve"): 
      # ask user about their story
      user_input = input("Awesome, mind sharing the good news??(y/n)\n")

  elif (r == "Negative"): 
    # ask user about their story
    user_input = input("Oh lord, want to talk about it??(y/n)\n I'm so sorry about that.\n")

# start bot chat
def start_chat():
  #instruction for users to quit chat
  print("Input 'exit' to quit the chat")

  user_input = input("Hello, how are you?\n")

  #Ask the user for more input, then use that in your response
  while user_input != quit_chat:
    # userResponse is either Positive or Negative else response doesn't contain mood keywords
    userResponse = check_response(user_input) 
    
    # if the response  contain key word "fine" from checker move on to mainMenu_chat
    if (userResponse != "fine"):
      users_story(userResponse)
    else:
      print("Thats nice.\n")
      mainMenu_chat() 
      

 """
------------------------
      Start program
------------------------
 """     
start_chat()

"""
#household bot
def household_bot(usIn):
  household_bot_responses = ["How interesting!",
                            "You don't say!.. let me check that",
                            "Very cool!", "Got that down..", "..Taking note of that",
                            "Programming is fun!"]
  return random.choice(household_bot_responses)
"""