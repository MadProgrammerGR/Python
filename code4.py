import Image, ImageDraw
import random
import math

def apostash_dio_shmeiwn(x1,y1,x2,y2):
    x = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return x

img = Image.new('RGB', (1024, 1024), "black")
draw = ImageDraw.Draw(img)
#circles=[[x1,y1,r1],...,[xn,yn,rn]]
circles=[]
for i in range(20):
    x = random.randint(0,1024)
    y = random.randint(0,1024)
    r = random.randint(10,500)
    circles.append([x,y,r])
    draw.ellipse((x-r, y-r, x+r, y+r), outline ='red')

#sygkrish ka8e kyklou me tous ypolipous
count=0
for i in range(20):
    for j in range(20):
        #wste na mhn elenx8ei me ton eauto tou
        if i!=j:
            #d h apostash twn kentrwn
            xi = circles[i][0]
            yi = circles[i][1]
            xj = circles[j][0]
            yj = circles[j][1]
            d = apostash_dio_shmeiwn(xi,yi, xj,yj)
            
            #syn8hkh gia na temnonte(xwris na emperiexontai)
            r1 = circles[i][2]
            r2 = circles[j][2]
            if d <= r1 + r2 and d >= abs(r1-r2):
                count += 1
                break

print "Temnontai %d kykloi" %count
img.show()
#img.save("circle.png")#(an den anoigei me show)
