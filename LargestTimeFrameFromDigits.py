def largestTimeFromDigits(arr):
    
    Time = []

    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                for l in range(len(arr)):
                    x = arr[i]*1000 + arr[j]*100 + arr[k]*10 + arr[l]
                    Time.append(x)
    
    newTime = []
    for i in range(len(Time)):
        if Time[i] < 2400:
            newTime.append(Time[i])
    
    if not newTime:
        print("")
    
    newNewTime = []
    for i in range(len(newTime)):
        if newTime[i] % 100 < 59:
            newNewTime.append(newTime[i])
    
    if not newNewTime:
        print("")
    
    ans = max(newNewTime)

    Hour = int(ans/100) 
    Minute = ans - Hour * 100 

    str = "{}:{}".format(Hour, Minute)
    return str

    
        

arr = [1,2,3,4]
x = largestTimeFromDigits(arr)
print(x)