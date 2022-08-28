# type casting 

a = "30.55"
#typecasting 30.55 from string to float

a = float(30.55)

print(type(a))


# converting b from string to int
b = "55"
b = int(b)
print(type(b))

c = 55.88
c = str(c) # or str(55.88)
print(type(c))

#this is invalid because "55thdkrh" cant be converted to int
#b = "55thdkrh"
#b = int(b)
#print(type(b))