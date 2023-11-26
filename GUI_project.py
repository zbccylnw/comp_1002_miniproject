import tkinter as tk
from tkinter import messagebox
import sys
class Game:
    def __init__(self,LOL):
        self.LOL=LOL
        self.LOL.title('Gomoku Game')
        self.LOL.geometry('800x800')
        self.frame1=tk.Frame(self.LOL)
        self.frame1.pack()

        self.user_name1=tk.StringVar()
        self.user_name2=tk.StringVar()
        self.board_size=tk.StringVar()
        self.x=tk.StringVar()
        self.y=tk.StringVar()
        global time
        time=0

        self.get_user_name()
        
    def packin_frame2(self):
        self.frame2=tk.Frame(self.LOL)
        self.frame2.pack()

    def show_chess(self):
        tk.Label(self.frame2,text=self.user_name1.get()+', you will use o.').grid(row=0)
        tk.Label(self.frame2,text=self.user_name2.get()+', you will use ●.').grid(row=1)
        tk.Button(self.frame2,text='confirm',command=self.delete_frame2).grid(row=2)

    def get_user_name(self):
        tk.Label(self.frame1,text='enter the first user name: ').grid(row=0,column=0)
        tk.Entry(self.frame1,textvariable=self.user_name1).grid(row=0,column=1)
        tk.Label(self.frame1,text='enter the second user name: ').grid(row=1,column=0)
        tk.Entry(self.frame1,textvariable=self.user_name2).grid(row=1,column=1)
        tk.Label(self.frame1,text='choose the size of board, 15 or 19').grid(row=2,column=0)
        tk.Entry(self.frame1,textvariable=self.board_size).grid(row=2,column=1)
        tk.Button(self.frame1,text='confirm',command=self.judge_name_size).grid(row=3,column=1)
    
    def judge_name_size(self):
        global user_name1,user_name2
        user_name1=self.user_name1.get()
        user_name2=self.user_name2.get()
        if self.user_name1.get() != self.user_name2.get() and (self.board_size.get()=='15' or self.board_size.get()=='19'):
            self.frame1.destroy()
            self.packin_frame2()
            self.show_chess()
            global size
            size=self.board_size.get()
            size=int(size)
            global piece
            piece=[["十"for i in range(size)] for j in range(size)]
        elif self.user_name1.get() == self.user_name2.get() and (self.board_size.get()=='15' or self.board_size.get()=='19'):
            messagebox.showerror('Warning','The names of users cannot be the same. Please try again.')
        elif self.user_name1.get() != self.user_name2.get() and (self.board_size.get()!='15' or self.board_size.get()!='19'):
            messagebox.showerror('Warning','The size of board should be 15 or 19. Please try again.')
        else:
            messagebox.showerror('Warning','Wrong enter. Please try again.')

    def delete_frame2(self):
        self.frame2.destroy()
        self.packin_frame4()
        self.packin_frame3()
        self.packin_frame5()

    def packin_frame3(self):
        self.frame3=tk.Frame(self.LOL)
        self.frame3.grid(row=0,column=0)
        self.make_board()

    def empty_frame3(self):
        self.frame3.destroy()
    
    def packin_frame4(self):
        self.frame4=tk.Frame(self.LOL)
        self.frame4.grid(row=1)
        self.play_game()

    def make_board(self):
        tool1=[]
        tool2=[]
        tool3=[]
        count=0
        countelse=size+1
        for m in range(10):
            tool1.append('0')
        for n in range(size-10):
            tool1.append('1')
        for z in range(10):
            tool2.append(str(z))
        for oi in range(size-10):
            tool2.append(str(oi))
        tool3.append(tool1)
        tool3.append(tool2)
        for line1 in piece:
            piece_new='  '.join(line1)
            tk.Label(self.frame3,text=piece_new).grid(row=count)
            count+=1
        for line2 in tool3:
            tool4=' '.join(line2)
            tk.Label(self.frame3,text=tool4,font=('宋体',15)).grid(row=countelse,sticky='W')
            countelse+=1
        self.play_game()

    def packin_frame5(self):
        com=[]
        for pq in range(size):
            if pq<=9:
                com.append('0'+str(pq))
            else:
                com.append(str(pq))
        self.frame5=tk.Frame(self.LOL)
        self.frame5.grid(row=0,column=1,sticky='N')
        tk.Message(self.frame5,text=com,width=30,pady=0,anchor='nw',font=('宋体',17)).grid(row=0,column=0)

    def play_game(self):
        self.judge_time()
        tk.Label(self.frame4,text=f'please enter move with {player}').grid(row=size+3)
        tk.Label(self.frame4,text='x').grid(row=size+4,column=0)
        tk.Entry(self.frame4,textvariable=self.x).grid(row=size+4,column=1)
        tk.Label(self.frame4,text='y').grid(row=size+5,column=0)
        tk.Entry(self.frame4,textvariable=self.y).grid(row=size+5,column=1)
        tk.Button(self.frame4,text='confirm',command=self.judge_x_y).grid(row=size+6)
                    
    def judge_x_y(self):
        global x,y
        x=self.x.get()
        y=self.y.get()
        try:
            x=int(x)
            y=int(y)
        except:
            messagebox.showerror('Warning','What you enter can not be recognised. Please try again.')
        else:
            self.judge_place()

    def judge_place(self):
        global x,y
        x=int(x)
        y=int(y)
        if x<0 or y<0 or x>=size or y>=size:
            messagebox.showerror('Warning','please place on the chessboard')
        elif piece[y][x]!='十':
            messagebox.showerror('Warning','there are already chess piece here')
        else:
            piece[y][x]=player
            self.judge_win()
            self.make_board()
    
    def judge_time(self):
        global player,time,users_name
        if time%2!=0:
            player="o "
            users_name=user_name1
        else:
            player="● "
            users_name=user_name2
        time+=1
        if time==size**2:
            messagebox.showinfo('Sorry','it is a draw. ')
            sys.exit()
        
    def judge_win(self):
        global Win
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
                        messagebox.showinfo('Congratulations',f'{users_name} Win')
                        sys.exit()
                if n<size-4:
                    Win=0
                    for A in range(5):
                        if piece[m][n+A] is player:
                            Win+=1
                        else:
                            break
                    if Win==5:
                        messagebox.showinfo('Congratulations',f'{users_name} Win')
                        sys.exit()
                if n<size-4 and m<size-4:
                    Win=0
                    for A in range(5):
                        if piece[m+A][n+A] is player:
                            Win+=1
                        else:
                            break
                    if Win==5:
                        messagebox.showinfo('Congratulations',f'{users_name} Win')
                        sys.exit()


app = tk.Tk()
game=Game(app)
tk.mainloop()