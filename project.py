from tkinter import *
import PIL.Image
from PIL import ImageTk
import numpy as np
from scipy import optimize
from scipy import stats
from sklearn import cluster

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

penid=[]           # for smoothing the curves
xlist=[]
ylist=[]

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

        # dictates the images on the buttons
        var=shape+".png"                    
        self.image=PIL.Image.open(var)
        self.photo=ImageTk.PhotoImage(self.image)

        # calling the button object of tkinter
        self.button=Button(root, image=self.photo, command=lambda: draw(self))
        self.button.image=self.image           # keeping an instance of the image to avoid python grabage collector
        self.button.place(relx=relx, rely=rely, relheight=0.07, relwidth=0.07)

# cleans the entire canvas
def clean():
    canvas.delete("all")
    return

def draw(a):
    global prev,polyvar

    # changing the active status of previosly selected button
    # and raising the previosly selected button
    if prev!="null":
        prev.atv=0
        prev.button.config(relief='raised')

    # activating the selected button
    a.atv=1
    a.button.config(relief='sunken')

    if prev==poly:             # to stop making a polynomial
        polyvar=0

    # changing the previous button to the current button
    prev=a
    return

# storing the coordinates of first click
def func1(event):
    global x1,y1,id1,id2,polyvar,initx,inity,polyx,polyy

    # storing the coordinates of first click
    x1=event.x
    y1=event.y

    # creating ids of the shape to be drawn
    if line.atv==1 or curve.atv==1:
        xlist.append(x1)
        ylist.append(y1)

    elif erase.atv==1:
        id1=canvas.create_line(x1,y1,x1,y1,width=15,fill="white")

    elif star.atv==1:
    	id1=canvas.create_line(x1,y1,x1,y1,x1,y1)
    	id2=canvas.create_line(x1,y1,x1,y1,x1,y1)

    elif poly.atv==1:
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

    else:
        id1=canvas.create_line(x1,y1,x1,y1)               # creating a dummy id that is used to draw shapes in func2

    return

# storing the coordinates of drag and drawing
def func2(event):
    global id1,id2,x1,y1,penid
    rect1=[]
    # storing the coordinates of drag
    x2=event.x
    y2=event.y

    # deleting the old shape and drawing new one as the user drags the mouse
    if line.atv==1:
        id1=canvas.create_line(x1,y1,x2,y2)
        penid.append(id1)
        xlist.append(x2)
        ylist.append(y2)
        x1=x2
        y1=y2

    elif oval.atv==1:
        canvas.delete(id1)
        id1=canvas.create_oval(x1,y1,x2,y2)

    elif rect.atv==1 or tri.atv==1:
        id1=canvas.create_line(x1,y1,x2,y2)
        penid.append(id1)
        xlist.append(x2)
        ylist.append(y2)
        x1=x2
        y1=y2

    elif pen.atv==1:
        id1=canvas.create_line(x1,y1,x2,y2)
        x1=x2
        y1=y2

    elif curve.atv==1:
        id1=canvas.create_line(x1,y1,x2,y2)
        penid.append(id1)
        xlist.append(x2)
        ylist.append(y2)
        x1=x2
        y1=y2

    elif erase.atv==1:
        id1=canvas.create_line(x1,y1,x2,y2,width=15,fill="white")
        x1=x2
        y1=y2

    elif rho.atv==1:
        canvas.delete(id1)
        id1=canvas.create_line((x1+x2)/2,y1,x2,(y1+y2)/2,(x1+x2)/2,y2,x1,(y1+y2)/2,(x1+x2)/2,y1)

    elif right.atv==1:
        canvas.delete(id1)
        id1=canvas.create_line(x1,y1,x2,y2,x1,y2,x1,y1)

    # elif tri.atv==1:
    #     canvas.delete(id1)
    #     id1=canvas.create_line((x1+x2)/2,y1,x2,y2,x1,y2,(x1+x2)/2,y1)

    elif pent.atv==1:
    	canvas.delete(id1)

    	id1=canvas.create_line((x1+x2)/2,y1,x1,(y1+y2)/2-0.3249*(y2-y1)/2,0.5*(x1-x2)/1.37638+(x1+x2)/2,y2,0.5*(x2-x1)/1.37638+(x1+x2)/2,y2,x2,(y1+y2)/2-0.3249*(y2-y1)/2,(x1+x2)/2,y1)

    elif hex.atv==1:
    	canvas.delete(id1)

    	id1=canvas.create_line((x1+x2)/2,y1,x1,y1+(y2-y1)*0.2929,x1,y2-(y2-y1)*0.2929,(x1+x2)/2,y2,x2,y2-(y2-y1)*0.2929,x2,y1+(y2-y1)*0.2929,(x1+x2)/2,y1)

    elif star.atv==1:
    	canvas.delete(id1)
    	canvas.delete(id2)

    	a=(x1+x2)/2
    	b=0.25*(y2-y1)

    	id1=canvas.create_line(a,y1,x1,y2-b,x2,y2-b,a,y1)
    	id2=canvas.create_line(a,y2,x1,y1+b,x2,y1+b,a,y2)

    return

