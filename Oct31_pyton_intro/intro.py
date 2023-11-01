s = 'Python'

def test_answer1():
    assert s[4] == 'o' 
    assert s[:4] == 'Pyth' 
    assert s[1:4] == 'yth' 
    assert s[::-1] == 'nohtyP'

def test_answer2():
    l = [3,7,[1,4,'hello']] 
    l[2][2] = "goodbye"
    assert l[2][2] == "goodbye"


def test_answer3():
    d1 = {'simple_key':'hello'} 
    assert d1['simple_key'] == "hello"
    d2 = {'k1':{'k2':'hello'}} 
    assert d2['k1']['k2'] == "hello"
    d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
    assert d3['k1'][0]['nest_key'][1][0] == "hello"

def test_answer4():
    mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]  
    myset = set(mylist)  
    assert myset == set([1,2,3]) 

def test_answer5():
    age = 4 
    name = "Sammy"
    output = f"Hello my dog's name is {name} and he is {age} years old"
    assert output == "Hello my dog's name is Sammy and he is 4 years old"  
  