def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return a / b

result = function_with_uncommon_error(0, 0)
print(result) # This will raise an error, but maybe not the one you expect.