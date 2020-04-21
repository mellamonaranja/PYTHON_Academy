def sum(a, b):
    return a + b

def safeSum(a, b):
    if type(a) != type(b):
        print('더할 수 있는 값이 아닙니다.')
        return
    else:
        result = sum(a, b)
    
    return result