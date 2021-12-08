def permutations(n):

    lst=[]
    newlst=[]
    
    for i in range(1,n+1):
        lst.append(i)


    if n==3 or n==2:
        print("NO SOLUTION")

    elif n==1:
        print(1)

    else:
        odd=[]
        even=[]

        for i in lst:
            if i%2!=0:
                odd.append(i)
            else:
                even.append(i)

        newlst=even+odd

    for i in newlst:
        print(i , end= " ")


n=int(input())

permutations(n)
    
