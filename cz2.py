#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt

class AppWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "matplotlib example"
        self.initInterface()
        self.initWidgets()
    
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,300,400)
        self.show()
    
    def initWidgets(self):
        btn = QPushButton("rysuj",self)
        xLabel = (QLabel("X",self))
        yLabel = (QLabel("Y",self))
        self.xEdit = QLineEdit()
        self.yEdit = QLineEdit()
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        grid=QGridLayout()
        grid.addWidget(xLabel, 1, 0)
        grid.addWidget(self.xEdit, 1, 1)
        grid.addWidget(yLabel, 2, 0)
        grid.addWidget(self.yEdit, 2, 1)
        grid.addWidget(btn, 3, 0, 1, 2)
        grid.addWidget(self.canvas, 1, 2, -1, -1)
        self.setLayout(grid)
        
        btn.clicked.connect(self.rysuj)
    
    def rysuj(self):
        
        x=float(self.xEdit.text())
        y=float(self.yEdit.text())
        
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        ax.plot(x, y, "ro")
        self.canvas.draw()

        
def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    app.exec_()

if __name__=="__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




