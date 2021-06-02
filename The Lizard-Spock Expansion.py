import random

results = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"),
           ("rock", "lizard"), ("lizard", "spock"), ("spock", "scissors"), 
           ("scissors", "lizard"), ("lizard", "paper"), ("paper", "spock" ), ("spock", "rock")]

moves = [result[1] for result in results]
sheldon_score, AI_score = (0,0)

sheldon = input("Enter your choice or quit:").lower()

while sheldon != "quit":
    AI = random.choice(moves)
    if sheldon == AI:
        print(" It's a tie, you are not the smartest person Sheldon")
    elif (sheldon, AI) in results:
        print("Yeah you win")
        sheldon_score +=1
    elif (AI, sheldon) in results:
        print(" Go home buddy!!!")
        AI_score += 1
    else:
        print("Give a valid input sheldon")
    sheldon = input("Enter your choice or quit:").lower()

print("Moment of truth")
print("----------------------------------------")
if (sheldon_score > AI_score):
    print("Buzingaaaa !!!!")
print("Sheldon{}, AI {}".format(sheldon_score, AI_score))

