from time import sleep
import os

username1 = input("Please choose a username: ")
sleep(0.5)
password1 = input("Please choose a password: ")
sleep(0.5)
os.system('cls')

username2 = input("Please enter your username: ")
sleep(0.5)
password2 = input("Please enter your password: ")
sleep(0.5)
os.system('cls')

if username1 == username2:
    if password1 == password2:
        print("Welcome to your private space. Please enjoy your time here.")
    if password1 != password2:
        print("You have entered the incorrect username or password.")
        quit()
            
if username1 != username2:
    if password1 == password2:
        print("You have entered the incorrect username or password.")
        quit()
    if password1 != password2:
        print("You have entered the incorrect username and password.")
        quit()