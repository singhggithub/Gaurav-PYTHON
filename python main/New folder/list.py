# list is like array for numbers 

list = [ 95,2,99,55,5]
var = type(list)
l = list[0]
ll = list[0:3]


print(var)
print(list)
print(ll)
print(l)

#to change element in list
list[3] = 444
print(list)
print(len(list)) #length of list

list.append(999) # append function add the number at end of the list
print(list)  

# to inert at any index
list.insert(4,87)
print(list)

# to remove 

del list[5]
print(list)

list.remove(999)
print(list)

list.clear()
print(list)



# ctrl / (to comment and uncomment)
# alt up or alt down (to move up or down)