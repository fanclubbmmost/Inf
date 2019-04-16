#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from math import atan, pi,sqrt

class AppWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "matplotlib example"
        self.col1="red"
        self.col2="blue"
        self.initInterface()
        self.initWidgets()
    
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,300,400)
        self.show()
    
    def initWidgets(self):
        btn = QPushButton("draw",self)
        btnCol1 = QPushButton("color AB",self)
        btnCol2 = QPushButton("color CD",self)
        xLabel = (QLabel("Xa",self))
        yLabel = (QLabel("Ya",self))
        self.xEdit = QLineEdit()
        self.yEdit = QLineEdit()
        xbLabel = (QLabel("Xb",self))
        ybLabel = (QLabel("Yb",self))
        self.xbEdit = QLineEdit()
        self.ybEdit = QLineEdit()
        xcLabel = (QLabel("Xc",self))
        ycLabel = (QLabel("Yc",self))
        self.xcEdit = QLineEdit()
        self.ycEdit = QLineEdit()
        xdLabel = (QLabel("Xd",self))
        ydLabel = (QLabel("Yd",self))
        self.xdEdit = QLineEdit()
        self.ydEdit = QLineEdit()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        K1a=QLabel('Kąt ostry',self)
        K2a=QLabel('Kąt rozwarty',self)
        self.K1=QLineEdit()
        self.K2=QLineEdit()
        M1a=QLabel('Punkt P względem AB po:',self)
        M2a=QLabel('Punkt P względem CD po:',self)
        self.M1=QLineEdit()
        self.M2=QLineEdit()
        A1a=QLabel('Azymut odcinka AB:',self)
        A2a=QLabel('Azymut odcinka CD:',self)
        self.A1=QLineEdit()
        self.A2=QLineEdit()
        resultLabel=QLabel('',self)
        
        grid=QGridLayout()
        grid.addWidget(xLabel, 1, 0)
        grid.addWidget(self.xEdit, 1, 1)
        grid.addWidget(yLabel, 1, 2)
        grid.addWidget(self.yEdit, 1, 3)
        grid.addWidget(xbLabel, 2, 0)
        grid.addWidget(self.xbEdit, 2, 1)
        grid.addWidget(ybLabel, 2, 2)
        grid.addWidget(self.ybEdit, 2, 3)
        grid.addWidget(xcLabel, 3, 0)
        grid.addWidget(self.xcEdit, 3, 1)
        grid.addWidget(ycLabel, 3, 2)
        grid.addWidget(self.ycEdit, 3, 3)
        grid.addWidget(xdLabel, 4, 0)
        grid.addWidget(self.xdEdit, 4, 1)
        grid.addWidget(ydLabel, 4, 2)
        grid.addWidget(self.ydEdit, 4, 3)
        grid.addWidget(btnCol1, 5, 0, 1, 2)
        grid.addWidget(btnCol2, 6, 0, 1, 2)
        grid.addWidget(btn, 7, 0, 1, 2)
        grid.addWidget(K1a,8,0,1,2)
        grid.addWidget(self.K1,8,3)
        grid.addWidget(K2a,9,0,1,2)
        grid.addWidget(self.K2,9,3)
        grid.addWidget(M1a,10,0,1,2)
        grid.addWidget(self.M1,10,3)
        grid.addWidget(M2a,11,0,1,2)
        grid.addWidget(self.M2,11,3)
        grid.addWidget(A1a,12,0,1,2)
        grid.addWidget(self.A1,12,3)
        grid.addWidget(A2a,13,0,1,2)
        grid.addWidget(self.A2,13,3)
        grid.addWidget(self.canvas, 1, 7, -1, -1)
        
        self.setLayout(grid)
        
        btn.clicked.connect(self.oblicz)
        btnCol1.clicked.connect(self.color1)
        btnCol2.clicked.connect(self.color2)
    
    def sprawdzliczbe(self, element):
         if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
         else:
            element.setFocus()
            return None
        
    def color1(self):
        kolor1= QColorDialog.getColor()
        if kolor1.isValid():
            print('color AB', kolor1.name())
            self.col1 = kolor1.name()
            self.draw()
            
    def color2(self):
        kolor2= QColorDialog.getColor()
        if kolor2.isValid():
            print('color AB', kolor2.name())
            self.col2 = kolor2.name()
            self.draw()
    
    def draw(self):
        x=self.sprawdzliczbe(self.xEdit)
        y=self.sprawdzliczbe(self.yEdit)
        xb=self.sprawdzliczbe(self.xbEdit)
        yb=self.sprawdzliczbe(self.ybEdit)
        xc=self.sprawdzliczbe(self.xcEdit)
        yc=self.sprawdzliczbe(self.ycEdit)
        xd=self.sprawdzliczbe(self.xdEdit)
        yd=self.sprawdzliczbe(self.ydEdit)
        
        if None not in [x,y,xb,yb,xc,yc,xd,yd]:
            x=float(self.xEdit.text())
            y=float(self.yEdit.text())
            xb=float(self.xbEdit.text())
            yb=float(self.ybEdit.text())
            xc=float(self.xcEdit.text())
            yc=float(self.ycEdit.text())
            xd=float(self.xdEdit.text())
            yd=float(self.ydEdit.text())
            a=[]
            b=[]
            c=[]
            d=[]
            a.append(x)
            a.append(y)
            b.append(xb)
            b.append(yb)
            c.append(xc)
            c.append(yc)
            d.append(xd)
            d.append(yd)
            dx1=[x,xb]
            dy1=[y,yb]
            dx2=[xc,xd]
            dy2=[yc,yd]
            
            
            if (xb-x)*(yd-yc)-(yb-y)*(xd-xc)==0:
                print("proste równoległe")
                self.figure.clear()
                ax=self.figure.add_subplot(111)
                ax.plot(dx1, dy1, color=self.col1)
                ax=self.figure.add_subplot(111)
                ax.plot(dx2, dy2, color=self.col2)
                self.canvas.draw()
                self.M1.setText('Odcinki')
                self.M2.setText('równoległe')

            else:
                t=((c[0]-a[0])*(d[1]-c[1])-(c[1]-a[1])*(d[0]-c[0]))/((b[0]-a[0])*(d[1]-c[1])-(b[1]-a[1])*(d[0]-c[0]))
                Xp=a[0]+t*(b[0]-a[0])
                Yp=a[1]+t*(b[1]-a[1])
                print(t)

                if 0 <= t <= 1:
                    print("proste przecinają sie w punkcie ", Xp, Yp)
                    self.figure.clear()
                    ax=self.figure.add_subplot(111)
                    ax.plot(dx1, dy1, color=self.col1)
                    ax=self.figure.add_subplot(111)
                    ax.plot(dx2, dy2, color=self.col2)
                    ax=self.figure.add_subplot(111)
                    ax.plot(Xp, Yp, color="pink", marker='o')
                    self.canvas.draw()
                    
                else:
                    print("proste nie przecinają się")  
                    dxp1=[x,Xp]
                    dyp1=[y,Yp]
                    dxp2=[xc,Xp]
                    dyp2=[yc,Yp]
                    self.figure.clear()
                    ax=self.figure.add_subplot(111)
                    ax.plot(dxp1, dyp1, color="pink", linestyle="--")
                    ax=self.figure.add_subplot(111)
                    ax.plot(dxp2, dyp2, color="pink", linestyle="--")
                    ax=self.figure.add_subplot(111)
                    ax.plot(dx1, dy1, color=self.col1)
                    ax=self.figure.add_subplot(111)
                    ax.plot(dx2, dy2, color=self.col2)
                    ax=self.figure.add_subplot(111)
                    ax.plot(Xp, Yp, color="pink", marker='o')
                    self.canvas.draw()
            
                dxAB=xb-x
                dyAP=Yp-y
                dxAP=Xp-x
                dyAB=yb-y
                k=dxAB*dyAP-dxAP*dyAB
                if k==0:
                    self.M1.setText('współliniowe')
                elif k>0:
                    self.M1.setText('prawej stronie')
                else:
                     self.M1.setText('lewej stronie')

                dxCD=xd-xc
                dyCP=Yp-yc
                dxCP=Xp-xc
                dyCD=yd-yc
                kb=dxCD*dyCP-dxCP*dyCD
                if kb==0:
                    self.M2.setText('współliniowe')
                elif kb>0:
                    self.M2.setText('prawej stronie')
                else:
                    self.M2.setText('lewej stronie')
                
        else:
            print ("prosze wpisac poprawne dane")
            
    def kat(self):
        x=self.sprawdzliczbe(self.xEdit)
        y=self.sprawdzliczbe(self.yEdit)
        xb=self.sprawdzliczbe(self.xbEdit)
        yb=self.sprawdzliczbe(self.ybEdit)
        xc=self.sprawdzliczbe(self.xcEdit)
        yc=self.sprawdzliczbe(self.ycEdit)
        xd=self.sprawdzliczbe(self.xdEdit)
        yd=self.sprawdzliczbe(self.ydEdit)
       
        if (xb-x)==0 and (xd-xc)==0:
            print("brak przeciecia")
        elif (xb-x)==0 and xc==0:
            fi=atan(yd/xd)*200/pi
        elif (xb-x)==0 and xd==0:
            fi=atan(yc/xc)*200/pi
        elif (xd-xc)==0 and x==0:
            fi=atan(yb/xb)*200/pi
        elif (xd-xc)==0 and xb==0:
            fi=atan(y/x)*200/pi
        else:    
            a1=(yb-y)/(xb-x)
            a2=(yd-yc)/(xd-xc)
            fi=atan(abs((a1-a2)/(1+a1*a2)))*200/pi
        fi=round(fi,4)
        fir=200-fi
        fir=round(fir,4)
        if fi>100:
            self.K2.setText(str(fi))
            self.K1.setText(str(fir))
        else:
            self.K1.setText(str(fi))
            self.K2.setText(str(fir))
                    
    def azymut(self):
        x=self.sprawdzliczbe(self.xEdit)
        y=self.sprawdzliczbe(self.yEdit)
        xb=self.sprawdzliczbe(self.xbEdit)
        yb=self.sprawdzliczbe(self.ybEdit)
        xc=self.sprawdzliczbe(self.xcEdit)
        yc=self.sprawdzliczbe(self.ycEdit)
        xd=self.sprawdzliczbe(self.xdEdit)
        yd=self.sprawdzliczbe(self.ydEdit)
        dxAB=xb-x
        dyAB=yb-y
        dxCD=xd-xc
        dyCD=yd-yc  
        if dyAB==0:
            az=100
            az=round(az,4)
            self.A1.setText(str(az))
        elif dyAB>0 and dxAB>0:
            az=atan(dxAB/dyAB)*200/pi
            az=round(az,4)
            self.A1.setText(str(az))
        elif dyAB<0 and dxAB>0:
            az=atan(dxAB/dyAB)*200/pi+200
            az=round(az,4)
            self.A1.setText(str(az))
        elif dxAB<0 and dyAB<0:
            az=atan(dxAB/dyAB)*200/pi+200
            az=round(az,4)
            self.A1.setText(str(az))
        elif dyAB>0 and dxAB<0:
            az=atan(dxAB/dyAB)*200/pi+400
            az=round(az,4)
            self.A1.setText(str(az))
        if dyCD==0:
            az1=100
            az1=round(az1)
        elif dyCD>0 and dxCD>0:
            az1=atan(dxCD/dyCD)*200/pi
        elif dyCD<0 and dxCD>0:
            az1=atan(dxCD/dyCD)*200/pi+200
        elif dxCD<0 and dyCD<0:
            az1=atan(dxCD/dyCD)*200/pi+200
        elif dyCD>0 and dxCD<0:
            az1=atan(dxCD/dyCD)*200/pi+400
        elif dxCD==0:
            az1=0
        az1=round(az1)
        self.A2.setText(str(az1))
        if dxCD==0:
            self.A2.setText('0')

    def oblicz(self):
        self.draw()
        self.kat()
        self.azymut()
            
def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    app.exec_()

if __name__=="__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




