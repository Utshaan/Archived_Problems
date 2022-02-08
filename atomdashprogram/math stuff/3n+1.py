from fpack import Syracuse

theIntermediate = "" 
x = int(input())
print(Syracuse(x))

y = Syracuse(x)

#for i in range(1,len(y)+1):
#    theIntermediate = theIntermediate + str(y[i-1])


for ele in y:
    theIntermediate += str(ele)
    theIntermediate += ","

theIntermediate = theIntermediate.rstrip(theIntermediate[-1])


file = open(r"C:\Users\Utkar\Dropbox\Atom programs\math stuff\hailstoneSeries.txt", "a")
file.write(theIntermediate)
file.write("\n")
file.close()
