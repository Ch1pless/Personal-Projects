# Made by Ch1pless

print("\nRock Paper Scissors: The first player to win three times will win the game. \
\nInput Rock, Paper, or Scissors to play your turn\n")


def Turn(player) :
	while True :
		pl = input("Player " + str(player) + ": ").lower()
		if pl not in ["rock", "paper", "scissors"] :
			print("Invalid Turn. Try Again. ")
			continue
		else :
			break
	return pl

def Compare(winner,loser) :
	if ((winner == "rock" and loser == "scissors") or
			(winner == "scissors" and loser == "paper") or
			(winner == "paper" and loser == "rock")) :
		return True
	else :
		return False

pl1score = 0
pl2score = 0

while pl1score < 3 and pl2score < 3 :
	print("Player 1 Score: " + str(pl1score) + "	Player 2 Score: " + str(pl2score) + '\n')
	pl1 = Turn(1)
	pl2 = Turn(2)
	if Compare(pl1,pl2) :
		print("Player 1 won that round.")
		pl1score += 1
	elif Compare(pl2,pl1) :
		print("Player 2 won that round.")
		pl2score += 1
	else :
		print("That round was a tie.")


if pl1score == 3 :
	print("Player 1 Won!")
else :
	print("Player 2 Won!")

input("\nPress any key to exit.\n" + '*'*20)
