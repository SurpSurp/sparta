
def findMaxNum():
    num_1 = int(input("정수 한 개를 입력하세요:"))
    max = num_1
    for i in range(4):
        num = int(input("정수 한 개를 입력하세요:"))
        if num > max:
            max = num

    return max

max = findMaxNum()
print("최대값 = ", max)
    

