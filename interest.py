def years_to_2x_investment_simple(initial_investment, interest_rate):

    # YOUR CODE HERE
    initial_investment=float(initial_investment)
    interest_rate=float(interest_rate)

    doub=2 * initial_investment
    
    for i in range(1, 1001):
        final=initial_investment*(1+ (interest_rate*i/100))
        if final>=doub:
            duration=i
            break 
    return(duration)
    

dur=years_to_2x_investment_simple(100000, 5)
print(dur)
