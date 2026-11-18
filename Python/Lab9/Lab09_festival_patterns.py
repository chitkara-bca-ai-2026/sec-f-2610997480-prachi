a=int(input("Enter the number of rows: "))
print("Pattern 1: Star Triangle")
print("-"*35)
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("Pattern 2: Number Triangle")
print("-"*35)
for i in range(1,a+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
print("Pattern 3: Inverted Star Triangle")
print("-"*35)
for i in range(a,0,-1):
    for j in range(i):
        print("*" ,end="")
    print()
print("Pattern 4: Pyramid")
print("-"*35)
for i in range(1,a+1):
    for col in range(a-i):
        print(" ",end="")
    for col in range(2*i-1):
        print("*",end="")
    print()