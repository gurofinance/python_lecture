def multi(v1, v2):
    retList = []
    res1 = v1 +v2
    res2 = v1 -v2
    retList.append(res1)
    retList.append(res2)
    return retList

def multi_1(v1, v2):
    res1 = v1 +v2
    res2 = v1 -v2

    return res1, res2


myList = multi(100, 200)

print(myList[0], myList[1])

myresult1 , myresult2  = multi_1(100, 200)

print(myresult1 ,myresult2 )


