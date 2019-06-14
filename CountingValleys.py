def countingValleys(n, s):
    sea_level = valley = 0
    for word in s:
        if(word=='U'):
            sea_level +=1
        else:
            sea_level -=1

        if(sea_level==0 and word=='U'):
            valley+=1
    return valley
