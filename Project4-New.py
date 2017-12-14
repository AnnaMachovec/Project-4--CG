
# coding: utf-8

# In[1]:

arr = []
def basic_alg(x0, y0, x1, y1):
    arr = []
    start = 0
    finish = 0
    dx = (x1-x0)
    dy = (y1-y0)
    y= y0
    x = x0
    #calculate slope
    if dx == 0:
        if y0<y1:
            start = y0
            finish = y1
        if y1<y0:
            start = y1
            finish = y0
        for y in range(start,finish+1):
            x = x
            coord = (x,y)
            arr.append(coord)
            y = y +1
    else:
        m = float(float(dy)/float(dx))
        b = y0-m*x0
   
    #swapping method in case its a negative slope
        if(m < 0):
            tx, ty = x0, y0
            x0, y0 = x1, y1
            x1, y1 = tx, ty
    #y intercept calculation
        b = y0-m*x0
        y = y0
        x = x0
        #preconditions for for loop
        if x0<x1:
            start = x0
            finish = x1
        if x1<x0:
            start = x1
            finish = x0
        #for loop that starts at x0 and ends at x1
        for x in range(start,finish+1):
            y = m * x + b
            coord = (x,y)
            # prints and appends the coordinates
            arr.append(coord)
            x = x+1
    
    return arr


# In[2]:

def call(x1,y1,z1,x2,y2,z2):
    l = a3d.Line3D((x1,x2),(y1,y2),(z1,z2), c = 'k', ls = '--')
    ax.add_line(l)
                   
    
    


# In[3]:

#Basic Translate

def Translation3d(Tx,Ty,Tz):
    t1 = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[Tx,Ty,Tz,1]])
    return t1


# In[4]:

#Scale
import numpy as np
def Scale3d(Sx,Sy,Sz):
    matrixscale = np.matrix([[Sx,0, 0, 0], [0, Sy, 0,0], [0, 0, Sz,0],[0,0,0,1]])
    return matrixscale


# In[5]:

def Rotate3Dx(angle):
    matrix = np.matrix([[1,0,0,0],[0,math.cos(angle),-(math.sin(angle)),0],[0,math.sin(angle),math.cos(angle),0],[0,0,0,1]])
    return matrix
    
    


# In[6]:

def Rotate3Dy(angle):
    matrix = np.matrix([[math.cos(angle),0,math.sin(angle),0],[0,1,0,0],[-(math.sin(angle)),0,math.cos(angle),0],[0,0,0,1]])
    return matrix


# In[7]:

def Rotate3Dz(angle):
    matrix = np.matrix([[math.cos(angle),-(math.sin(angle)),0,0],[math.sin(angle),math.cos(angle),0,0],[0,0,1,0],[0,0,0,1]])
    return matrix


# In[8]:

#rotate
import math
def PP(x,y,z):
    #constant
    t1 = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-x,-y,-z,1]])
    
    t2 = np.matrix([[1,0, 0, 0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]])
    
    
    #yaxis stuff
    costheta = (y)/(math.sqrt(math.pow(x,2)+math.pow(y,2)))
    
    
    sintheta = (x)/(math.sqrt(math.pow(x,2)+(math.pow(y,2))))
    t3 =  np.matrix([[-(costheta),0, sintheta, 0], [0,1,0,0], [-(sintheta),0, -(costheta),0],[0,0,0,1]])
    
    
    #xaxis
    
    cosalpha = (math.sqrt(math.pow(x,2)+math.pow(y,2)))/(math.sqrt(math.pow(x,2)+(math.pow(y,2))+(math.pow(z,2))))
    
    sinalpha = (z)/(math.sqrt(math.pow(x,2)+(math.pow(y,2))+(math.pow(z,2))))
    
    t4 = np.matrix([[1,0, 0, 0], [0,cosalpha, sinalpha,0], [0, -sinalpha,cosalpha,0],[0,0,0,1]])
    
    t5 = np.matrix([[1,0,0,0],[0,1,0,0],[0, 0, -1,0],[0,0,0,1]])
    
    
    temp = np.matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    
    temp = t1 * t2 * t3 * t4 * t5
    return temp


# In[9]:

#Input Lines for 3d
def InputLines(datalines,num):
    with open(datalines,'r') as myfile:
        data = []
        for line in myfile:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                data.append(line)
            newdata = np.array(data)
        
    return newdata
   


# In[10]:

##Display Lines
def DisplayLines(datalines,num): 
    
    for x in range(len(datalines)):
        x0 = datalines[x][0]
        y0 = datalines[x][1]
        z0 = datalines[x][2]
        x1 = datalines[x][3]
        y1 = datalines[x][4]
        z1 = datalines[x][5]
        call(x0,y0,z0,x1,y1,z1)
   


# In[11]:

