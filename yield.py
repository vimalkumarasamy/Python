def simpleGeneratorFun(): 
    check='It can return strings'
    yield check
    yield ' '.join(check)
    yield 3
  
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 