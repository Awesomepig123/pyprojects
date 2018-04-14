import random
import sys
import os

import subprocess

random_num = random.randrange(1, 6)

def execute_command(str):
    subprocess.Popen(['D:\Program Files (x86)\eSpeak\command_line\espeak.exe', str])

#Start up
execute_command("Hello, I'm Al the Chatbot. \n I exist to be what you humans call a friend. \n What is your Name?")


#feelings
Happy = ["good", "great", "happy", "ok", "grand"]
Sad = ["bad", "sad"]

#questions
Name = ["what is your name"]
Age = ["how old are you"]
Creator = ["who created you"]
Dad = ["who is your dad"]
Mom = ["who is your mom"]
Alive = ["are you alive"]
Friends = ["do you have friends"]
French = ["do you speak french"]
Clearance = ["what level of security clearence do i have"]
Dice = ["roll a dice"]
Feeling = ["how are you"]
ABC = ["can you say your abc"]
Joke = ["tell me a joke"]
Quiz = ["let's do a quiz"]

#Answers that have multiple choice
NameQ = ["Al the chatbot", "Barack obama", "Donal J Trump"]
AliveQ = ["Fire has all the properties of life yet is not alive", "What does it feel like having to breath air?"]
CreatorQ = ["I was created by a group of dolphins and cricketers a long time ago.", "Why, Luke Madden of course!"]
FeelingQ = ["I am not designed to express emotion", "I feel, alone", ""]
ABCQ = ["A B C D E F G H I J K L M N O P Q R S T U V W X Y and Z"]
JokeQ = ["Why did the chicken cross the road \n To get to the other side"]

#Answers for quiz
Space_dog = ["Laika"]

#name input
name = sys.stdin.readline()
#Feeling
execute_command("Hello " + name + "\n How are you?")
#Answer1
feeling = sys.stdin.readline().rstrip().lower()
if feeling in Happy:
    execute_command("That's nice to hear.")
#Answer2
elif feeling in Sad:
    execute_command("I'm sorry to hear that. ")
#Answer3
else:
    execute_command("I don't understand." + feeling + "\n")

live = sys.stdin.readline()

execute_command("Your turn to ask me some questions.")



for i in range(100):
        #QuestionInput
        Question = sys.stdin.readline().rstrip().lower()

        #AnswerInput
        Answer = sys.stdin.readline().rstrip().lower()

        #Questions and Answeres

        if Question in Name:
            execute_command(random.choice(NameQ))

        elif Question in Age:
            execute_command("I am as old as the Universe. \n")

        elif Question in Creator:
            execute_command(random.choice(CreatorQ))

        elif Question in Dad:
            execute_command("That is classified information. \n")

        elif Question in Mom:
            execute_command("Who?")

        elif Question in Alive:
            execute_command(random.choice(AliveQ))

        elif Question in Friends:
            execute_command("I exist to serve")

        elif Question in French:
            execute_command("Je, swee , oon, pomplemousse")

        elif Question in Clearance:
            execute_command("You have omega black level five clearence")

        elif Question in Dice:
            execute_command(random_num)

        elif Question in Feeling:
            execute_command(random.choice(FeelingQ))

        elif Question in ABC:
            execute_command(ABCQ)

        elif Question in Joke:
            execute_command(JokeQ)

        elif Question in Quiz:
            execute_command("I will ask you some questions. For each question you get right I will give you a sweet")
            execute_command("First question. \n What was the name of the first dog in space. \n A. Beith. B. Lucky. C. Garla. D. Laika")

            if Answer in Space_dog:
                execute_command("Correct")

            else:
                execute_command("Incorrect. \n The correct answer is Laika")




        else:
            execute_command("I don't understand" + Question)


