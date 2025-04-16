#name:shaikh maviya 
#uin 231p050
#roll no 25 

print("performed by maviya")

def sum(n):
    if n<1:
        return n
    
    else:
        return n+sum(n-1)
    


n=int(input("enter number till sum has to be calculated "))
print("sum of number is :",sum(n))




num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))
num3=int(input("enter the number 3"))

def largest(num1,num2,num3):
    if (num1>num2) and (num1>num3):
        print("largest is :",num1)

    elif num2>num3:
        print("largest is :",num2)

    else:
        print("largest is :",num3)
    
    



n=largest(num1,num2,num3)  