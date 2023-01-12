def get_input():
    num_1 = int(input("Enter the first number > "))
    num_2 = int(input("Enter the second number > "))
    return num_1, num_2

def divide_by_2(number):
    mocks = []
    while number != 0:
        mocks.append(number)
        number = number // 2

    return mocks

if __name__=='__main__':
    (num_1, num_2) = get_input()
    mocks = []

    if num_1 > num_2:
        mocks = divide_by_2(num_2)
    else:
        mocks = divide_by_2(num_1)

    print(mocks)
    
