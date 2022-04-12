# The pipe class
The pipe class is a wrapper class to facilitate the implementation of 'pipeable' functions (a.k.a. `fn1 | fn2`, "Pass the output of 'fn1' to 'fn2'").

To implement your own pipeable functions, is a very easy process, just:
```python
from pipe import pipe
```

Then decorate your function with `@pipe`:
```python
@pipe
def my_fun(...):
    ...
```
The only rule here is that the first argument will be the input of the pipe, such as:
```python
1 | fn == fn(1)
```
You  may recognize this pattern, because it is the exact same thing as a class calling a method, which it's first argument is `self` (`method(self) == self.method()`).

Now, if you're still not sure how to use it, let's implement a simple sum function to add all elements of a list, the implementation is as it follows:
```python
def sum(elements):
    result = 0
	
    for element in elements:
	result += element
    
    return result
```
Do you see how simple the implementation is? It is just a common sum function, like everybody would implement. The catch here, is that adding the `@pipe` decorator, let's you pass the first argument in a pipe form, so, let's do that:
```python
@pipe
def sum(elements):
    result = 0
	
    for element in elements:
	result += element
		
    return result
```
After adding the decorator, you may now use both forms of calling the function, as both will work:

Pipe form:
```python
[1, 2, 3, 4, 5] | sum # 15
```
Normal form:
```
sum([1, 2, 3, 4, 5]) # 15
```
And finally, you can enjoy the power of the pipes. Let's see another example, in both forms, let's say I want to sum all of the even numbers in a list:
```python
# We will be using the sum function defined above to save typing.
# So I'll just define the 'even' function.

@pipe
def even(elements):
    return [ element for element in elements if element % 2 == 0 ]
	
# This is how you would call it normally:
sum(even([1, 2, 3, 4, 5]))

# This is how you call it with pipes:
[1, 2, 3, 4, 5] | even | sum
```
Much easier, isn't it?

# The app class (applicative)
The app class is a wrapper for curried functions to be partially applied with a custom syntax.

To create an app function, just wrap it in the `app` class, just make sure to know, that this only works for curried functions that have two or more levels of curry (Function needs atleast two arguments). You'll may have to wrap all function returns, except the last one. If you're still not sure what all of this means, let's take a look at some implementations:
```python
# Boring function, with boring calling syntax.
add = lambda a: lambda b: a + b

# If you wish to partially apply this function, you'll do something like this:
add_1 = add (1)

# But now, with the app wrapper:
add = app(lambda a: lambda b: a + b)

# You may use this style of partially application, using the & symbol to feed in the argument:
add_1 = add& 1

# And if you need to feed in another function as argument, while you're feeding it also, use the ^ to feed the argument, instead of the &.
fn = fn_a& arg_a ^ fn_b& arg_b

# The code above is the same as:
fn = fn_a(arg_a, fn_b(arg_b))
```
Easier to write, and easier to read.
