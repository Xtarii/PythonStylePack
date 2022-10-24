#imports:
import time



#extras:
#denna delen är lånad av google för att färger i window är väldigt compliserade
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
#detta är en loadingbar som spinner runt
def loadingbar_spinning(sleep=float(0.1), times=int(3), text=str("Loading: ")):
    print(Colors["BOLD"] + text + " ", sep="", end="", flush=True)
    for x in range(times):
        for x in r"-\|/-\|/":
            print("\b", Colors["FAIL"] + x, sep="", end="", flush=True)
            time.sleep(sleep)
    
    print("\b|", Colors["ENDC"] + "\n\n")


#detta är en loadingbar som bara är ett streck
def loadingbar_line(sleep=float(0.1), times=int(51), text=str("Loading: ")):
    print(Colors["BOLD"] + text + " ", sep="", end="", flush=True)
    for x in range(times):
        print(Colors["FAIL"] + "#", sep="", end="", flush=True)
        time.sleep(sleep)
    
    print(Colors["ENDC"] + "\n\n")