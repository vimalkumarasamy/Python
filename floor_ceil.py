def calculate_within_bmi_range(height):
    """
    Given a person's height (in inches), the function returns
    a tuple containing the healthy BMI weight range. The range should be an integer.
    Round up the lowest value range and round down for the highest value.

    The function MUST raise a ValueError type exception if the height is less than
    or equal to zero.
    """
    import math
    
   
    height=float(height)
    if height <=0:
        raise ValueError
    low=(19 * height**2 )/ 720
    high=(25 * height **2) / 720
    tup=(math.ceil(low),math.floor(high))
    return(tup)


x=calculate_within_bmi_range(5.0*12)
print(x)

print (4%2)
