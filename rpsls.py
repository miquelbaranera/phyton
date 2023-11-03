import random

def PresentacioJoc ():
    print("Pedra, paper, tisores, llangardaix, Spock és un joc d'atzar ampliació popular Pedra, paper, tisores") 
    print("Creat per Sam Kass amb Karen Bryla http://www.samkass.com/theories/RPSSL.html") 
    print("Popularitzat per Sheldon Cooper a la sèrie Big Bang Theory.")
    print("Es fa servir per solucionar una disputa entre Sheldon i Raj en el capítol The Lizard - Spock Expansion ")
    print("El joc és al millor de N partides on N és un nombre senar \n")


def Senar(num):
    if (num%2==0):
        return False
    else:
        return True

def LlegirSenar():
    num = int(input("Introdueix el nombre (senar) de partides que vols fer: "))
    senar= Senar(num)
    while (senar == False):
        print("ERROR: El nombre introduït és parell ")
        num = int(input("Introdueix el nombre (senar) de partides que vols fer: "))
        senar= Senar(num)
    return num

def MenuRPSLS():
    print("Escull entre:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("4 - Lizard")
    print("5 - Spock")

def LlegirNombre (Min,Max):
    num = int(input("Entra un valor entre " +str(Min)+ " i " +str(Max)+":"))
    while (num > Max) or (num < Min):
        print("Error: Valor fora de l'interval")
        num = int(input("Entra un valor entre " +str(Min)+ " i " +str(Max)+ ":"))
    return num
  
def JocRPSLS(j1,j2):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOCK = 5
    if (j1 == j2):
        return 0
    elif (j1 == ROCK):
        if (j2 == PAPER) or (j2 == SPOCK):
            return 2
        else:
            return 1
    elif (j1 == PAPER):
        if (j2 == SCISSORS) or (j2 == LIZARD):
            return 2
        else:
            return 1
    elif (j1 == SCISSORS):
        if (j2 == ROCK) or (j2 == SPOCK):
            return 2
        else:
            return 1
    elif (j1 == LIZARD):
        if (j2 == SCISSORS) or (j2 == ROCK):
            return 2
        else:
            return 1    
    elif (j1 == SPOCK):
        if (j2 == PAPER) or (j2 == LIZARD):
            return 2
        else:
            return 1



def MissatgeRPSLS(j1,j2):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOCK = 5
    if (j1 == j2):
        print("Empat")
    elif (j1 == SCISSORS and j2 == PAPER) or (j1 == PAPER and j2 == SCISSORS):
        print("Scissors cuts Paper \n")
    elif (j1 == PAPER and j2 == ROCK) or (j1 == ROCK and j2 == PAPER):
        print("Paper covers Rock \n")
    elif (j1 == ROCK and j2 == LIZARD) or (j1 == LIZARD and j2 == ROCK):
        print("Rock crushes Lizard \n")
    elif (j1 == LIZARD and j2 == SPOCK) or (j1 == SPOCK and j2 == LIZARD):
        print("Lizard poisons Spock \n")
    elif (j1 == SCISSORS and j2 == SPOCK) or (j1 == SPOCK and j2 == SCISSORS):
        print("Spock smashes Scissors \n")
    elif (j1 == SCISSORS and j2 == LIZARD) or (j1 == LIZARD and j2 == SCISSORS):
        print("Scissors decapitates Lizard \n")
    elif (j1 == LIZARD and j2 == PAPER) or (j1 == PAPER and j2 == LIZARD):
        print("Lizard eats Paper \n")
    elif (j1 == SPOCK and j2 == PAPER) or (j1 == PAPER and j2 == SPOCK):
        print("Paper disproves Spock \n")
    elif (j1 == SPOCK and j2 == ROCK) or (j1 == ROCK and j2 == SPOCK):
        print("Spock vaporizes Rock \n")
    elif (j1 == SCISSORS and j2 == ROCK) or (j1 == ROCK and j2 == SCISSORS):
        print("Rock crushes Scissors \n")

PresentacioJoc()

nom = input("Nom i Cognoms: ")
random.seed(nom)

n_partides_senars = LlegirSenar()

victòries1 = 0
victòries2 = 0
NOMS = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
llistaSheldon = []
llistausuari = []

while victòries1 <=(n_partides_senars/2) and victòries2 <= (n_partides_senars/2):
    num_Sheldon = random.randint(1, 5)
    MenuRPSLS()
    num = int(LlegirNombre(1,5))
    w = JocRPSLS(num, num_Sheldon)
    MissatgeRPSLS(num, num_Sheldon)
    if w == 2:
        victòries1 += 1
        print("Guanya Sheldon Cooper!!!")
    elif w == 1:
        victòries2 += 1
        print("Guanya " + nom + "!!!")
    llistaSheldon.append(NOMS[num_Sheldon - 1])
    llistausuari.append(NOMS[num - 1])
    print("MARCADOR -- Sheldon", victòries1, nom, victòries2, "\n")

if victòries1 > victòries2:
    print("El guanyador és Sheldon")
else:
    print("El guanyador és", nom)
    
print("Sheldon:", llistaSheldon)
print(str(nom)+":", llistausuari)
