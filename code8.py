def print_board(matrix):
    text=""
    for row in matrix:
        for c in row:
            text += str(c)
        text+="\n"
    print text

def peristrofh(matrix):
    #dhmiourgia adeiou 8x8
    temp=[["" for i in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(8):
            temp[i][j] = matrix[7-j][i]
    matrix = temp
    return matrix
    
#metatroph apo text se pinaka
pinakas=[]
text = open("pinakas.txt", "r")
for row in text:
    t=[]
    for c in row:
        if str(c)!="\n":
            t.append(str(c))
    pinakas.append(t)


print "==========================\nArxikos pinakas:"
print_board(pinakas)
print "==========================\nPrwth peristrofh pros de3ia:"
pinakas = peristrofh(pinakas)
print_board(pinakas)
print "==========================\nDeuterh:"
pinakas = peristrofh(pinakas)
print_board(pinakas)
print "==========================\nTrith:"
pinakas = peristrofh(pinakas)
print_board(pinakas)
        




