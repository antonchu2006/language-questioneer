#!/usr/bin/python3
import random, sys, os

def clear():
      
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def question(integer, file):

    clear()
    f = open(file, "r")
    lines = f.readlines()

    spanish = []
    english = []

    for line in lines:
        line = line.strip("\n")
        
        pieces = line.split(":")

        spanish.append(str(pieces[0]))
        english.append(str(pieces[1]))

    if len(spanish) != len(english):
        print("[!] Error, revisa la lista txt.")
        sys.exit(1)

    randominteger = integer

    print(spanish[randominteger])
    inputt = input("Cómo se dice en inglés?: ")
    
    clear()
    
    print("La respuesta: " + str(english[randominteger]))
    print("Tu respuesta: " + str(inputt))

def main():
    if len(sys.argv) != 2:
        print("[!] Usage: python3 {} <vocabulary.txt>".format(sys.argv[0]))
        print("The vocabulary must be in the format español:inglés")
        sys.exit(1)

    f = open(str(sys.argv[1]), 'r')
    lines = f.readlines()

    nums = list(range(0, int(len(lines))))

    for i in nums:
        question(i, str(sys.argv[1]))

if __name__ == "__main__":
    main()