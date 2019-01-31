from tkinter import Tk,Button,Label
from tkinter import Canvas
from random import randint

root=Tk()
root.title("My first Game")
root.resizable(False,False)

# defining canvas(for shapes and figures)

canvas=Canvas(root,width=600,height=600)
canvas.pack()
#varible for vertical distance travelled by ball
vert=0

#variable for horizontal distance travelled  by bar
hort=5
 # score variable
score=0
#class for creating and moving ball
class Ball:
    def __init__(self,canvas,x1,y1,x2,y2):
        self.x1=x1
        
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.canvas=canvas

        self.ball=canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill="pink",tags='dot1')

        #for moving the ball
    def move_ball(self):
        offset=10
        global vert
        if vert>=510:
            global hort,score,next

                #checking ball fall on the bar
            if(hort-offset<=self.x1 and hort+40+offset>=self.x2):
                score=score+10
                canvas.delete('dot1')

                ball_set()
            else:
                canvas.delete('dot1')
                Bar.delete_bar(self)
                score_board()
            return
        vert+=1
        self.canvas.move(self.ball,0,1)
        self.canvas.after(10,self.move_ball)





class Bar:
    def __init__(self,canvas,x1,y1,x2,y2): 
        self.x1 = x1 
        self.y1 = y1 
        self.x2 = x2 
        self.y2 = y2 
        self.canvas = canvas 
          
        # for creating bar using create_rectangle 
        self.rod=canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,  
                                                    fill="green",tags='dot2')
        
        #method for moving bar
    def move_bar(self,num):
        global hort

            #checking button for forward and backward
        if(num==1):
            self.canvas.move(self.rod,20,0)
            hort=hort+20
        else:
            self.canvas.move(self.rod,-20,0)
            hort=hort-20
    def delete_bar(self):
        canvas.delete('dot2')

def ball_set():
    global vert
    vert=0
    value=randint(0,570)
    ball1=Ball(canvas,value,20,value+30,50)
    ball1.move_ball()

def score_board():
    root2=Tk()
    root2.title("Catch the ball game")
    root2.resizable(False, False)
    canvas2=Canvas(root2,width=300,height=300)
    canvas2.pack()
    w=Label(canvas2, text="\nOOPS......You Loose \n\n Your Final Score="+str(score)+"\n\n")
    w.pack()
    button3=Button(canvas2,text="Play Again",bg="yellow",command=lambda:play_again(root2))
    button3.pack()
    
    button4=Button(canvas2,text="Exit",bg="yellow",command=lambda:exit_handler(root2))
    button4.pack()

def play_again(root2):
    root2.destroy()
    main()
def exit_handler(root2):
    root2.destroy()
    root.destroy()
def main():
    global score,hort
    score=0
    hort=0

    bar1=Bar(canvas,5,560,45,575)

        #define text color of buttons and other features

    button=Button(canvas,text="==>",bg="yellow",command=lambda:bar1.move_bar(1))
    button.place(x=300,y=580)
    button2=Button(canvas,text="<==",bg="yellow",command=lambda:bar1.move_bar(0))
    button2.place(x=260,y=580)

    ball_set()
    root.mainloop()

if(__name__=="__main__"):
    main()
    

    
            
            
                
                        
                    

        
 
