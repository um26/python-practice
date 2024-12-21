weight = float(input("weight: "))
unit = input("K(g) or L(bs): ")
if(unit == "K"):
    weight *= 2.2
    print(weight)
elif(unit == "L"):
    weight /= 2.2
    print(weight)
else:
    print("wrong unit")