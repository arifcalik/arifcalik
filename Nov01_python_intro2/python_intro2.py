def arrayCheck(alist):
    one = two = False
    for item in alist:
        if item == 1:
            one = True
        elif item == 2:
            if one == True:
                two = True
            else:
                one = two = False
        elif item == 3:
            if two == True:
                #three = True
                return True
            else:
                one = two = False
        else:
            one = two = False
    return False


def test_arrayCheck():
    assert arrayCheck([1, 1, 2, 3, 1]) == True
    assert arrayCheck([1, 1, 2, 4, 1]) == False
    assert arrayCheck([1, 1, 2, 1, 2, 3]) == True
    assert arrayCheck([1, 1, 2, 7, 1, 2, 0, 3, 2, 1, 2, 3,]) == True
    assert arrayCheck([1, 1, 2, 0, 1, 3, 2, 1, 2, 1, 2, 4, 3, 1, 2,]) == False
    assert arrayCheck([1, 1, 2, 1, 2, 0, 3, 1, 3, 2, 1, 3, 1, 2, 3]) == True    


def stringBits(s):
    return ''.join([c for i, c in enumerate(s) if i % 2 == 0]) 

def test_stringBits():
    assert stringBits('Hello') == 'Hlo' 
    assert stringBits('Hi') == 'H' 
    assert stringBits('Heeololeo') == 'Hello'
    assert stringBits('Wwworldlldde') == 'Wwrdld'

def doubleChar(s):
    return ''.join([c*2 for c in s])

def test_doubleChar():
    assert doubleChar('The') == 'TThhee' 
    assert doubleChar('AAbb') == 'AAAAbbbb' 
    assert doubleChar('Hi-There') == 'HHii--TThheerree'

def count_evens(alist):
    return sum([1 for num in alist if num % 2 == 0])

def test_count_evens(): 
    assert count_evens([2, 1, 2, 3, 4]) == 3
    assert count_evens([2, 2, 0]) == 3 
    assert count_evens([1, 3, 5]) == 0    
    assert count_evens([-1, 1, 7, 3, -123, 23, 67, 7,]) == 0
    assert count_evens([0]) == 1 
    assert count_evens([0, -2, 7, 11, 0, 0, -5]) == 4 

       