def shape(x,n):

    x2=[]
    for i in range(0,n):
        x2+=[[]]

    split=[]
    kmeans=cluster.KMeans(n).fit(x)
    arr=kmeans.labels_
    x1=kmeans.cluster_centers_

    order=[]
    true=False
    for i in arr:
        for j in order:
            if i==j:
                true=True
        if true==True:
            true=False
        else:
            order+=[i]

    cut=0
    pre=kmeans.predict([x[0]])
    prev=arr[1]
    for i in range(1,len(arr)):
        if arr[i]!=prev:
            cut=i
            break
        prev=arr[i]
    beg=[]
    for i in range(0,len(arr)):
        if arr[i]==pre[0]:
            if i<=cut:
                x2[arr[i]]+=[x[i]]
            else:
                beg+=[x[i]]
        else:
            x2[arr[i]]+=[x[i]]
    x2[pre[0]]=beg+x2[pre[0]]
    
    cen=[]
    for i in order:
        cen+=[[x2[i][len(x2[i])//2][0],x2[i][len(x2[i])//2][1]]]

    return(cen)

def func3(event):

    global penid, xlist, ylist, rect1

    for i in range(0,len(penid)):                     # deleting the curves with error
        canvas.delete(penid[i])

    penid.clear()
    xarr = np.asarray(xlist)
    yarr = np.asarray(ylist)

    if line.atv==1:                      # linear regression to correct the drawn line

        opt1 = stats.linregress(xarr, yarr)
        opt2 = stats.linregress(yarr, xarr)

        if opt1[4]<opt2[4]:
            yarr=opt1[0]*xarr+opt1[1]

        else:
            xarr=opt2[0]*yarr+opt2[1]

        for i in range(1,len(xarr)):       # creating the curves with fitted data
            canvas.create_line(xarr[i-1],yarr[i-1],xarr[i],yarr[i])
        

    if curve.atv == 1:                 # polynomial regression to smooth the curve

        def func(x, a, b, c, d,e,f):
            return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f

        popt, pcov= optimize.curve_fit(func, xarr, yarr)
        print(len(xarr))
        
        yarr=func(xarr,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5])

    
        for i in range(1,len(xarr)):       # creating the curves with fitted data
            canvas.create_line(xarr[i-1],yarr[i-1],xarr[i],yarr[i])

    x=[]
    for i in range(0,len(xlist)):
        x+=[[xlist[i],ylist[i]]]
    
    if rect.atv==1:
        cen=shape(x,4)
        for i in range(1,4):
            canvas.create_line(cen[i-1][0],cen[i-1][1],cen[i][0],cen[i][1],fill="black")

        canvas.create_line(cen[0][0],cen[0][1],cen[-1][0],cen[-1][1],fill="black")

    if tri.atv==1:
        cen=shape(x,3)
        for i in range(1,3):
            canvas.create_line(cen[i-1][0],cen[i-1][1],cen[i][0],cen[i][1],fill="black")

        canvas.create_line(cen[0][0],cen[0][1],cen[-1][0],cen[-1][1],fill="black")

    xlist.clear()
    ylist.clear()

    return

# binding the mouse clicking and dragging events
canvas.bind("<ButtonPress-1>", func1)
canvas.bind("<B1-Motion>", func2)
canvas.bind("<ButtonRelease-1>", func3)

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
curve=button('curve',0.07,0.42)

# clear canvas button
imbroom=PIL.Image.open("broom.png")
phbroom=ImageTk.PhotoImage(imbroom)

broom=Button(root, image=phbroom, command=clean)
broom.image=phbroom
broom.place(relx=0.07, rely=0.07, relheight=0.07, relwidth=0.07)

root.mainloop()
