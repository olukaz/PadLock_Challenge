def challenge1():
    code = 0
    for i in range(1,41):
        code+=i
    return code


def challenge2():
    code = 0
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if digit1<digit2<digit3:            
                    code+=1
    return code

def challenge3():
    
    code = 0
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if digit1 % 2 == 0 | digit2 % 2 == 0 | digit3 % 2 == 0:
                    code+=1
    return code

def challenge4():
    code = 0
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if ((digit1)+(digit2)+(digit3)) % 2 != 0:
                    code+=1
    return code


def challenge5():
    code = 0
    for digit1 in range(0,10):
        for digit2 in range(0,10):
            for digit3 in range(0,10):
                if digit1==digit2 or digit1==digit3 or digit2==digit3:
                    code+=1
    return code




print(f'Challenge 1: ', challenge1())
print(f'Challenge 2: ', challenge2())
print(f'Challenge 3: ', challenge3())
print(f'Challenge 4: ', challenge4())
print(f'Challenge 5: ', challenge5())