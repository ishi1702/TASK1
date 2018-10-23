import random

print("WELCOME TO THE GAME OF ROCK , PAPER AND SCISSORS..............")
print("THE RULES ARE AS FOLLOWS::")
print("ROCK BLUNTS SCISSORS,PAPER COVERS ROCKS,SCISSORS CUTS PAPER")
print("WOULD YOU LIKE TO PLAY rock , paper , scissor?(y/n)")
reply=input()

while(reply=="y"):
	player_score = 0
	computer_score = 0
	print("HOW MANY TIMES YOU WANT TO PLAY")
	n = int(input())
	for i in range (0,n): 
		player_choice = input("ENTER YOUR CHOICE OF rock,paper or scissor    ")
		print ("YOUR CHOICE = ", player_choice)
		computer_choice = random.randint(1,3)
	
		if (computer_choice == 1):
			computer = "rock"
		elif (computer_choice == 2):
			computer = "paper"
		elif(computer_choice == 3):
			computer = "scissors"
	
		print("COMPUTER CHOICE = ",computer)
		
		
		if(player_choice == computer):
			print("tie")
			print("PLAYER SCORE = ",player_score)
			print("COMPUTER SCORE = ",computer_score)
		elif(player_choice == "rock"):
			if (computer == "paper"):
				print("COMPUTER WINS")
				computer_score +=1
				
			else:
				print("YOU WIN")
				player_score +=1
			print("PLAYER SCORE = ",player_score)
			print("COMPUTER SCORE = ",computer_score)
		elif(player_choice == "paper"):
			if (computer == "rock"):
				print("YOU WIN")
				player_score +=1
				
			else:
				print("COMPUTER WINS")
				computer_score +=1
			print("PLAYER SCORE = ",player_score)
			print("COMPUTER SCORE = ",computer_score)
		elif(player_choice == "scissor"):
			if (computer == "rock"):
				print("COMPUTER WINS")
				computer_score +=1
				
			else:
				print("YOU WIN")
				player_score +=1
				print("PLAYER SCORE = ",player_score)
				print("COMPUTER SCORE = ",computer_score)
	if (player_score>computer_score):
		print("   ########################           FINALLY YOU WON             #####################            ")
	elif(player_score==computer_score):
		print("   ######################      THE MATCH IS FINALLY TIE         #####################         ")
	else:
		print("  ######################            THE COMPUTER WON            #######################            ")
	print("WOULD YOU LIKE TO PLAY rock, paper, scissors? y/n")
	reply=input()
	if(reply=="n"):
		print("******************************     THANKS FOR PLAYING        *****************************")
		
        
           
	
