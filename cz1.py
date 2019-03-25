import matplotlib.pyplot as plt

a=[]
b=[]
c=[]
d=[]
print("podaj wspl x punktu a")
ax=int(input())
a.append(ax)
print("podaj wspl y punktu a")
ay=int(input())
a.append(ay)
print("podaj wspl x punktu b")
bx=int(input())
b.append(bx)
print("podaj wspl y punktu b")
by=int(input())
b.append(by)
print("podaj wspl x punktu c")
cx=int(input())
c.append(cx)
print("podaj wspl y punktu c")
cy=int(input())
c.append(cy)
print("podaj wspl x punktu d")
dx=int(input())
d.append(dx)
print("podaj wspl y punktu d")
dy=int(input())
d.append(dy)

if (b[0]-a[0])*(d[1]-c[1])-(b[1]-a[1])*(d[0]-c[0])==0:
    print("proste równoległe")
else:
        t=((c[0]-a[0])*(d[1]-c[1])-(c[1]-a[1])*(d[0]-c[0]))/((b[0]-a[0])*(d[1]-c[1])-(b[1]-a[1])*(d[0]-c[0]))
        Xp=a[0]+t*(b[0]-a[0])
        Yp=a[1]+t*(b[1]-a[1])
        print(t)
        
        if 0 <= t <= 1:
            Xp=a[0]+t*(b[0]-a[0])
            Yp=a[1]+t*(b[1]-a[1])
            print(Xp)
            print(Yp)
            print("proste przecinają sie w punkcie ", Xp, Yp)
            x=[a[0],b[0]]
            y=[a[1],b[1]]
            xb=[c[0],d[0]]
            yb=[c[1],d[1]] 
            xp=[a[0],Xp]
            yp=[a[1],Yp]
            xpd=[c[0],Xp]
            ypd=[c[1],Yp]
            plt.figure(figsize=(10, 10))
            plt.title('Wykres')
            plt.ylabel('wspolrzedna x')
            plt.xlabel('wspolrzedna y')
            plt.plot(y, x, linestyle='--')
            plt.plot(y, x, marker='o')
            plt.plot(yb, xb, linestyle='--')
            plt.plot(yb, xb, marker='o')
            plt.plot(Yp, Xp, marker='o',color='r')
            plt.savefig('Wykres.png')
            DaneABCD=open('daneabcd.txt','w')
            DaneABCD.write("\n   |{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("A","B","C","D","P"))
            DaneABCD.write("\n X |{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(a[0],b[0],c[0],d[0],Xp))
            DaneABCD.write("\n Y |{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(a[1],b[1],c[1],d[1],Yp))
            DaneABCD.close()
        else:
            print("proste nie przecinają się")      
            x=[a[0],b[0]]
            y=[a[1],b[1]]
            xb=[c[0],d[0]]
            yb=[c[1],d[1]] 
            plt.figure(figsize=(10, 10))
            plt.title('Wykres')
            plt.ylabel('wspolrzedna x')
            plt.xlabel('wspolrzedna y')
            plt.plot(y, x, marker='o')
            plt.plot(yb, xb, marker='o')
            plt.savefig('Wykres.png')
            DaneABCD=open('daneabcd.txt','w')
            DaneABCD.write("\n|{:^20}|{:^20}|{:^20}|{:^20}|".format("A","B","C","D"))
            DaneABCD.write("\n X |{:^20}|{:^20}|{:^20}|{:^20}|".format(a[0],b[0],c[0],d[0]))
            DaneABCD.write("\n Y |{:^20}|{:^20}|{:^20}|{:^20}|".format(a[1],b[1],c[1],d[1]))
            DaneABCD.close()

