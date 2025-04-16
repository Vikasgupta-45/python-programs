#name:shaikh maviya 
#uin 231p050
#roll no 25

print("performed by maviya ")
class person:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def display(self):
        print("name:",self.name)
        print("age:",self.age)


class teacher(person):
    exp=""
    area=""

    def __init__(self,name,age,exp,area):    
        person.__init__(self,name,age)
        self.exp=exp
        self.area=area 


    def display(self):
        person.display(self)    
        print("exp:",self.exp)
        print("area:",self.area)


class student(person):
    cource=""
    marks=0
    def __init__(self,name,age,cource,marks):    
        person.__init__(self,name,age)
        self.cource=cource
        self.marks=marks 


    def display(self):
        person.display(self)    
        print("cource:",self.cource)
        print("marks:",self.marks)



         
print("******TEACHER******")
T = teacher("Ashfaque", 50, 20,"Python")
T.display()
print("******STUDENT******")
S = student("Mohamedali", 20, "B.Tech", 60)
S.display()