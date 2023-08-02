#morse translate
import sys

def menu():
    inpc = input("\nPlease select from the options below:\n\n1) Translate into morse\n\n2) Translate from morse\n\n3) Exit translator\n\n")
    if inpc == "1":
        intoM()
    elif inpc == "2":
        fromM()
    elif inpc == "3":
        sys.exit("Exiting translator")
    else:
        print("Not a vaild input")
        menu()

def intoM():
    n = 0
    print("\nYou have chosen, translate INTO morse\nIf you would like to return to the selection menu just input: ~\n")
    while n == 0:
        Mout = []
        Moutp = []
        inpd = input("Input: ")
        if inpd == "~":
            n = 1
            menu()
        elif inpd != "~":
            for latters in inpd:
                if latters.upper() == "A":
                    Mout.append(".- ")
                if latters.upper() == "B":
                    Mout.append("-... ")
                if latters.upper() == "C":
                    Mout.append("-.-. ")
                if latters.upper() == "D":
                    Mout.append("-.. ")
                if latters.upper() == "E":
                    Mout.append(". ")
                if latters.upper() == "F":
                    Mout.append("..-. ")
                if latters.upper() == "G":
                    Mout.append("--. ")
                if latters.upper() == "H":
                    Mout.append(".... ")
                if latters.upper() == "I":
                    Mout.append(".. ")
                if latters.upper() == "J":
                    Mout.append(".--- ")
                if latters.upper() == "K":
                    Mout.append("-.- ")
                if latters.upper() == "L":
                    Mout.append(".-.. ")
                if latters.upper() == "M":
                    Mout.append("-- ")
                if latters.upper() == "N":
                    Mout.append("-. ")
                if latters.upper() == "O":
                    Mout.append("--- ")
                if latters.upper() == "P":
                    Mout.append(".--. ")
                if latters.upper() == "Q":
                    Mout.append("--.- ")
                if latters.upper() == "R":
                    Mout.append(".-. ")
                if latters.upper() == "S":
                    Mout.append("... ")
                if latters.upper() == "T":
                    Mout.append("- ")
                if latters.upper() == "U":
                    Mout.append("..- ")
                if latters.upper() == "V":
                    Mout.append("...- ")
                if latters.upper() == "W":
                    Mout.append(".-- ")
                if latters.upper() == "X":
                    Mout.append("-..- ")
                if latters.upper() == "Y":
                    Mout.append("-.-- ")
                if latters.upper() == "Z":
                    Mout.append("--.. ")
                if latters.upper() == "0":
                    Mout.append("----- ")
                if latters.upper() == "1":
                    Mout.append(".---- ")
                if latters.upper() == "2":
                    Mout.append("..--- ")
                if latters.upper() == "3":
                    Mout.append("...-- ")
                if latters.upper() == "4":
                    Mout.append("....- ")
                if latters.upper() == "5":
                    Mout.append("..... ")
                if latters.upper() == "6":
                    Mout.append("-.... ")
                if latters.upper() == "7":
                    Mout.append("--... ")
                if latters.upper() == "8":
                    Mout.append("---.. ")
                if latters.upper() == "9":
                    Mout.append("----. ")
                if latters.upper() == ".":
                    Mout.append(".-.-.- ")
                if latters.upper() == ",":
                    Mout.append("--..-- ")
                if latters.upper() == "?":
                    Mout.append("..--.. ")
                if latters.upper() == " ":
                    Mout.append(" ")
            Moutp = "".join(Mout)
            print(Moutp)

def fromM():
    n = 0
    print("\nYou have chosen, translate FROM morse\nIf you would like to return to the selection menu just input: ~\n(Note: please leave a space between all morse characters)\n")
    while n == 0:
        inpb = input("Input: ")
        if inpb == "~":
            n = 1
            menu()
        elif inpb != "~":
            Eouts = []
            Eout = inpb.split(" ")
            for x in Eout: 
                if x == ".-":
                    Eouts.append("a ")
                if x == "-...":
                    Eouts.append("b ")
                if x == "-.-.":
                    Eouts.append("c ")
                if x == "-..":
                    Eouts.append("d ")
                if x == ".":
                    Eouts.append("e ")
                if x == "..-.":
                    Eouts.append("f ")
                if x == "--.":
                    Eouts.append("g ")
                if x == "....":
                    Eouts.append("h ")
                if x == "..":
                    Eouts.append("i ")
                if x == ".---":
                    Eouts.append("j ")
                if x == "-.-":
                    Eouts.append("k ")
                if x == ".-..":
                    Eouts.append("l ")
                if x == "--":
                    Eouts.append("m ")
                if x == "-.":
                    Eouts.append("n ")
                if x == "---":
                    Eouts.append("o ")
                if x == ".--.":
                    Eouts.append("p ")
                if x == "--.-":
                    Eouts.append("q ")
                if x == ".-.":
                    Eouts.append("r ")
                if x == "...":
                    Eouts.append("s ")
                if x == "-":
                    Eouts.append("t ")
                if x == "..-":
                    Eouts.append("u ")
                if x == "...-":
                    Eouts.append("v ")
                if x == ".--":
                    Eouts.append("w ")
                if x == "-..-":
                    Eouts.append("x ")
                if x == "-.--":
                    Eouts.append("y ")
                if x == "--..":
                    Eouts.append("z ")
                if x == "-----":
                    Eouts.append("0 ")
                if x == ".----":
                    Eouts.append("1 ")
                if x == "..---":
                    Eouts.append("2 ")
                if x == "...--":
                    Eouts.append("3 ")
                if x == "....-":
                    Eouts.append("4 ")
                if x == ".....":
                    Eouts.append("5 ")
                if x == "-....":
                    Eouts.append("6 ")
                if x == "--...":
                    Eouts.append("7 ")
                if x == "---..":
                    Eouts.append("8 ")
                if x == "----.":
                    Eouts.append("9 ")
                if x == ".-.-.-":
                    Eouts.append(". ")
                if x == "--..--":
                    Eouts.append(", ")
                if x == "..--..":
                    Eouts.append("? ")
            Eoutp = "".join(Eouts)
            print(Eoutp)
                

inpa = input("\nHello, this is MOIK's Morse code translator \nto use, please select from the options below:\n\n1) Translate into morse\n\n2) Translate from morse\n\n3) Exit translator\n\n")
if inpa == "1":
    intoM()
elif inpa == "2":
    fromM()
elif inpa == "3":
    sys.exit("Exiting translator")
else:
    print("Not a vaild input")
    menu()