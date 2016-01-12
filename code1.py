import random

"""
def print_matrix(matrix):
	txt = ""
	for row in matrix:
		for c in row:
			txt += str(c)+" "
		txt += "\n"
	print txt
"""

def move_up(matrix, x, y):
        global playerx
        global playery
        if y-1>=0:
                matrix[y][x] = 0
                matrix[y-1][x] = 1
                playery+= -1
        return matrix
        
def move_left(matrix, x, y):
        global playerx
        global playery
        if x-1>=0:
                matrix[y][x] = 0
                matrix[y][x-1] = 1
                playerx+= -1
        return matrix
        
def move_down(matrix, x, y):
        global playerx
        global playery
        if y+1<=9:
                matrix[y][x] = 0
                matrix[y+1][x] = 1
                playery+= 1
        return matrix
        
def move_right(matrix, x, y):
        global playerx
        global playery
        if x+1<=9:
                matrix[y][x] = 0
                matrix[y][x+1] = 1
                playerx+= 1
        return matrix
        
#apostash metrhmenh se tetragwna dld akeraies kinhseis
def distance(x1, y1, x2, y2):
        apostash = abs(x1-x2)+abs(y1-y2)
        return apostash


def print_matrix(matrix):
	txt = ""
	for row in matrix:
		for c in row:
			txt += str(c)+" "
		txt += "\n"
	print txt


#dhmiourgia epipedou 10x10
Map = [[0 for i in range(10)] for i in range(10)]

#epilogh 2 diaforetikwn tyxaiwn shmeiwn me syntetagmenes
f=False
while f == False:
        global playerx
        global playery
        playerx = random.randint(0,9)
        playery = random.randint(0,9)
        goalx = random.randint(0,9)
        goaly = random.randint(0,9)
        if not((playerx==goalx)and(playery==goaly)):
                f = True
Map[playery][playerx] = 1
Map[goaly][goalx] = 2

#ena loop ka8e kinhsh
print "Apanthse me WASD gia to pou 8a kinh8eis"
treasure = False
while treasure == False:
        #print_matrix(Map)
        kinhsh = str(raw_input(""))

        if kinhsh == "W" or kinhsh == "w":
                Map = move_up(Map, playerx, playery)
                print playery
        elif kinhsh == "A" or kinhsh == "a":
                Map = move_left(Map, playerx, playery)
        elif kinhsh == "S" or kinhsh == "s":
                Map = move_down(Map, playerx, playery)
        elif kinhsh == "D" or kinhsh == "d":
                Map = move_right(Map, playerx, playery)
        else:
                kinhsh = str(raw_input("Mh egkyro input, 3anadokimase"))

        r = distance(playerx, playery, goalx, goaly)
        if r == 0:
                print "Sygxarhthria vrhkes to 8ysauro!!!"
                treasure = True
        else:
                print "Einai mono %d tetragwna makria!" %r



        
        
