""" ========
::: Classes;
======== """

class pipe: # Pipe stream class
    def __init__(self, function, *args, **kwargs):
        self.function = function
        self.args     = args
        self.kwargs   = kwargs

    def __call__(self, *predicates): # Rebuild pipe with arguments.
        return pipe (
            self.function, *(predicates + self.args), **self.kwargs
        )

    def __pow__(self, other): # Used to match right-associative expressions.
        return self.function(other, *self.args, **self.kwargs)

    def __ror__(self, other): # Used to match left-associative expressions.
        return self.function(other, *self.args, **self.kwargs)

class app: # Applicative
    def __init__(self, function, *args, **kwargs):
        self.function = function
        self.args     = args
        self.kwargs   = kwargs

    def __call__(self, *args, **kwargs):
        return self.function (*(args + self.args), **(kwargs | self.kwargs))

    def __and__(self, argument): # Apply argument to functiion
        return self.function (argument, *self.args, **self.kwargs)

    def __xor__(self, argument): # Apply function as argument
        return self.function (argument, *self.args, **self.kwargs)

""" ==========
::: Functions;
========== """

square           = lambda n: n * n
is_even          = lambda n: n % 2 == 0
is_odd           = lambda n: n % 2 != 0
is_positive      = lambda n: n > 0
is_negative      = lambda n: n < 0

plus             = app(lambda static: lambda dynamic: dynamic +  static)
minus            = app(lambda static: lambda dynamic: dynamic -  static)
times            = app(lambda static: lambda dynamic: dynamic *  static)
power_of         = app(lambda static: lambda dynamic: dynamic ** static)
equals           = app(lambda static: lambda dynamic: dynamic == static)
not_equals       = app(lambda static: lambda dynamic: dynamic != static)
greater_than     = app(lambda static: lambda dynamic: dynamic >  static)
greater_or_equal = app(lambda static: lambda dynamic: dynamic >= static)
less_than        = app(lambda static: lambda dynamic: dynamic <  static)
less_or_equal    = app(lambda static: lambda dynamic: dynamic <= static)
contains         = app(lambda static: lambda dynamic: static in dynamic)

name             = app( lambda property  : 
                   app( lambda predicate : 
                        lambda object    : 
                            predicate(object[property]) if property in object else False ))

@pipe
def head (element):
    return element[0]

@pipe
def tail (element):
    return element[1:]

@pipe
def reverse (elements):
    return elements[::-1]

@pipe
def apply (elements, function): # Basically `map'
    return [
        function (element) for element in elements
    ]

@pipe
def where (elements, predicate):
    return [
        element for element in elements if predicate (element)
    ]

@pipe
def select (elements, *keys):
    
    overral = [ ]
    for element in elements:
        
        current = { }
        for key in keys:
            current |= ({ key: element [key] } if key in element else { })

        overral.append(current)

    return overral

@pipe
def get (elements, key):
    return [ 
        element [key] for element in elements if key in element 
    ]

@pipe
def find (elements, predicate):
    index = 0

    for element in elements:
        if predicate (element):
            return (index, element)

        index += 1

    return (None, None)

@pipe
def sum (elements):
    result = 0

    for element in elements:
        result += element
    
    return result

@pipe
def even (elements):
    return elements | where (is_even)

@pipe
def odd (elements):
    return elements | where (is_odd)
