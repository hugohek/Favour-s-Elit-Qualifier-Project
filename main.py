import random

#chat system 
#variables
quit_chat = 0
user_input = "m"

#list of topics for user
def list():
  print("1. Household")
  print("2. School")
  print("3. Religion")
  print("4. Politics")

# if false person is sad/ feeling bad
def check_response(user_input):
  #check for sensitive feelings ...
  keyword_list = ["sad","angry","crying","dreadful","crazy","tired","dying"]
  for item in keyword_list:
    if item in user_input:
      return False
  return True

#sad story interation
def conti_story(user_input):
  reply = ["Dam",
           "wow...", "intersting",
           "I could never... maybe",
           "holy smokes", ":("]
  return random.choice(reply)

# othertopic chat interation
def chat() :
  print("Well, heres a list of new potential topics for today.")
  list()
  user_input = input("What would you like to talk about?(1, 2, 3, 4)\n")
  response_to_topic(user_input)

#household bot
def household_bot(usIn):
  household_bot_responses = ["How interesting!",
                            "You don't say!.. let me check that",
                            "Very cool!", "Got that down..", "..Taking note of that",
                            "Programming is fun!"]
  return random.choice(household_bot_responses)

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

# start bot chat
def start_chat():
  quit_chat = "q"

  user_input = input("Hello, how are you?\n")

  while user_input != quit_chat:
    #Ask the user for more input, then use that in your response

    # if the response doesn't contain key word move on
    if (user_input != quit_chat):
      if (check_response(user_input)):
          chat()
      # apologize to user and ask abot story
    else:
      user_input = input("OH dam, want to talk about it??(y/n)\nI'm so sorry about that.\n")

      #if user what you to listen to chatbot go ahead if not move on to list
      if user_input == "y":
        ser_input  = input("ok lets hear it...(type 'm' to change subject)\n")
        while user_input != "m" :
          user_input = input(conti_story(user_input) + "\n")
        print("Well sorry to hear that.") 
    chat()
      


start_chat()


#print("hello")