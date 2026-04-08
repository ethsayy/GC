import func.calculations as calc
import func.prompts as prompts
from func.clearfunc import clear

h = "GC (GENERATOR CALCULATOR)"

print(h)
a = prompts.askmoney()
while a == False:
    clear()
    print(h)
    a = prompts.askmoney()
clear()
print(h)
b = prompts.asktp()
while b == False:
    clear()
    print(h)
    b = prompts.asktp()
clear()
print(h)
c = prompts.askgen()
while c == False:
    clear()
    print(h)
    c = prompts.askgen()
clear()
print(h)
d = prompts.asklong()
while d == False:
    clear()
    print(h)
    d = prompts.asklong()
clear()
print(h)
e = prompts.askcost()
while e == False:
    clear()
    print(h)
    e = prompts.askcost()
clear()
print(h)
x = calc.amountofgen(a,b,c,d)
y = calc.costofgen(x,e)
print(a,b,c,d)
print(f'NUMBER OF GENERATORS NEEDED: {x} generators')
print(f'COST OF TOTAL GENERATORS: {y}')
input()
exit()