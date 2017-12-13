import inspect
import functools


def linenumber(func):
    @functools.wraps(func)
    def linenumber_wrap(*args, **kwargs):
        previous_frame = inspect.currentframe().f_back
        filename, line_number, function_name, lines, index = \
            inspect.getframeinfo(previous_frame)

        # loop for parameters
        signature = inspect.signature(func)  # signature needs python3.6
        parameters = []
        i = 0
        for name, param in signature.parameters.items():
            paramstr = name + '='
            if (i < len(args)):
                paramstr += str(args[i])
            elif name in kwargs:
                paramstr += str(kwargs[name])
            if param.default != inspect._empty:
                paramstr += '(default:' + str(param.default) + ')'
            parameters.append(paramstr)
            i += 1

        print(
            '>>> %s(%s) is called at [%s:%d]' %
            (func.__name__, parameters, filename, line_number))
        res = func(*args, **kwargs)
        return res
    return linenumber_wrap
