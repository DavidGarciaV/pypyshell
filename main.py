from functions import psh_cd
from functions import *

def main():
    while True:
        inp = input("$ ")
        if inp == "exit":
            break
        elif inp[:3] == "cd ":
            psh_cd(inp[:3])
        elif inp == "help" or inp == "h":
            psh_help()
        else:
            execute(inp)


if '__main__' == __name__:
    main()

