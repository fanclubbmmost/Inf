import matplotlib.pyplot as plt
a=[1,2]
b=[3,5]
c=[1,1]
d=[5,1]
if (b[0]-a[0])*(d[1]-c[1])-(b[1]-a[1])*(d[0]-c[0])==0:
    print("proste równoległe")
else:
        t=((c[0]-a[0])*(d[1]-c[1])-(c[1]-a[1])*(d[0]-c[0]))/((b[0]-a[0])*(d[1]-c[1])-(b[1]-a[1])*(d[0]-c[0]))
        Xp=a[0]+t*(b[0]-a[0])
        Yp=a[1]+t*(b[1]-a[1])
        print(t)
        print(Xp)
        print(Yp)
        if 0 <= t <= 1:
            print("proste przecinają sie w punkcie ", Xp, Yp)
        else:
            print("proste nie przecinają się")
        
x=[a[0],b[0]]
y=[a[1],b[1]]
xp=[c[0],d[0]]
yp=[c[1],d[1]] 
plt.figure(figsize=(10, 10))
plt.title('Wykres')
plt.ylabel('wspolrzedna x')
plt.xlabel('wspolrzedna y')
plt.plot(y, x)
plt.plot(yp, xp)