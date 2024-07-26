n = int(input("raqam kiriting: "))
for num in range(1, n):
    if num %3==0 and num%5==0:
        print("fizbuz")
    elif num%3==0:
        print("fiz")
    elif num %5==0:
        print("buz")
    else:
        print(num)
    
