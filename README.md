# Secant-and-Newton-Raphson's-method:
this repository will demonstrate how to implement Secant and Newton-Raphson's methods with Python

# Secant-Method - quick reveiw:
The Secant method is an iterative method for finding the roots of a continuous function of one variable.

This method is similar to the Newton-Raphson method for finding roots. In the Newton-Raphson method it is necessary to derive the function at the last point. The string method brings the derivative closer by the slope of the string that connects the last two points calculated, hence its name. The convergence order of the method is lower than that of the Newton-Rapson method: in the Newton-Rapson method the order is 2, while in the string method, the order is the golden ratio (about 1.618). The advantage of the string method is that it does not use a derivative: if the derivative is unknown, or its calculation consumes many computational resources, the string method converges faster.

# Calculate Xr+1:</br>
![Xr+1](https://i.ibb.co/D1J6p4q/secant.jpg)
</br></br>


# Newton-Raphson's-method - quick reveiw:
The Newton-Raphson method - is an efficient algorithm in numerical analysis, for finding the roots of any real function, i.e. points where the function is reset.
When we are given a function and we are looking for the roots of the equation in a domain where the function has only one root,
If a point close to the root is selected, the root of the tangent to the function at that point will be closer to the root we are looking for.
With each iteration of the loop, a better and better approximation is obtained.
it is a good method when we know the derivative of the function.</br>

# The Newton Rapson method is:
1 Guess a point close to the desired root.</br>
2 Calculate the slope of the tangent to the function at this point,
  This is the derivative of the function at that point.</br>
3 Calculate the tangent equation.</br>
4 Find the tangent root, i.e. the point where the tangent intersects the x-axis.</br></br>

# Calculate Xr+1:</br>
![Xr+1](https://i.ibb.co/zrQw6kC/new.jpg)



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sympy and Texttable.

```bash
pip install sympy
```

```bash
pip install Texttable
```

## Contributing
I built the algorithm in the form of object-oriented programming, in order to simplify the idea behind it. <br/>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

