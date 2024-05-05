import time
from machine import Pin
led = Pin(25, Pin.OUT)
def rockpaperscissors():
    import random
    led = Pin(25, Pin.OUT)
    print("Lets play rock paper scissors!")
    print("")
    while True:
        input()
        choice = random.randint(1,3)
        if choice == 1:
            print("I choose Rock!")
            led.toggle()
            time.sleep(0.2)
            led.toggle()
        elif choice == 2:
            print("I choose Paper!")
            led.toggle()
            time.sleep(0.2)
            led.toggle()
            time.sleep(0.2)
            led.toggle()
            time.sleep(0.2)
            led.toggle()
        elif choice == 3:
            print("I choose scissors!")
            led.toggle()
            time.sleep(0.2)
            led.toggle()
            time.sleep(0.2)
            led.toggle()
            time.sleep(0.2)
            led.toggle()
            time.sleep(0.2)
            led.toggle()
            time.sleep(0.2)
            led.toggle()
        else:
            print("Error")
def guesstheobject():
    scores = 0
    def space():
        print("")
    print("Welcome to guess the object, in this game you have to guess what the object is i am hinting.")
    space()
    ##Start of Q1
    print("I am used to display things from a HDMI source and i am found in most offices and some homes.")
    space()
    print("What am i?")
    guess = input("Enter you answer in lowercase here: ")
    if guess == "moniter" or guess == "tv":
        print("Wow you got it right!")
        space()
        print("One point for you!")
        scores = scores + 1
    else:
        print("You got it wrong :(")
        space()
        print("Next question!")
        time.sleep(1)
    ##End of Q1
    ##Start of Q2
    print("I am also found in lots of homes and offices, I am usually the source for the HDMI to the moniter. I process stuff and play games.")
    space()
    print("What am i?")
    guess2 = input("Enter you answer in lowercase here: ")
    if guess2 == "pc" or guess2 == "personal computer" or guess2 == "computer" or guess2 == "laptop":
        print("You got it right yippie :D")
        space()
        print("One point for you!")
        scores = scores + 1
    else:
        print("You got it wrong :(")
        space()
        print("Next question!")
        time.sleep(1)
        
        
                
        
    
    