from time import sleep
import os
print("!Warning! Please do not use dollar signs. Only numbers and decimal points are allowed. You must restart the program in order to switch from one calculator to another.")
sleep(2)
COrder = input("What calculator type?\n 1. One\n 2. Two\n?")
CType = input("What would you like to calculate?\n1. Sales Tax\n2. Markup\n3. Discount\n")
os.system('cls')

def CSalesTax1(): #Calculates sales tax percentage
    while True:
        PriceBeforeTax = input("Price before tax: ")
        PriceAfterTax = input("Price after tax: ")
        sleep(0.5)
        Difference = float(PriceAfterTax) - float(PriceBeforeTax)
        TaxPer = float(Difference) / float(PriceBeforeTax)
        print("Sales tax: "+"{:.2%}".format(TaxPer));
        sleep(1)
        print("\n")
        Reset = input("Would you like to calculate another sales tax? Y/N: ")
        if Reset.casefold() == "Y" or "Yes":
            os.system('cls')
            sleep(1)
            CSalesTax1()
        if Reset.casefold() == "N" or "No":
            os.system('cls')
            exit()
            
def CMarkup1(): #Calculates markup percentage
    while True:
        PriceBeforeMarkup = input("Production cost/pre-markup cost: ")
        PriceAfterMarkup = input("Price after markup: ")
        sleep(0.5)
        Difference = float(PriceAfterMarkup) - float(PriceBeforeMarkup)
        MarPer = float(Difference) / float(PriceBeforeMarkup)
        print("Markup: "+"{:.2%}".format(MarPer));
        sleep(1)
        print("\n")
        Reset = input("Would you like to calculate another markup? Y/N: ")
        if Reset.casefold() == "Y" or "Yes":
            os.system('cls')
            sleep(1)
            CMarkup1()
        if Reset.casefold() == "N" or "No":
            os.system('cls')
            exit()
            
def CDiscount1(): #Calculates discount percentage
    while True:
        PriceBeforeDiscount = input("Price before discount: ")
        PriceAfterDiscount = input("Price after discount: ")
        sleep(0.5)
        Difference = float(PriceBeforeDiscount) - float(PriceAfterDiscount)
        DisPer = float(Difference) / float(PriceBeforeDiscount)
        print("Discount: "+"{:.2%}".format(DisPer));
        sleep(1)
        print("\n")
        Reset = input("Would you like to calculate another discount? Y/N: ")
        if Reset.casefold() == "Y" or "Yes":
            os.system('cls')
            sleep(1)
            CDiscount1()
        if Reset.casefold() == "N" or "No":
            os.system('cls')
            exit()
            
            
if COrder.casefold() == "1" or "One":
    if CType.casefold() == "1" or "Sales Tax":
        CSalesTax1()
    if CType.casefold() == "2" or "Markup":
        CMarkup1()
    if CType.casefold() == "3" or "Discount":
        CDiscount1()

if COrder.casefold() == "2" or "Two":
    if CType.casefold() == "1" or "Sales Tax":
        CSalesTax2()
    if CType.casefold() == "2" or "Markup":
        CMarkup2()
    if CType.casefold() == "3" or "Discount":
        CDiscount2()

    
