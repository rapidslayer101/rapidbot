num_ = 1
while True:
    #num = int(input("num: "))
    num_ += 1
    num = num_
    num_saved = num
    highest_num = 0
    steps = 0
    while True:
        steps += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3*num+1

        if num > highest_num:
            highest_num = num
        if num == 1:
            break
        #print(num)

    print(f"Num: {num_saved}, Steps: {steps}, Highest_num: {highest_num}")