def toC(matrix,N,datalines):
    numlines = sum(1 for line in open('input.txt'))
    data = []
    for x in range(numlines):
        xfront = datalines[x][0]
        yfront = datalines[x][1]
        zfront = datalines[x][2]
        xback = datalines[x][3]
        yback = datalines[x][4]
        zback = datalines[x][5]
        xyzwfront = np.matrix([xfront, yfront,zfront, 1])
        xyzwback = np.matrix([xback,yback,zback,1])
        xyzefront = xyzwfront * matrix
        xyzeback = xyzwback * matrix
        xyzefront = xyzefront * N
        xyzeback = xyzeback * N
        data.append(int(round(xyzefront.item(0))))
        data.append(int(round(xyzefront.item(1))))
        data.append(int(round(xyzefront.item(2))))
        data.append(int(round(xyzeback.item(0))))
        data.append(int(round(xyzeback.item(1))))
        data.append(int(round(xyzeback.item(2))))
      
    
    return data    


# In[12]:

def changeworld(matrix,N,datalines):
    numlines = sum(1 for line in open('input.txt'))
    data = []
    for x in range(numlines):
        xfront = datalines[x][0]
        yfront = datalines[x][1]
        zfront = datalines[x][2]
        xback = datalines[x][3]
        yback = datalines[x][4]
        zback = datalines[x][5]
        xyzwfront = np.matrix([xfront, yfront,zfront, 1])
        xyzwback = np.matrix([xback,yback,zback,1])
        xyzefront = xyzwfront * matrix
        xyzeback = xyzwback * matrix
        data.append(int(round(xyzefront.item(0))))
        data.append(int(round(xyzefront.item(1))))
        data.append(int(round(xyzefront.item(2))))
        data.append(int(round(xyzeback.item(0))))
        data.append(int(round(xyzeback.item(1))))
        data.append(int(round(xyzeback.item(2))))
      
    
    return data 


# In[13]:

def toXsYs(cdata,Vsx,Vsy,Vcx,Vcy):
    numlines = sum(1 for line in open('output.txt'))
    data = []
    count = 0
    for x in range(numlines):
        xfront = cdata[x][0]
        yfront = cdata[x][1]
        zfront = cdata[x][2]
        xback = cdata[x][3]
        yback = cdata[x][4]
        zback = cdata[x][5]
        Xs1 = int(round((float(xfront)/zfront)*Vsx+Vcx))
        
        ys = int(round((float(yfront)/zfront)*Vsx+Vsy))
       
        data.append(Xs1)
        data.append(ys)
        Xs2 = int(round((float(xback)/zback)*Vsx+Vcx))
        Ys2 = int(round((float(yback)/zback)*Vsy+Vcy))
       
        data.append(Xs2)
        data.append(Ys2)
        
        call2(Xs1,ys,Xs2,Ys2)
        
        
    return data    
        


# In[14]:

##Display Lines
def DisplayLines2(datalines,num): 
    
    for x in range(len(datalines)):
        x0 = datalines[x][0]
        y0 = datalines[x][1]
        x1 = datalines[x][2]
        y1 = datalines[x][3]
     
        call2(x0,y0,x1,y1)


# In[15]:

def call2(x1,y1,x2,y2):
    arr = basic_alg(x1,y1,x2,y2)
    axes = plt.gca()
    axes.set_xlim([-200,2000])
    axes.set_ylim([-200,2000])
    ex, why = zip(*arr)
    plt.plot(ex,why)
    arr = []
 


# In[16]:

#Output lines
def OutputLines(datalines,num):
    temparr = []
    outputfile = open("output.txt","w+") 
    for x in range(len(datalines)):
            if (x!=0 and x%6==0):
                outputfile.write("\n")
            outputfile.write("%s" % datalines[x])
            outputfile.write(" ")
                
    outputfile.close()


# In[17]:

#Output lines
def OutputLines2(datalines,num):
    temparr = []
    outputfile = open("output2.txt","w+") 
    for x in range(len(datalines)):
            if (x!=0 and x%4==0):
                outputfile.write("\n")
            outputfile.write("%s" % datalines[x])
            outputfile.write(" ")
                
    outputfile.close()


# In[ ]:

#Output lines
def OutputLines3(datalines,num):
    temparr = []
    outputfile = open("output3.txt","w+") 
    for x in range(len(datalines)):
            if (x!=0 and x%4==0):
                outputfile.write("\n")
            outputfile.write("%s" % datalines[x])
            outputfile.write(" ")
                
    outputfile.close()


# In[ ]:

#### import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as ax3d
import mpl_toolkits.mplot3d.art3d as a3d

numlines = sum(1 for line in open('input.txt'))
finaldata = []
#CALL INPUT LINES
wcsdata = InputLines('input.txt',numlines)
print wcsdata
finaldata = []
#CALL DISPLAY LINES
fig = plt.figure() # Create figure
ax = ax3d.Axes3D(fig) # Create axes
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)
DisplayLines(wcsdata,numlines)
plt.show() 

#viewing point 
eye = [6,8,7.5]

#INITIALIZE SOME MATRICES
tempTranformation = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
transformtranslation = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
transformScale = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
transformRotationx = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
transformRotationy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
transformRotationz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
finalTransformation = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]  

#N
s = 15
d = 60
N = [[int(d/s),0,0,0],[0,int(d/s),0,0],[0,0,1,0],[0,0,0,1]]
Vsx =Vsy = Vcx = Vcy = 512


