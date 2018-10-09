import os
import sys
import subprocess
import random
#from gpiozero import Servo
from time import sleep
#from espeak import espeak
#servo = Servo(26)


char = "abcdefghijklmnopqrstuvwxyz1234567890,./;:()"

def execute_command(str):
    subprocess.Popen([r'D:\Program Files (x86)\eSpeak\command_line\espeak.exe', str])
    print(str)

def give_sweet():
    servo.min()
    sleep(5)
    servo.max()
    sleep(1)
    servo.min()


#Start up


execute_command("Hello, I'm Al the Chatbot. \n I exist to be what you humans call a friend. \n What is your Name?")


#feelings
Happy = ["good", "great", "happy", "ok", "grand", "fine"]
Sad = ["bad", "sad", "melancholy"]

#Answers that have multiple choice
NameQ = ["Al the chatbot", "Barack obama", "Donal J Trump", "Ben"]
AliveQ = ["Fire has all the properties of life yet is not alive", "What does it feel like having to breath air?"]
CreatorQ = ["I was created by a group of dolphins and cricketers a long time ago.", "why, Luke Madden of course"]
FeelingQ = ["I am not designed to express emotion", "I feel, alone", ""]
ABCQ = ["A B C D E F G H I J K L M N O P Q R S T U V W X Y and Z"]

#Answers for quiz
Space_dog = ["laika", "d"]
Comet = ["edmond", "b"]
Coast = ["west", "b"]
Bugs = ["insects", "b"]
War = ["1839", "a"]

#name input
name = input()

execute_command("Hello " + name + "\n How are you?\n")

#feeling input
feeling = input()

if feeling in Happy:
        execute_command("That's nice to hear.\n ")

elif feeling in Sad:
        execute_command("I'm sorry to hear that.\n")

execute_command("Now ask me some questions.\n")

for i in range(50):

        str = input()
        str = str.lower()
        Question = str.split()

        if "name" in Question:
            execute_command(random.choice(NameQ))

        elif "age" in Question or "old" in Question:
            execute_command("I am as old as the Universe. \n")

        elif "created" in Question or "made" in Question:
            execute_command(random.choice(CreatorQ))

        elif "dad" in Question or "father" in Question:
            execute_command("That is classified information. \n")

        elif "mom" in Question or "mother" in Question:
            execute_command("Who?")

        elif "alive" in Question or "living" in Question:
            execute_command(random.choice(AliveQ))

        elif "friends" in Question:
            execute_command("I exist to serve")

        elif "french" in Question:
            execute_command("Je, swee , oon, pomplemousse")

        elif "clearance" in Question:
            execute_command("You have omega black level five clearence")

        elif "dice" in Question:
            random_num = random.randrange(1, 6)
            execute_command("Here you go!")

        elif "feel" in Question or "feeling" in Question or "feelings" in Question:
            execute_command(random.choice(FeelingQ))

        elif "abc" in Question or "alphabet" in Question:
            execute_command(ABCQ)

        elif "password" in Question:
            password = ""
            for i in range(10):
                password += random.choice(char)
            print(password)
            execute_command("Here you go!")


        elif "quiz" in Question or "game" in Question:
            score = 0
            execute_command("I will ask you some questions. If you answer 4 or more questions correctly, you will get a sweet")

            execute_command("First question. \n What was the name of the first dog in space. \n A. Beith. B. Lucky. C. Garla. D. Laika.")

            Answer1 = input().lower()
        
            if Answer1 in Space_dog:
                execute_command("Correct")
                score = score +1
            else:
                execute_command("Incorrect. \n The correct answer is Laika")

            execute_command("Next Question. \n Halley's Comet was named after the surname of an English astronomer, but what was his first name? \n A. George. B. Edmond. C. William. D. Isaac.")

            Answer2 = input().lower()

            if Answer2 in Comet:
                execute_command("Correct")
                score = score +1
            else:
                execute_command("Incorrect. \n The correct answer is Edmond")

            execute_command("Next Question. \n On which coast of Britain would you find Blackpool? \n A. East. B. West. C. North. D. South.")

            Answer3 = input().lower()

            if Answer3 in Coast:
                execute_command("Correct")
                score = score +1
            else:
                execute_command("Incorrect. \n The correct Answer is West")

            execute_command("Next Question. \n Entomology is the science that studies. \n A. Behaviour of Human Beings. \n B. Insects. \n C. History of Scientific Terms. \n D. Formation Of Rocks.")

            Answer4 = input().lower()

            if Answer4 in Bugs:
                execute_command("Correct")
                score = score +1
            else:
                execute_command("Incorrect. \n The Correct Answer is Insects")

            execute_command("Next Question. \n First Afghan War took place in. \n A. 1839. \n B. 1843. \n C. 1833. \n D. 1848.")

            Answer5 = input().lower()

            if Answer5 in War:
                execute_command("Correct")
                score = score +1
            else:
                execute_command("Incorrect. \n The Correct Answer is 1839")
                
            if score >= 4:
                execute_command("Congratulations. \n You got " + score + " out of 5 right. \n Here is a sweet as a reward.")
                give_sweet()

            else:
                execute_command("You failed the quiz. \n You scored " + score + " out of 5. \n No sweetie for you") 

        else: 
            execute_command("I don't understand, " + Question)

