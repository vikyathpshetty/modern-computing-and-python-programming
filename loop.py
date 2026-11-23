number = int(input("enter a positive integer"))
if (number <= 0):
    print("PLEASE ENTER POSITIVE NUMBER")
else:
    i = 1
    while (i != 10):
        print(f"{number}*{i} = {number}*{i}")
        i = i + 1
        