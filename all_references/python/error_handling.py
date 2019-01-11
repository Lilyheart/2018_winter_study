def sqrt(radicand):
    """Returns the square root of a number"""
    try:
        if(radicand < 0):
            raise ValueError("radicand must be non-negative")
        return radicand ** 0.5
    except TypeError:
        print("the radicand must be an int or float")


sqrt(25)
sqrt("this is an error")
sqrt(-9)

####
# Error Types
####

IndexError
TypeError
