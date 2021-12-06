#  This is my first battle game. Very bare-bones, more of a proof-of-concept. All of this code was written from scratch and therefore I don't really have any due credits to give.
#  I've never written a battle in anything from scratch or even compiled a python program. So yes, there will likely be issues. However, I would also like to hear them! If you want
#  to take the time and critique this code or my coding in general, you can contact me at strabane@gmail.com

#  I am fairly new to python, and this as a result is still a somewhat abmbitious project for me, despite being relatively unimpressive in a grand scheme.
#  This code is also slightly old, and as a result does not use else/elif statements as much as it really should. I have (since originally coding it) learned those statements, but
#  they will not appear here. I know it's really dumb to not know how to else/elif even as a beginner, but you really should take the phrase "beginner" here literally; this is quite
#  literally one of my first programs. 

#  For those of you who aren't "in the know" about my characters used here, I will explain briefly (with little depth): Quitus is a lawful neutral, and Heciost
#  is a fan-made Ultra Beast of mine. Both of these characters exist in the Pokemon universe.

from time import sleep
import random
import os

def game():
    firstTime = 0
    while quitusHealth > 0:
        validone = ['1', 'one', 'bludgeon']
        validtwo = ['2', 'two', 'blaster']
        blaDamage = 0 
        swDamage = 0 
        shDamage = 0
        heciostAttack = 0
        moveAccuracy = 0
        hecAbsorb = 0
        cantShock = 0
        killed = 0
        print("Heciost attacks!")
        if firstTime = 0:  
            heciostHealth = 75 
            quitusHealth = 95 
            blastUses = 2 
            bludgeonUses = 5 
            fieldState = 3
        if heciostHealth <= 0:
            os.system('cls')
            print("Quitus defeated Heciost!")
            break
        if killed == 1:
            os.system('cls')
            print("Quitus defeated Heciost!")
            break
        if fieldState <= 0:
            cantShock = 1
        if quitusHealth <= 0:
            os.system('cls')
            print("Quitus was fatally wounded!")
            sleep(0.5)
            resetButton = input("You died. Would you like to retry? Y/N: ")
            if resetButton.casefold() == "y" or "yes":
                os.system('cls')
                resetvar()
                game()
            if resetButton.casefold() == "n" or "no":
                os.system('cls')
                print("Terminating game, please wait...")
                sleep(1.3)
                print("Terminated.")
                break
        print("\n")
        print("Heciost HP: ",heciostHealth, "")
        sleep(0.25)
        print("Quitus HP: ",quitusHealth, "\n")
        sleep(1.25)
        print("1. Bludgeon (uses left: ", bludgeonUses, ")")
        sleep(0.5)
        print("2. Blast (uses left: ", blastUses, ")")
        afterFirst()
        sleep(0.5)
        choice = input("What will Quitus do?  ")
        sleep(1)
        os.system('cls')
        if cantShock == 0:
            heciostAttack = random.randint(0, 1)
        if cantShock == 1:
            heciostAttack = 0
        if heciostAttack == 0:
            swDamage = random.randint(25, 35)
            print("Heciost swung its sword!\n")
            moveAccuracy = random.randint(1, 100)
            if moveAccuracy <= 90:
                sleep(0.25)
                quitusHealth - swDamage
                print(swDamage, "damage to Quitus!\n")
                sleep(3)
                os.system('cls')
                afterfirst()
            if moveAccuracy >90:
                sleep(0.25)
                print("...But it missed!\n")
                sleep(2)
                afterfirst()
                os.system('cls')
        if heciostAttack == 1:
            shDamage = random.randint(30, 40)
            print("The fields charged power!")
            sleep(1.5)
            print("A lightning bolt bulleted from the fields at Quitus!")
            moveAccuracy = random.randint(1, 100)
            if moveAccuracy <= 75:
                sleep(1.50)
                print(shDamage, "damage to Quitus!")
                quitusHealth - shDamage
                sleep(1.50)
                os.system('cls')
            if moveAccuracy > 75:
                sleep(1.5)
                print("...But it missed!")
                sleep(1.5)
                os.system('cls')
                
        if choice.casefold() in validone:
            bluDamage = random.randint(10, 25)
            moveAccuracy = random.randint(1, 100)
            print("Quitus swung his baton at one of the cores!")
            bludgeonUses - ppdeduct
            if moveAccuracy <= 90:
                fieldState - 1
                heciostHealth - bluDamage
                print(bluDamage, "damage to Heciost!")
                sleep(0.5)   
                if fieldState == 2:
                    print("A field was downed!")
                    sleep(0.56)
                    print("Two of the other cores are protecting the downed field!\n")
                    sleep(2.5)
                    os.system('cls')
                if fieldState == 1:
                    print("Another field was downed!")
                    sleep(0.54)
                    print("The two cores are hiding behind the last field!\n")
                    sleep(2.5)
                    os.system('cls')
                if fieldState == 0:
                    print("The final field was downed!")
                    sleep(0.48)
                    print("All the fields were downed!\n")
                    sleep(2.5)
                    os.system('cls')
            if moveAccuracy > 90:
                sleep(0.5)
                print("...But it missed.")
                sleep(1.5)
                os.system('cls')
        if choice.casefold() in validtwo:
            blaDamage = random.randint(30, 45)
            blastUses - ppdeduct
            moveAccuracy = random.randint(1, 100)
            print("Quitus charged his laser cannon!")
            sleep(0.5)
            print("A powerful blinding shot flashed from the laser cannon!")
            if moveAccuracy <= 80:
                if fieldState > 0:
                    hecAbsorb = blaDamage / 2
                    sleep(1)
                    print("The intact fields absorbed the enormous blast and gained" ,hecAbsorb, "HP!")
                    sleep(2.75)
                    os.system('cls')
                    heciostHealth + hecAbsorb
                if fieldState <= 0:
                    heciostHealth = 0
                    killed = killed + 1
            if moveAccuracy > 80:
                sleep(0.5)
                print("...The cannon had an unexpected malfunction!")
                sleep(2.5)
                os.system('cls')
game()

#  And this is where the script itself ends. I would have programmed graphics into this...if I knew how. Until next time!
#     -Halder