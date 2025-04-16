#name:shaikh maviya 
#uin 231p050
#roll no 25 

print("performed by maviya")
def present():
    p=[]
    n=int(input("enter the no of student present :"))
    for i in range(1,n+1):
        roll_no=int(input("enter the roll no of student:"))
        p.append(roll_no)



    print("the list of student present is :",p)
    return p


def detail(roll,attendence_list):
    if roll in attendence_list:
        print("roll no is present ")

    else:
        print("not present ")



attendence_listi=present()
roll=int(input("enter the number to be searched "))
detail(roll,attendence_listi)
