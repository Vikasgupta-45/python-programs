#programm performed by maviya 
# uin 231p050
# roll no 37

fname=input("Enter file name: ")
num_lines=0
with open(fname, 'r') as f:
    for line in f:
        num_lines+=1
print("Number of lines:")
print(num_lines)