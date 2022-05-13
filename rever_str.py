def decorator_funk(funk):
    print('We rever string')
    return funk

@decorator_funk    
def rever_str(string: str):
    return string[::-1]


