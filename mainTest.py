# use python {filename}.py in shell to run test

import unittest

#imported functions/classes
from wrdBank_Class import wrdBank
from main import check_response

# test contained in main
'''def list()
    def check_response(user_input):  # check people feelings through response
    def sad_story(user_input): #sad story interation
    def happy_story(): #happ story interaction
    def mainMenu_chat() : # othertopic chat interation
    def response_to_topic(user_input): # response to chat topic
    def users_story(r): #r states user's response  
    def start_chat():# start bot chat '''

class TestCheckResponse(unittest.TestCase):
  #error in code : code reruns only positive
  def test_positive(self):
    #assertIn(a,b) if a in b
    self.assertIn("Positive", check_response("I am so happy today"))

  def test_negative(self):
    self.assertIn("Negative", check_response("I am angry"))

  
if __name__ == '__main__':
    unittest.main()