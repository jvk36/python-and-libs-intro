height = float(input("Height in meters: "))
weight = float(input("Weight in Kilos: "))
if height > 3:
    raise(ValueError("Height should not be greater than 3 meters."))
bmi = weight / height ** 2
print(bmi)
