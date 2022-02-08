from fpack import SumofSquares, SquareofSum

x = int(input("number, now\n"))
a = SquareofSum(x)-SumofSquares(x)
print(a)
