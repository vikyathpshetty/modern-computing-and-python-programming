psum = nsum = 0
number = int(input("enter a number: "))

while (number != -1):
    if (number > 0):
        print("postive")
        psum = psum + number 
    elif (number < 0):
        print("negative")
        nsum = nsum + number 
    else:
        print("zero")
        
    number = int(input("enter a number: "))
     
print("total of positive numbers: ", psum)
print("total of negative numbers: ", nsum)