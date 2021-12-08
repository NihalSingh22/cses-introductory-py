def repetitions(s):
    counter=0
    maxcounter=0

    string=''

    for i in s:
        if i==string:
            counter=counter+1
        else:
            maxcounter=max(counter,maxcounter)
            counter=1
            string=i


    maxcounter=max(counter,maxcounter)

    print(maxcounter)

s=input()

repetitions(s)
