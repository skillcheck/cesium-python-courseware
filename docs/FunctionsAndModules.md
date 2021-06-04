## Organizing into Functions and Modules

This lesson is the first step beyond the basic low level language features of Python. Here we will look at dividing up the code into functions and modules. We will also take the first steps into non-linear process flow. These will form the basis for large(r)-scale software development.

Up until now, you have been learning the basic features of the Python language such as variables, conditionals, loops, etc. These of course are very useful for the detailed part of writing software. For this, all the code was written in a single file and all the contents were executed from start to finish and then the program exited. In the previous lesson, the program essentially did the following:

1. Give the user a description of what the program did (using ```print()``` statements)
2. Asked the user to enter data (using the ```input()``` function)
3. Processed the data (by splitting the input into an array and performing calculations)
4. Exit

This is sometimes referred to as "sequential" or "linear" programming. Everything happens in the order that is stated in the code.

For larger-scale programs however, you can imagine that there may be pieces of code that you want to reuse (you don't want to write the same thing over and over again for each new project do you?). For example, although the calculations were simple in the previous lesson, they could be much more complicated in a real project and you may want to reuse them in other projects. For this we will place those calculations in a *function* definition. If we save this to a separate file, it can be included in other projects.

Furthermore, you may want to give the user the option to do a new calculation with new values without having to exit and restart the program each time. For this, we will give the user a list of options to choose from and then perform actions based on what they enter.

### Creating a function

