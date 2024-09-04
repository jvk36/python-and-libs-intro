import builtins

# BUILTINS CAN BE CALLABLE OR NOT
print("CALLABLE BUILTINS:")
builtin_functions = [name for name, obj in vars(builtins).items() if callable(obj)]
print(builtin_functions)


# print("CALLABLE BUILTINS WITH DESCRIPTION (first line of docstring):")
# for name, obj in vars(builtins).items():
#     if callable(obj):
#         if obj.__doc__:
#             print(f"{name}: {obj.__doc__.split('.')[0]}")
#         else:
#             print(name)

print("\nNON-CALLABLE BUILTINS:")
non_callable_builtins = [name for name, obj in vars(builtins).items() if not callable(obj)]
print(non_callable_builtins)

