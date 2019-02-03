from tkinter import *
import PIL.Image
from PIL import ImageTk

# calling all Tk objects
root=Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title('Py Draw')

# variables governing the making of a polygon
initx=0
inity=0
polyvar=0
polyx=0
polyy=0

prev="null"        # tells which shape was active earlier

# instance of frame object
frame= Frame(root,height="540", width="980")
frame.pack()

# instance of canvas object
canvas=Canvas(root, bg="white")
canvas.place(relheight=1.0, relwidth=.86, relx=.14, rely=0)

# class which dictates the position and working of a button
class button:
    def __init__(self,shape, relx, rely):
        self.atv=0                         # tells us if this shape is currently active
        self.command=shape                 # command which activates the shape to be drawn
        self.relx=relx                     # position of the button
        self.rely=rely

        # dictates the images on the buttons
        var=shape+".png"                    
        self.image=PIL.Image.open(var)
        self.photo=ImageTk.PhotoImage(self.image)

        # calling the button object of tkinter
        self.button=Button(root, image=self.photo, command=lambda: draw(self.command))
        self.button.image=self.image
        self.button.place(relx=self.relx, rely=self.rely, relheight=0.07, relwidth=0.07)

# cleans the entire canvas
def clean():
    canvas.delete("all")
    return

def draw(a):
    global prev,polyvar

    # changing the active status of previosly selected button
    # and raising the previosly selected button
    if prev!="null":
        if prev=="line":
            line.atv=0
            line.button.config(relief='raised')
        elif prev=="oval":
            oval.atv=0
            oval.button.config(relief='raised')
        elif prev=="rect":
            rect.atv=0
            rect.button.config(relief='raised')
        elif prev=="pen":
            pen.atv=0
            pen.button.config(relief='raised')
        elif prev=="erase":
            erase.atv=0
            erase.button.config(relief='raised')
            canvas.config(cursor="arrow")
        elif prev=="broom":
            broom.atv=0
        elif prev=="rho":
            rho.atv=0
            rho.button.config(relief='raised')
        elif prev=="right":
            right.atv=0
            right.button.config(relief='raised')
        elif prev=="tri":
            tri.atv=0
            tri.button.config(relief='raised')
        elif prev=="pent":
            pent.atv=0
            pent.button.config(relief='raised')
        elif prev=="hex":
            hex.atv=0
            hex.button.config(relief='raised')
        elif prev=="star":
            star.atv=0
            star.button.config(relief='raised')
        elif prev=="poly":
            poly.atv=0
            polyvar=0
            poly.button.config(relief='raised')

    # changing the active status according to button click
    # and making the selected button pressed as long as it is in use
    if a=="line":
        line.atv=1
        line.button.config(relief='sunken')
    elif a=="oval":
        oval.atv=1
        oval.button.config(relief='sunken')
    elif a=="rect":
        rect.atv=1
        rect.button.config(relief='sunken')
    elif a=="pen":
        pen.atv=1
        pen.button.config(relief='sunken')
    elif a=="broom":
        broom.atv=1
    elif a=="erase":
        erase.atv=1
        erase.button.config(relief='sunken')
        canvas.config(cursor="circle")
    elif a=="rho":
        rho.atv=1
        rho.button.config(relief='sunken')
    elif a=="right":
        right.atv=1
        right.button.config(relief='sunken')
    elif a=="tri":
        tri.atv=1
        tri.button.config(relief='sunken')
    elif a=="pent":
        pent.atv=1
        pent.button.config(relief='sunken')
    elif a=="hex":
        hex.atv=1
        hex.button.config(relief='sunken')
    elif a=="star":
        star.atv=1
        star.button.config(relief='sunken')
    elif a=="poly":
        poly.atv=1
        poly.button.config(relief='sunken')

    # changing the previous button to the current button
    prev=a
    return

# storing the coordinates of first click
def func1(event):
    global x1,y1,id1,id2,id3,id4,polyvar,initx,inity,polyx,polyy

    # storing the coordinates of first click
    x1=event.x
    y1=event.y

    # creating ids of the shape to be drawn
    if line.atv==1:
        id1=canvas.create_line(x1,y1,x1,y1)

    if oval.atv==1:
        id1=canvas.create_oval(x1,y1,x1,y1)

    if rect.atv==1:
        id1=canvas.create_rectangle(x1,y1,x1,y1)

    if pen.atv==1:
        id1=canvas.create_line(x1,y1,x1,y1)

    if erase.atv==1:
        id1=canvas.create_line(x1,y1,x1,y1,width=15,fill="white")

    if rho.atv==1:
        id1=canvas.create_line(x1,y1,x1,y1)
        id2=canvas.create_line(x1,y1,x1,y1)
        id3=canvas.create_line(x1,y1,x1,y1)
        id4=canvas.create_line(x1,y1,x1,y1)

    if right.atv==1:
        id1=canvas.create_line(x1,y1,x1,y1)
        id2=canvas.create_line(x1,y1,x1,y1)
        id3=canvas.create_line(x1,y1,x1,y1)

    if tri.atv==1:
        id1=canvas.create_line(x1,y1,x1,y1)
        id2=canvas.create_line(x1,y1,x1,y1)
        id3=canvas.create_line(x1,y1,x1,y1)

    if pent.atv==1:
    	id1=canvas.create_line(x1,y1,x1,y1,x1,y1,x1,y1,x1,y1,x1,y1)

    if hex.atv==1:
    	id1=canvas.create_line(x1,y1,x1,y1,x1,y1,x1,y1,x1,y1,x1,y1,x1,y1)

    if star.atv==1:
    	id1=canvas.create_line(x1,y1,x1,y1,x1,y1)
    	id2=canvas.create_line(x1,y1,x1,y1,x1,y1)

    if poly.atv==1:
    	if polyvar==0:
    		polyvar=1
    		polyx=x1
    		polyy=y1
    		initx=x1
    		inity=y1
    	elif (((initx-x1)**2)+((inity-y1)**2))<50:
    		id1=canvas.create_line(polyx,polyy,initx,inity)
    		polyvar=0
    	elif polyvar==1:
    		id1=canvas.create_line(polyx,polyy,x1,y1)
    		polyx=x1
    		polyy=y1

    return

