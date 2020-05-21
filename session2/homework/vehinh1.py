from turtle import *
shape ("turtle")
speed(-1)
pensize(4)
color('DarkOliveGreen2')

goc_nhon = 55                 #int(input("Dien goc nhon cua hinh thoi vao day: "))
goc_tu = 180 - goc_nhon
goc_quay = (180-2*goc_nhon)/2
left(goc_nhon/2)
for i in range(4):
    forward(100)
    right(goc_nhon)
    forward(100)
    right(goc_tu)
    forward(100)
    right(goc_nhon)
    forward(100)
    right(goc_quay)

mainloop()
    
