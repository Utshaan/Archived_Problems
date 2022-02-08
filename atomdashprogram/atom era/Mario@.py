
def MarioTower(y):
     if y >= 1:
       x = 1
       while x <= y:
         return("#" * x)
         if x == y:
          break
         x = x + 1
     else :
        return("give me a proper input")
y = int(input("Enter a random positive integer: "))
print(MarioTower(y))
