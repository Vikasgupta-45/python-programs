

class employee:
    def __init__(self,id):
        self.id=id

    def setname(self,name):
        self.name=name
    
    def getname(self):
        return self.name

    def getid(self):
        return self.id
     

class student:

    def __init__(self,college):
        self.college=college

    
    
    def setbranch(self,branch):
        self.branch=branch

    def getbranch(self):
        return self.branch    


    
    def getcollege(self):
        return self.college

    





class intern(employee,student):
    def __init__(self,id,college,period):
        employee.__init__(self,id)
        student.__init__(self,college)
        self.period=period

    def setdetails(self,name,branch):
        super().setname(name)    
        super().setbranch(branch)

        

    def getdetails(self):
        print("ID      : ",super().getid())
        print("name      : ",super().getname())    
        print(" COLLEGE NAME :",super().getcollege())
        print("BRANCH :",super().getbranch())
        print("PERIOD:",self.period)


id = input("Enter ID: ")
college = input("Enter College Name: ")
period = input("Enter Internship Period (e.g., 6 months): ")
name = input("Enter Name: ")
branch=input("enter your branch ")



i=intern(id,college,period)
i.setdetails(name,branch)
i.getdetails()