# storing the coordinates of drag and drawing
def func2(event):
    global id1,id2,id3,id4,x1,y1

    # storing the coordinates of drag
    x2=event.x
    y2=event.y

    # deleting the old shape and drawing new one as the user drags the mouse
    if line.atv==1:
        canvas.coords(id1,x1,y1,x2,y2)

    if oval.atv==1:
        canvas.delete(id1)
        id1=canvas.create_oval(x1,y1,x2,y2)

    if rect.atv==1:
        canvas.delete(id1)
        id1=canvas.create_rectangle(x1,y1,x2,y2)

    if pen.atv==1:
        id1=canvas.create_line(x1,y1,x2,y2)
        x1=x2
        y1=y2

    if erase.atv==1:
        id1=canvas.create_line(x1,y1,x2,y2,width=15,fill="white")
        x1=x2
        y1=y2

    if rho.atv==1:
        canvas.delete(id1)
        id1=canvas.create_line((x1+x2)/2,y1,x2,(y1+y2)/2)
        canvas.delete(id2)
        id2=canvas.create_line(x2,(y1+y2)/2,(x1+x2)/2,y2)
        canvas.delete(id3)
        id3=canvas.create_line((x1+x2)/2,y2,x1,(y1+y2)/2)
        canvas.delete(id4)
        id4=canvas.create_line(x1,(y1+y2)/2,(x1+x2)/2,y1)

    if right.atv==1:
        canvas.delete(id1)
        id1=canvas.create_line(x1,y1,x2,y2)
        canvas.delete(id2)
        id2=canvas.create_line(x1,y1,x1,y2)
        canvas.delete(id3)
        id3=canvas.create_line(x1,y2,x2,y2)

    if tri.atv==1:
        canvas.delete(id1)
        id1=canvas.create_line((x1+x2)/2,y1,x2,y2)
        canvas.delete(id2)
        id2=canvas.create_line((x1+x2)/2,y1,x1,y2)
        canvas.delete(id3)
        id3=canvas.create_line(x1,y2,x2,y2)

    if pent.atv==1:
    	canvas.delete(id1)

    	a1=(x1+x2)/2
    	b1=y1
    	a2=x1
    	b2=(y1+y2)/2-0.3249*(y2-y1)/2
    	a3=0.5*(x1-x2)/1.37638+(x1+x2)/2
    	b3=y2
    	a4=0.5*(x2-x1)/1.37638+(x1+x2)/2
    	b4=y2
    	a5=x2
    	b5=b2

    	id1=canvas.create_line(a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a1,b1)

    if hex.atv==1:
    	canvas.delete(id1)

    	a1=(x1+x2)/2
    	b1=y1
    	a2=x1
    	b2=y1+(y2-y1)*0.2929
    	a3=x1
    	b3=y2-(y2-y1)*0.2929
    	a4=a1
    	b4=y2
    	a5=x2
    	b5=b3
    	a6=x2
    	b6=b2

    	id1=canvas.create_line(a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6,a1,b1)

    if star.atv==1:
    	canvas.delete(id1)
    	canvas.delete(id2)

    	a=(x1+x2)/2
    	b=0.25*(y2-y1)

    	id1=canvas.create_line(a,y1,x1,y2-b,x2,y2-b,a,y1)
    	id2=canvas.create_line(a,y2,x1,y1+b,x2,y1+b,a,y2)

    return

# binding the mouse clicking and dragging events
canvas.bind("<ButtonPress-1>", func1)
canvas.bind("<B1-Motion>", func2)

# objects of button of corresponding shape
line=button('line',0,0)
oval=button('oval',0.07,0)
rect=button('rect',0,0.07)
pen=button('pen',0,0.14)
erase=button('erase',0.07,0.14)
rho=button('rho',0,0.21)
right=button('right',0.07,0.21)
tri=button('tri',0,0.28)
pent=button('pent',0.07,0.28)
hex=button('hex',0,0.35)
star=button('star',0.07,0.35)
poly=button('poly',0,0.42)

# clear canvas button
imbroom=PIL.Image.open("broom.png")
phbroom=ImageTk.PhotoImage(imbroom)

broom=Button(root, image=phbroom, command=clean)
broom.image=phbroom
broom.place(relx=0.07, rely=0.07, relheight=0.07, relwidth=0.07)

root.mainloop()
