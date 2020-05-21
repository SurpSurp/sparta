import random

def randomCoin(n):
    
    countF = 0
    countB = 0
    for i in range(n):
        randomN = random.randint(0, 1)
        if randomN ==  1:
            countF += 1 
        else:
            countB += 1

    print("앞면이 나온 횟수= ", countF)
    print("뒷면이 나온 횟수= ", countB)




n = int(input("반복할 횟수를 정하세요: "))
randomCoin(n)
