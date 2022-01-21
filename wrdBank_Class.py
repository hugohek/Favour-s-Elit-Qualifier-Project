import random
import ast #imports any form of files
import json # import files that are in dictionary 


class wrdBank:
  #class attribute
  user_has_mood = False
  userMood_type = "null"

  # open files
  posWord = open('Postive mood words.txt')
  negWord = open('Negative sad words.txt')

  # reading the data from the files
  with posWord as f:
    data = f.read()

  #instance attribute
  def __init__(self, word):
    self.userInput = word

  # check files while there has being no return that the user is happyy or sad
  # get lines in a posWord file and check for userInput
  for line in posWord:
    if line in self.userInput:
      userMood_type = "pos"
      user_has_mood = True
      return "Postive"
    else:
      # get lines in a negWords file and check for userInput if they are no positive lines found
      for line in posWord:
        if line in self.userInput:
          userMood_type = "neg"
          user_has_mood = True
          return "Negative"

  #get users mood status here
  def getMood():
    print("Does user have a mood? {}\n The user has a {}".format(user_has_mood, userMood_type))
  
  


  """
  # dictionaries
  #check for sensitive feelings ...
  keyword_list = ["sad","angry","crying","dreadful","crazy","tired","dying"]
  for item in keyword_list:
    if item in user_input:
      return False
  return True
  """

  # driver program
  if __name__ == "__main__":
    print("one sec please...")