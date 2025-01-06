# static methods

class Math:
    def __init__(self, num):
        self.num = num 

    def addToNum(self, n):
        return self.num + n
    
    @staticmethod
    def squareNum(num):
        return num * num

m = Math(2)
print(m.addToNum(5))
print(Math.squareNum(5))