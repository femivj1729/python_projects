import random
print("TIC TAC TOE GAME")
user1=input("Player 1 choose Head or Tail::").upper()
if user1=='HEAD':
    user2='TAIL'
else:
    user2='HEAD'
print('Player 2 choose::',user2)
toss=['head','tail']
cointoss=random.choice(toss).upper()
print(f'Coin toss:: {cointoss}')
select=['X','O','x','o']

if user1==cointoss:
    choice1=input("Enter player 1 choice X/O::").upper()
    while choice1 not in select:
        choice1=input('Enter correct choose X/O:').upper()
    print(f'Player 1 choose {choice1}')
    if choice1=='X':
        choice2='O'
        print('Player 2 choose',choice2)
    else:
        choice2='X'
        print('Player 2 choose',choice2)
    print('Start Game')
    
elif user2==cointoss:
    choice2=input("Enter player2 choice X/O::").upper()
    while choice2 not in select:
        choice2=input('Enter correct choose X/O:').upper()
    print(f'Player 2 choose {choice2}')
    if choice2=='X':
        choice1='O'
        print('Player 1 choose',choice1)
    else: 
        choice1='X'
        print('Player 1 choose',choice1)
    print('Start Game')
    
else:
    print(" wrong choice")


board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def screenboard(board):
    
    print('  '+board[0]+' | '+board[1]+'  | '+board[2])
    print('----|----|----')
    print('  '+board[3]+' | '+board[4]+'  | '+board[5])
    print('----|----|----')
    print('  '+board[6]+' | '+board[7]+'  | '+board[8])

        
check_list=[]

def checkval():
    while True:
        position=int(input('Enter the position between [1-9]::'))
        position-=1
        if 0<= position < 10:
            if position in check_list:
                print('Spot is blocked')
                continue
            check_list.append(position)
            return position
        
def player1():
    
        box=checkval()
        if choice1=='X':
            board[box]='X'
        elif choice1=='O':
            board[box]='O'
        screenboard(board)

def player2():
    
        box=checkval()
        if choice2=='X':
            board[box]='X'
        elif choice2=='O':
            board[box]='O'
        screenboard(board)


def main():
    
    screenboard(board)
    for i in range(1,11):
        if user1==cointoss:
            if i%2!=0:
                print("Player 1's chance")
                player1()
                if choice1=='X':
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 1 win')
                        break
                
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 2 win')
                        break
                else:
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 2 win')
                        break
                    
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 1 win ')
                        break

            elif i%2==0 and i<10:
                print("Player 2's chance")
                player2()
                if choice2=='X':
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 2 win')
                        break
                    
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 1 win ')
                        break
                else:
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 1 win')
                        break
                    
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 2 win ')
                        break
            elif i==10:
                print('XO DRAW!')
                        
        
        elif user2==cointoss:
            if i%2!=0:
                print("Player 2's chance")
                player2()
                if choice2=='X':
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 2 win')
                        break
                    
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 1 win')
                        break
                    
                else:
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 1 win')
                        break
            
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 2 win')
                        break
                    
            elif i%2==0 and i<10:
                print("Player 1's chance")
                player1()
                if choice1=='X':
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 1 win')
                        break
                    
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 2 win')
                        break
                else:
                    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
                        print('Player 2 win')
                        break
                    
                    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
                        print('Player 1 win ')
                        break
            
            elif i==10:
                print('XO DRAW!')
            

main()



             
                





 







