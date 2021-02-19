import math
import sympy as sy
from texttable import Texttable

x = sy.symbols("x")


def CreateFunction():  ## step 1 - choose a polynom
    ##fast example   x**4+x**3-3*x**2
    funcInput = input("Enter a function: ")
    func = sy.sympify(funcInput)
    return func


def CreateBoundry():  ## step 2 - choose an a and b
    a = 0
    b = 0
    while a >= b:
        print("\nA Note: A < B")
        a = float(input('please choose boundary A: '))
        b = float(input('please choose boundary B: '))
    return [a, b]


def CreateEpsilon():  ## step 3 - choose an epsilon
    return float(input("please choose an Epsilon: "))


def NewtonRaphson(f, derF, boundary, epsilon):
    a = boundary[0]
    b = boundary[1]
    count = 1  # iteration count
    xr = (a + b) / 2  # initial guess
    table = Texttable()
    table.set_precision(10)
    rows = [["f'(x)", "f(x)", "Xr", "i"]]
    print()
    print("The Newton-Raphson table is:")
    while abs(f.subs(x, xr)) > epsilon and count < 500:  # iterate until f(x)>epsilon or count=500
        rows.append([derF.subs(x, xr), f.subs(x, xr), xr, count])
        xr = xr - (f.subs(x, xr) / derF.subs(x, xr))  # formula
        count = count + 1
    table.add_rows(rows)
    print(table.draw())
    return xr


def SecantMethod(function, boundery, epsilon):
    # example: x**3 - cos(x)
    count = 1
    xr = boundery[0]
    xr1 = boundery[1]
    temp = xr
    table = Texttable()
    table.set_precision(10)
    print("Secant method:\n\n")
    rows = [['f(x)', 'xr1', 'xr', 'i'], [function.subs(x, xr), xr1, xr, count]]
    while abs(xr1 - temp) > epsilon and count < 500:  # iterate until f(x)>epsilon or count=500
        count += 1
        temp = xr
        xr = xr1
        a = temp * function.subs(x, xr1)
        b = xr1 * function.subs(x, temp)
        c = function.subs(x, xr1)
        d = function.subs(x, temp)
        xr1 = (a - b) / (c - d)
        rows.append([function.subs(x, xr), xr1, xr, count])
    table.add_rows(rows)
    print(table.draw())
    return xr1


def StartIterating(function, boundry, epsilon, methodSelection):
    difference = 0.1
    a = boundry[0]
    b = boundry[1]
    count = 0
    prev = 0
    current = 0
    roots = []
    sus = []  # suspicious - may be roots
    table = Texttable()
    table.set_precision(10)
    rows = [['f(x)', 'x', 'i']]
    print(f'The difference is {difference}')
    print()
    while a <= b + 0.0001:
        count = count + 1
        y = function.subs(x, a)
        rows.append([str(y), str(a), str(count)])
        if count != 1:
            prev = current
        current = y
        if (current < 0 and prev > 0) or (current > 0 and prev < 0):  # sign change
            sus.append((a - difference, a))
        a = a + difference
    table.add_rows(rows)
    print(table.draw())
    print()
    table = Texttable()
    table.set_precision(10)
    xList = [["  ", "x1", "x2"]]
    rowsNum = 0
    if len(sus)==0:
        print("There are no roots for this table")
    else:
        print(f"The suspicious cutting roots are: ")
        for i in sus:
            rowsNum = rowsNum + 1
            xList.append([rowsNum, i[0], i[1]])
    table.add_rows(xList)
    if len(sus)!=0:
        print(table.draw())
    print()
    if methodSelection == 1:
        for i in sus:
            ans = NewtonRaphson(function, FindDerivative(function), [i[0], i[1]], epsilon)
            roots.append(ans)
    else:
        for i in sus:
            ans = SecantMethod(function, [i[0], i[1]], epsilon)
            roots.append(ans)
    return roots


def FindDerivative(function):
    derivative = sy.diff(function, x)
    return derivative


def FindSolution(function, boundry, epsilon, methodSelection):
    roots = StartIterating(function, boundry, epsilon, methodSelection)
    derivative = FindDerivative(function)
    deriRoots = roots + StartIterating(derivative, boundry, epsilon, methodSelection)
    for dr in deriRoots:
        if (function.subs(x, round(dr)) == 0):
            roots.append(round(dr))
    print()
    if len(roots) == 0:
        print("There are no roots")
    else:
        print(f'The roots are: {roots}')


print("Choose the methode you want to use: ")
print("1- Newton-Raphson             2 - Secant Method")
methodSelection = input()  # this flag will change the mothod according to the user choises
while methodSelection not in ['1','2']:
    print("You can choose only one or two")
    print()
    print("Choose the methode you want to use: ")
    print("1- Newton-Raphson             2 - Secant Method")
    methodSelection=input()
f = CreateFunction()
b = CreateBoundry()
e = CreateEpsilon()
FindSolution(f, b, e, int(methodSelection))
