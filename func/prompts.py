from func.clearfunc import clear
import func.calculations as calc
from time import sleep

def reject(x = ""):
    clear()
    print(x)
    sleep(1)
    return False

def askmoney():
    print("How much money would you like to earn?")
    x = input("Enter: ")
    try:
        x = float(x)
        return x
    except ValueError:
        reject("Must be an integer or float")

def asktp():
    print("How long would you like to wait?")
    print("Hours : h, Minutes : m, Seconds : s")
    x = input("Enter: ")
    if x.lower() not in ['h','m','s']:
        return reject("Must specify unit of time")
    clear()
    print("How long would you like to wait?")
    match x.lower():
        case 'h':
            x = "hours"
        case 'm':
            x = "minutes"
        case 's':
            x = "seconds"
    y = input(f"Enter in {x}: ")
    try:
        y = float(y)
        if x == 'hours':
            return calc.hourstoseconds(y)
        if x == 'minutes':
            return calc.minutestoseconds(y)
        if x == 'seconds':
            return y
    except ValueError:
        return reject("Must be an integer or float")
    
def askgen():
    print("How much do the generators generate?")
    x = input("Enter: ")
    try:
        x = float(x)
        return x
    except ValueError:
        return reject("Must be an integer or float")

def asklong():
    print("How long do they take to generate the amount (UNIT)")
    print("Hours : h, Minutes : m, Seconds : s")
    x = input("Enter: ")
    if x.lower() not in ['h', 'm', 's']:
        return reject("Must specify unit of time")
    clear()
    print("How long do they take to generate the amount")
    match x.lower():
        case 'h':
            x = "hours"
        case 'm':
            x = "minutes"
        case 's':
            x = "seconds"
    y = input(f"Enter in {x}: ")
    try:
        y = float(y)
        if x == 'hours':
            return calc.hourstoseconds(y)
        if x == 'minutes':
            return calc.minutestoseconds(y)
        if x == 'seconds':
            return y
    except ValueError:
        return reject("Must be an integer or float")
    
def askcost():
    print("How much do the generators cost?")
    x = input("Enter: ")
    try:
        x = float(x)
        return x
    except ValueError:
        return reject("Must be an integer or float")