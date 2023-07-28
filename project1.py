weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    print(f"you are {weight * 0.45} Kilos")
elif unit.upper() == "L":
    print(f"you are {weight / 0.45}  Pounds")
else:
    print("Enter Valid unit")
