for i in range(1,11):
    for j in range(1,21):
        if j>=12-i and j<=10+i:
            print("*",end="")
        else:
            print(" ",end="")

    print()

for i in range(1,13):
    for j in range(1,21):
        if j>=i and j<=22-i:
            print("*",end="")
        else:
            print(" ",end="")

    print()
