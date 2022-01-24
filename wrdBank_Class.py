import random
import ast #imports any form of files
import json # import files that are in dictionary 

# open files from word_banks folder
posWord = open('Positive_mood_words.txt')
negWord = open('Negative_sad_words.txt')

# reading the data from the files
with posWord as p:
  posData = p.read()
with negWord as n:
  negData = n.read()

class wrdBank:
  #class attribute
  #user_has_mood = False
  #userMood_type = ""
  #userInput = ""


  # reconstructing file to dictionary using ast
  #newPosData = ast.literal_eval(posData)
  
  #instance attribute
  def __init__(self, word):
    self.userMood_type = ""
    self.user_has_mood = False
    self.moodChecker_loop(word)

  #mood lop
  def moodChecker_loop(self, usIn):
    #check postive list first
    if(self.pChecker(usIn) == True):
      self.userMood_type = "Positive"

    # if postive returns False check negative list
    elif(self.nChecker(usIn) == True):
      self.userMood_type = "Negative"

    # if negative returns false return fine
    else:
      self.userMood_type = "Fine"

  # check files while there has being no return that the user is happyy or sad
  #checks postive list
  def pChecker(self, word):
    # get lines in a posWord file and check for userInput
    for line in posData:
      if line in word:  #happy is in "I am so happy today"
        self.user_has_mood = True
        return True
      #else: 
    return False

  def nChecker(self, word):
    # get lines in a negWords file and check for userInput if they are no positive lines found
    for nline in negData:
      if nline in word: #angry is in "im am angry"
        self.user_has_mood = True
        return True
      else: 
        return False

  def getMood(self):
    return self.userMood_type

  #get users mood status here
  def getMood_status():
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
  #if __name__ == "__wrdBank_Class__":
  #  print("one sec please...")