def squares(n):
    """Compute the squares of numbers from 1 to n, such that the 
    ith element of the returned list equals i^2.
    
    """
    # YOUR CODE HERE
    array=[]
    for i in range(n):
        j=(i+1)*(i+1)
        array.append(j)
    print(array)
    #raise NotImplementedError()
#if squares(10) != [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
 #   print("not-match")

# assert squares(1) == [1]
squares(9)