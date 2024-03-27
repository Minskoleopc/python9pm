# worldbank ---- save() loan()
# SBI       ---- save() loan()
# ICIC      ---- save() loan()

# complete abstraction ---- method definitaion 
# partial  abstraction ---- complete method abstact


# from abc import ABC , abstractmethod
# class WorldBank(ABC):
#     @abstractmethod
#     def loan(self,x):
#         pass
#     @abstractmethod
#     def save(self,x):
#         pass

# # we cannot create object of abstract class 
# #a = WorldBank()

# class SBI(WorldBank):
#     # loan 
#     def loan(self,x):
#         print("loan is "+ str(x))
    
#     #save
#     def save(self,x):
#         print("save is "+ str(x))

#     def branchName(self):
#         print("nagpur")

# class PNB(WorldBank):
#     #loan 
#     def loan(self,x):
#         print("loan is "+ str(x))
    
#     #save
#     def save(self,x):
#         print("save is "+ str(x))

#     def branchName(self):
#         print("nagpur")



# nagpur = SBI()
# nagpur.loan(3)
# nagpur.loan(13)
    
# nagpurPNB = PNB()


from abc import ABC , abstractmethod
class worldBank(ABC):
    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def save(self):
        pass

    def country(self):
        print("India")

class SBI(worldBank):
    def loan(self):
        print("loan from SBI")

    def save(self):
        print("save from SBI")
    

class PNB(worldBank):
    def loan(self):
        print("loan from PNB")

    def save(self):
        print("save from PNB")

sbiTwo = SBI()
sbiTwo.loan()
sbiTwo.save()
sbiTwo.country()
