'''
(15 points)
 Implement
Radix Sort
 on [35, 53, 55, 33,52, 32, 25]. Note that your program
should use
Queue
'''
print("RADIX SORT")
def radix_srot(arrg):
    import math
    arrggg = []
    place = 10
    ret = []
    while len(arrg) > 0:
        arrggg = []
        for x in range(10):
            for i in arrg:
                if math.floor(((i/place)%1)*10+.0000001) == x:
                    #print(math.floor(((i / place) % 1) * 10), end=" = ")
                    #print(x)
                    #print(math.floor(i/place*(place/10)),end=" ")
                    #print(((i*place)%(place*10))/place,end="    ")
                    #print(math.floor(((i/place)%1)*10+.0000001))
                    arrggg.append(i)
        argggggggggg = []
        #print(arrggg)
        for i in arrggg:
            if i%place == i:
                ret.append(i)
            else:
                argggggggggg.append(i)
        #print(argggggggggg)
        #print("---------")
        arrg = argggggggggg
        place *= 10
    return ret

print(radix_srot([35, 53, 55, 33,52, 32, 25]))
print(radix_srot([53,25,33,19,69,10000]))