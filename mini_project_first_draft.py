import sys
users_name1=input('enter the first user name')
users_name2=input('enter the second user name')
while users_name1==users_name2:
    print('the user can not use the same name. please try again')
    users_name1=input('enter the first user name')
    users_name2=input('enter the second user name')
while True:
    size=input("choose your board size: 15 or 19: ")
    if size=='15' or size=='19':
        size=int(size)
        break
    else:
        print('wrong input. please try again')
piece=[["+"for i in range(size)] for j in range(size)]
tool1=[]
tool2=[]
for x in range(10):
    tool1.append('0')
for y in range(size-10):
    tool1.append('1')
for z in range(10):
    tool2.append(str(z))
for oi in range(size-10):
    tool2.append(str(oi))
piece.append(tool1)
piece.append(tool2)
for pq in range(size):
    piece[pq].append(str(pq))
for row in piece:
    print(' '.join(row))
time=0
while 2==2:
    if time%2==0:
        player="⚪"
        users_name=users_name1
    else:
        player="⚫"
        users_name=users_name2
    while 3==3:
        c=0
        while c!=1:
            try:
                a,b =input(f"Player {users_name}, you will use {player}, enter your move in form 'x y': ").split()
                a=int(a)
                b=int(b)
            except:
                c=0
                print('What you enter can not be recognised. Please try again.')
            else:
                c=1
        a=int(a)
        b=int(b)
        if a<0 or b<0 or a>=size or b>=size:
            print("please place on the chessboard")
        else:
            if piece[b][a] == "+" :
                break
            else:
                print("there are already chess piece here")
    piece[b][a]=player
    for row in piece:
        print(' '.join(row))
    for m in range(size):
        for n in range(size):
            if m<size-4:
                Win=0
                for A in range(5):
                    if piece[m+A][n] is player:
                        Win+=1
                    else:
                        break
                if Win==5:
                    print(f"{users_name} Win!")
                    sys.exit()
            if n<size-4:
                Win=0
                for A in range(5):
                    if piece[m][n+A] is player:
                        Win+=1
                    else:
                        break
                if Win==5:
                    print(f"{users_name} Win!") 
                    sys.exit()
            if n<size-4 and m<size-4:
                Win=0
                for A in range(5):
                    if piece[m+A][n+A] is player:
                        Win+=1
                    else:
                        break
                if Win==5:
                    print(f"{users_name} Win!")         
                    sys.exit()
    time+=1
    if time==size**2:
        print('the game is draw.')
        sys.exit()