import sys
while 1==1:
    size=int(input("choose your board size:  15 or 19: "))
    if size==15 or size==19:
        break
    else:
        print("size wrong,try again")
piece=[["+"for i in range(size)] for j in range(size)]
#piece=["十"*size for j in range(size)]
for row in piece:
    print(' '.join(row))
    #print(row)
time=0
while 2==2:
    if time%2==0:
        player="X"
    else:
        player="O"
    while 3==3:
        a,b =input(f"Player {player}, enter your move in form 'x y': ").split()
        a=int(a)
        b=int(b)
        if a<0 or b<0 or a>=size or b>=size:
            print("please place on the chessboard")
        else:
            if piece[a][b] is "+" :
                break
            else:
                print("there are already chess piece here")
    piece[a][b]=player
    for row in piece:
        print(' '.join(row))
    for m in range(size):
        for n in range(size):
            if m<11:
                Win=0
                for A in range(5):
                    if piece[m+A][n] is player:
                        Win+=1
                    else:
                        break
                if Win==5:
                    print("You Win!")
                    sys.exit()
            if n<11:
                Win=0
                for A in range(5):
                    if piece[m][n+A] is player:
                        Win+=1
                    else:
                        break
                if Win==5:
                    print("You Win!") 
                    sys.exit()
            if n<11 and m<11:
                Win=0
                for A in range(5):
                    if piece[m+A][n+A] is player:
                        Win+=1
                    else:
                        break
                if Win==5:
                    print("You Win!")         
                    sys.exit()
    time+=1