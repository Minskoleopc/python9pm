class Calculator:
    # def addition(self,x,y):
    #     print(x+y)

    # def addition(self,x,y,z):
    #     print(x+y+z)

    # def addition(self,x,y,z,a):
    #     print(x+y+z+a)

    def addition(self,x=None, y=None , z  = None , a = None):
        if x != None and y !=None and z != None and a != None:
            print(x+y+z+a)
        elif x != None and y !=None and z != None:
            print(x+y+z)
        elif x != None and y !=None:
            print(x+y)


cc  = Calculator()
cc.addition(12,3)
cc.addition(12,3,4)
cc.addition(12,3,4,5)