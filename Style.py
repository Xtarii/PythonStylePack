#this file was created by Xtarii and uploaded to Github: https://github.com/Xtarii/PythonStylePack

#imports:
import time



#extras:
#this part is taken form google "StackOverflow" https://stackoverflow.com/questions/67241111/python-colored-text-to-the-terminal#:~:text=The%20most%20basic%20terminals%20have%20a%20set%20of,%5Cu001b%20%5B36m%208%20White%3A%20%5Cu001b%20%5B37m%20Fler%20objekt
Colors = {
    "HEADER": '\033[95m',
    "BLUE": '\033[94m',
    "CYAN": '\033[96m',
    "GREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[96m'
}



#defs:
#this is a round loadingbar
def loadingbar_spinning(sleep=float(0.1), times=int(3), text=str("Loading: ")):
    print(Colors["BOLD"] + text + " ", sep="", end="", flush=True)
    for x in range(times):
        for x in r"-\|/-\|/":
            print("\b", Colors["FAIL"] + x, sep="", end="", flush=True)
            time.sleep(sleep)
    
    print("\b|", Colors["ENDC"] + "\n\n")


#this is a loadingbar line
def loadingbar_line(sleep=float(0.1), times=int(51), text=str("Loading: ")):
    print(Colors["BOLD"] + text + " ", sep="", end="", flush=True)
    for x in range(times):
        print(Colors["FAIL"] + "#", sep="", end="", flush=True)
        time.sleep(sleep)
    
    print(Colors["ENDC"] + "\n\n")
