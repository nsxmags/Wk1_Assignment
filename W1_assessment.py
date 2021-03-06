## Maggie Cheng
## 06 May 2020
## Title --> Week 1 Mini Assessment 1 - A trivia game online
## Requirements: 
##    1. ask them questions using the input command and then,
##    2. save their answers as variables, and at the end,
##    3. tell them how interesting they were and
##    4. give them a summary of all of their answers.
## Resources: https://parade.com/944584/parade/trivia-questions-for-kids/

import time

time.sleep(1)
for i in "LOADING.....":
    print(i, sep=' ')

time.sleep(1)

print("Oh! Hello there!\nHave you been waiting for long?")
time.sleep(2)

answer_start = input("Please input \"1\" for Yes or \"0\" for No")
time.sleep(2)

if answer_start == "1":
    print("Oops, I couldn't remember where I left the trivia questions.\nOh I found them!")
else: 
    print("Well I am glad you are here!")

print()
time.sleep(4)

print("Do you like Trivia? What a silly question to ask. Of course you do!\nWhy else will you be here playing this online trivia game?\nU-hmmm, sorry, I am so happy you are here, I am getting a bit carried away!")
time.sleep(6)

print()
print("Oh how rude of me! Let me introduce myself.\nMy name is Ben, Ben Dover and I am your host to this trivia game...\nHey, why is it that everytime I introduce myself, someone is laughing?!")
time.sleep(6)

print()
print("You look like a kind person, what is your name?")
time.sleep(2)

name = input("Please type your name here: ")
for i in range(2):
    print("Processing...")
    time.sleep(2)

print(f"Welcome, {name}. It is a pleasure to meet you!")
time.sleep(2)

print()
print(f"I have 3 trivia questions for you today, {name}. If you get all 3 questions correct, I will reward you with a quote.")
time.sleep(1)

print("Let's see how you go shall we?...")
print()

wins = 0

time.sleep(4)

print("Question 1: How many pairs of wings do bees have?")
time.sleep(2)

answer_1 = input("The answer is between 1 and 4. Please type your answer here: ")
time.sleep(2)

if answer_1 == "2":
    print(f"Geez {name}, ain't you a clever duck!")
    wins += 1
else: 
    print(f"{name}, did you tried to count them whilst the bee was flying, because I initially had the same answer as you!")      
    
time.sleep(4)

print()   
print("Question 2: What is another name for a female deer?\nThis is a multiple choice question.\nOptions:")
time.sleep(2)

answer_2 = input(" dim\n doe\n day\nPlease type your answer here: ")
time.sleep(2)      
      
if answer_2 == "doe":
    print(f"Correct-o-mundo, {name}! The answer is {answer_2}. You must have watched \"The Sound of Music\" my friend!")
    wins += 1
else: 
    print(f"Oh {name}, the answer is not {answer_2}, this one was tough. I promised the next question will be easier.")
    
time.sleep(4)

print()
print("Question 3: What kind of cat is considered bad luck?\nThis is another multiple choice question.\nOptions:")
time.sleep(2)

answer_3 = input(" stray\n ugly\n black\nPlease type your answer here: ")
time.sleep(2)
      
if answer_3 == "black":
    print(f"Hey {name}, you are right! You won't happen to own a black cat will you?")
    wins += 1
else: 
    print(f"Hmm, incorrect. I personally think Black cats are actually quite regal-looking.")      
    
time.sleep(4)

print()
print("Okay, let's check the final results!")
print("." * 50)
time.sleep(4)

print()
print("You have correctly answered {} out of 3 questions.".format(wins))
time.sleep(4)

if wins > 2:    
    print("""
    Woohoooooo!!! Congratulations!
    
    As promised, here's a quote as your reward:
        --When I’m in social situations, I always hold onto my glass.
         It makes me feel comfortable and secure and I don’t have to shake hands.--
                                    —Larry (Larry David), Curb Your Enthusiasm
                                    
    I think I can use this piece of advice too!""")    
    time.sleep(2)   
    print(f"{name}, you are a really cool cat!\nThanks for playing. Until next time, so long!")
    
    time.sleep(20)
else:
    print(f"Ohh well {name}, better luck next time!\nThanks for playing and for keeping your cool.\nUntil next time, so long!")
    
    time.sleep(10)