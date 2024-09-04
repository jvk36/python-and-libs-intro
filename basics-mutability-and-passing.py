# BASIC TYPES ARE IMMUTABLE, THE REST ARE MUTABLE
print ("BASIC TYPES ARE IMMUTABLE, THE REST ARE MUTABLE")

# BASIC TYPES ARE IMMUTABLE (str, int, float, bool, tuple) 
print("\nBASIC TYPES ARE IMMUTABLE (str, int, float, bool, tuple)")
print("\nOPERATIONS ON THEM RETURNS A NEW OBJECT")
print(f"\nEXAMPLE: str operations: {dir('')}")

# THE REST ARE MUTABLE (list, set, dict, 3rd party types, etc.)
print("\nMUTABLE TYPES (list, set, dict, 3rd party types, etc.)")
print("\nOPERATIONS ON THEM RETURNS OBJECTS or CAN BE INPLACE")
print(f"\nEXAMPLE: dict operations: {dir({})}")

# PASSING IS ALWAYS BY REFERENCE
print("\nPASSING IS ALWAYS BY REFERENCE:")
# PASSING IMMUTABLE TYPES
print("\nPASSING IMMUTABLE TYPES:")
s = "John"
print(f"s before function call: {s}")
def use_s(a):
    a = a.upper()
    print(f"Pass by reference Value Inside Function (Immutable Types, Local Variable Created): {a}")
use_s(s)
print(f"s after call: {s}. Pass by reference but does not change value as it is immutable")

# PASSING MUTABLE TYPES
print("\nPASSING MUTABLE TYPES:")
l = [1, 2, 3, 4]
print(f"l before function call: {l}")
def change_l(a):
    a.append(5)
    print(f"Pass by reference Value Inside Function (Mutable Type, changed): {a}")
change_l(l)
print(f"l after call: {l}. Pass by reference does change value as it is mutable")
