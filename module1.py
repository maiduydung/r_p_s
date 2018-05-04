import random
a=""
cpu=None
def r_p_s( ):
    def player_input():
        global a
        player_input.a = input("Enter r - rock, p - paper, s - scissors: ")
        if player_input.a == "r":
            print("You have: rock")
            player_input.a = 1
            return player_input.a
        elif player_input.a == "s":
            print("You have: scissors")
            player_input.a = 2
            return player_input.a
        elif player_input.a == "p":
            print("You have: paper")
            player_input.a = 3
            return player_input.a

    def com_plays():
        global cpu
        com_plays.cpu=random.randint(1,3)
        if com_plays.cpu == 1:
            print("Computer have: rock")
            return cpu
            #r="rock"
        elif com_plays.cpu == 2:
            print("Computer have: scissors")
            return cpu
            #r="scissors"
        elif com_plays.cpu == 3:
            print("Computer have: paper")
            return cpu
            #r="paper"
    

    rock, scissors, paper = 1, 2, 3
    def beat(a,b):
        if(a,b) in ((rock,paper),(paper,scissors),(scissors,rock)):
            return False
        return True
    def game():
        i=0
        win=0
        #print(com_plays.cpu)
        while i<5:
            i=i+1
            print("Round ",i)
            player_input()
            com_plays()
            
            
            if com_plays.cpu!=player_input.a:
                if beat(player_input.a,com_plays.cpu)==True:
                    print("You won")
                    win=win+1
                else:
                    print("You lose")
            else:
                print("Tie")

        print("Your win rate: ",win*100/5)

    game()
    #Im so exhausted now, 2 nights without any sleep to write this program. I know many people can do better than this :( 

r_p_s()