ppTransformation = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
ppTransformation = PP(6,8,7.5)
cdata = toC(ppTransformation,N,wcsdata)
OutputLines(cdata,numlines)
numlinesend = sum(1 for line in open('output.txt'))
finalcdata = InputLines('output.txt',numlinesend)
newpoints = toXsYs(finalcdata,Vsx,Vsy,Vcx,Vcy)
print newpoints
OutputLines2(newpoints,numlines)
plt.grid()
plt.show()


#PP END
#END PART A




keepgoing = True
firsttime = True
menuitem = raw_input('(1) translate (2) scale (3) rotate (4)Apply Transformation')
while keepgoing:
    #Basic Translate
    if menuitem == "1":
        Tx = input('Factor for Tx: ')
        Ty = input('Factor for Ty: ')
        Tz = input('Factor for Tz: ')
        trans = Translation3d(Tx,Ty,Tz)
        if firsttime:
            finalTrans = trans
            
            firsttime = False
        else:
            finalTrans = finalTrans * trans
    
    #basic Scale
    if menuitem == "2":
        Sx = input('Factor for Sx: ')
        Sy = input('Factor for Sy: ')
        Sz = input('Factor for Sz: ')
        transformScale = Scale3d(Sx,Sy,Sz)
        if firsttime:
            finalTrans = transformScale
            firsttime = False
        else:
            finalTrans = finalTrans * transformScale
    
    #Basic Rotation
    if menuitem == "3":
        rotateitem = raw_input('(1) rotate x (2)rotate y (3)rotate z ')
        if rotateitem == "1":
            angle = input('Angle: ')
            transformRotationx = Rotate3Dx(angle)
            if firsttime:
                finalTrans = transformRotationx 
                firsttime = False
            else:
                finalTrans = finalTrans * transformRotationx 
        elif rotateitem == "2":
            angle = input('Angle: ')
            transformRotationy = Rotate3Dy(angle)
            if firsttime:
                finalTrans = transformRotationy 
                firsttime = False
            else:
                finalTrans = finalTrans * transformRotationy
        elif rotateitem == "3":
            angle = input('Angle: ')
            transformRotationz = Rotate3Dz(angle)
            if firsttime:
                finalTrans = transformRotationz 
                firsttime = False
            else:
                finalTrans = finalTrans * transformRotationz 
        
    
    elif menuitem == "4":
        
        newworlddata = changeworld(finalTrans,N,wcsdata)
        print newworlddata
        OutputLines(newworlddata,numlines)
        news = InputLines('output.txt',numlines)
        
        #new cube
        fig = plt.figure() # Create figure
        ax = ax3d.Axes3D(fig) # Create axes
        ax.set_xlim(-5,5)
        ax.set_ylim(-5,5)
        ax.set_zlim(-5,5)
        DisplayLines(news,numlines)
        plt.show() 
        #newcube
        
        ppTransformation = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
        ppTransformation = PP(6,8,7.5)
        cdata = toC(ppTransformation,N,news)
        OutputLines(cdata,numlines)
        numlinesend = sum(1 for line in open('output.txt'))
        finalcdata = InputLines('output.txt',numlinesend)
        newpoints = toXsYs(finalcdata,Vsx,Vsy,Vcx,Vcy)
        OutputLines2(newpoints,numlines)
        plt.grid()
        plt.show()
        
        
        keepgoing = False
        break
        
    menuitem = raw_input('(1) translate (2) scale (3) rotate (4)Apply Transformation')

    


# In[ ]:




# In[ ]:

#Basic Rotate
"""import math

def Rotate3d(angle,Tx,Ty,Tz):
    rotatez = np.matrix([[math.cos(angle),-(math.sin(angle)), 0, 0], [math.sin(angle),math.cos(angle), 0,0], [0, 0, 1,0],[0,0,0,1]])
    print rotatez
    rotatearoundx = np.matrix([[1,0, 0, 0], [0,math.cos(angle),math.sin(angle),0], [0, -(math.sin(angle)),math.cos(angle),0],[0,0,0,1]])
    print rotatearoundx
    #xaxis
    cosalpha = math.sqrt(math.pow(Tx,2)+math.pow(Ty,2))/math.sqrt(math.pow(Tx,2)+math.pow(Ty,2)+math.pow(Tx,2))
    sinalpha = Tz/math.sqrt(math.pow(Tx,2)+math.pow(Ty,2)+math.pow(Tx,2))
    rotatex = np.matrix([[1,0, 0, 0], [0,cosalpha, sinalpha,0], [0, -sinalpha,cosalpha,0],[0,0,0,1]])
    print rotatex
    #yaxis stuff
    costheta = Ty/math.sqrt(math.pow(Tx,2)+math.pow(Ty,2))
    sintheta = Tx/math.sqrt(math.pow(Tx,2)+math.pow(Ty,2))
    rotatey =  np.matrix([[-(costheta),0, sintheta, 0], [0,1,0,0], [-sintheta,0, -costheta,0],[0,0,0,1]])
    print rotatey
    temp = np.matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    temp = rotatearoundx * rotatex * rotatey * rotatez
    return temp
"""


# In[ ]:



