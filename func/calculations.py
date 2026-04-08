def hourstominutes(x):
    if type(x) not in [int,float]:
        print("hourstominutes must only contain an integer as an argument.")
        return
    return x*60

def hourstoseconds(x):
    if type(x) not in [int,float]:
        print("hourstoseconds must only contain an integer as an argument.")
        return
    return x*3600

def minutestoseconds(x):
    if type(x) not in [int,float]:
        print("minutestoseconds must only contain an integer as an argument.")
        return
    return x*60

def amountofgen(a,b,c,d):
    return ((a*d)/(c*b))

def costofgen(x, e):
    return x*e