File list
====

-   wraps.py - usage of \@wraps and decorator
-   wrapsmultilayer.py - multilayer decorator (2 layer most)
-   wrapswithparms.py - give more parms for a decorator
-   partialtest.py
-   wrapsattachattr.py



Decorator
====

[Non-Complete Thinking (Jerry Chou)](http://www.cnblogs.com/Jerry-Chou/archive/2012/05/23/python-decorator-explain.html)

```python
def wrapper_func(func):

    def __decorator():
        do_something()
        return func()

    return __decorator


def func():
    do_something()
func = wrapper_func(func)

func() # == wrapper_func(func)()

@wrapper_func
def func():
    do_something()

```

func with some parm (\*args, \*\*kwargs)

```python
def wrapper_func(func):

    def __decorator(parm):
        do_something()
        return func(parm)

    return __decorator

@wrapper_func
def func(parm):
    do_something()

[decorated]func(parm) => wrapper_func(func)(parm) => __decorator(parm) => [real]func(parm)

```

wrapper_func with some parm

```python
def wrapper_func_parm(wrapper_parm)

    def wrapper_func(func):

        def __decorator(parm):
            do_something(wrapper_parm)
            return func(parm)

        return __decorator

    return wrapper_func

@wrapper_func_parm(wrapper_parm)
def func(parm):
    do_something()

1. wrapper_func_parm(wrapper_parm) will be performed and return a wrapper "wrapper_func(func)"
2. [decorated]func(parm) => wrapper_func(func)(parm) => __decorator(parm) => [real]func(parm)

```
