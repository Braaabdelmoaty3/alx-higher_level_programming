#class Bikes:
#    def __init__(self, description, cost, sale_cost, condtion):
#        self.description = description
#        self.cost = cost
#        self.sale_cost = sale_cost
#        self.condtion = condtion
#bike1 = Bikes("Univega Alpina, orange",10000,False,0.5)
#print(bike1.condtion)
#print(dir(bike1)) # to list all the attribute
#bike1.km = 12000 # to add a new attribute
#print(dir(bike1))
class MyIinteger:
    def set_val(self,val):
        if (type(val) == int):
            self.val = val # here i safe the value of val 
        else:
            print("the data type does not integer !")

    def get_val(self):
        return self.val

    def increament_val(self):
        self.val+= 1

i = MyIinteger()

i.set_val(9)
print(i.get_val())

i.set_val("eh ya ahbl")
print(i.get_val())
    

        
