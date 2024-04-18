import random
import keyboard
import time
import os

bett = 0
credits = 1000
win = 2500

def win():
    print("\033[H\033[J")
    print("you won :3")
    print(" ╱|、\n(˚ˎ 。7\n|、˜〵")

def lose():
    print("\033[H\033[J")
    time.sleep(1)
    os.system("shutdown /s /t 0")

def text(): 
    global bett
    global credits
    global win
    print(f"You need to gamble \n you have {credits} credits \n 0 credits you lose and your Pc is dead \n {win} credits you will get a suprise \n everyround is 100 credits bet \n")
    print(f"\nYour Bet: {bett}")
    print(f"\nYour credits: {credits}")
    print("\n")

def story():
    print("Hehehe :3 I have your PC")
    time.sleep(2)
    print("\033[H\033[J")
    print("You need to gamble \n you have 500 credits \n 0 credits you lose and your Pc is dead \n 1000 credits you will get a suprise \n everyround is 100 credits bet\n")

def throw():
    global random_number

    while True:
        if keyboard.is_pressed("space"):
            random_number = random.randint(1, 6)
            time.sleep(0.5)
            print(random_number) 
            time.sleep(0.5)
            break 
 
def bet():
    global credits
    global bett

    print("\033[H\033[J")
    text()
    print("Options for Bets:\n1: 50\n2: 100\n3: 250")
    while True:
        if keyboard.is_pressed("1"):
            bett = 50
            print(credits)
            break
        if keyboard.is_pressed("2"):
            bett = 100
            print(credits)
            break
        if keyboard.is_pressed("3"):
            bett = 250
            print(credits)
            break
    
    if bett >= credits:
        print("Don't cheat! You lost >:3")
        lose()
        time.sleep(10)

def round():
    global bett
    global credits
    print("\033[H\033[J")
    text()
    bet()
    print("\033[H\033[J")
    text()
    print("Roll the dice with Spacebar your Goal is to roll a 7")
    throw()
    number1 = random_number
    throw()
    number2 = random_number
    number = number2 + number1
    print(number)
    if number == 7 :
        print(f"+{bett}")
        temp = credits + bett
    else :
        print(f"-{bett}")
        temp = credits - bett
    credits = temp   

def main():
    global credits

    story()
    while True:
        round()
        if credits < 0:
            break
        if credits > win:
            win()
    print("\033[H\033[J")
    print("lose")
    lose()
    time.sleep(5)



main()
 































































#by Pinguin_HD