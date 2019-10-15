def squares(n):
    """Compute the squares of numbers from 1 to n, such that the 
    ith element of the returned list equals i^2.
    
    """
    # YOUR CODE HERE
    final="["
    #print("[",end="")
    for i in range(n):
        j=(i+1)*(i+1)
        tp=str(j)
        final=final+tp
        if i+1<n:
            sp=", "
            final=final+sp
            #print(", ",end="")
    en="]"
    final=final+en
    final.strip()
    print(final)
    #print("]")
        
     
  arr=[]
    arr=[(i+1)*(i+1) for i in range(n)]
    print(arr)