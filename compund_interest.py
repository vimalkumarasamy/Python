def years_to_2x_investment_compound(initial_investment, interest_rate):

    # YOUR CODE HERE
    # YOUR CODE HERE
    initial_investment=float(initial_investment)
    interest_rate=float(interest_rate)
    doub=2 * initial_investment
    
    for i in range(1, 1001):
        final=initial_investment*(1+ (interest_rate/100)**i)
        if final>=doub:
            return(i)
            break
            
x=1
x=years_to_2x_investment_compound(1000000,5)

print(x)