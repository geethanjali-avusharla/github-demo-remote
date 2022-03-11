# Add implementation1
def add(x,y):
    return x+y;
# Subtract implementation1
def subtract(x,y):
    return x-y            #on master
# multiply implementation1
def multiply(x,y):
    return x*y          #on bug456
# divide implementation1
def divide(x,y):
    if y==0:            #on master
        return DIVIDE_BY_0_ERROR;
    else:
        return x/y

#square implntn1
def square(x):
    return x*x

