#Different methods to write strings

name = "My name is Gaurav"
print(name)



# to print string with spaces and different lines
Name = '''My name is 
                        Gaurav singh \n'''
print(Name)



# to print only one character of string 
st ="Gaurav"
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])



#this prints all elements from 0 to 6 
print(st[0:6] ,"\n")



#this prints all elements of name from 0 to 10 
print(name[0:10] ,"\n")



# to remove extra spaces at end and start from string
a =  "       Gaurav    singh       "
print(a.strip() ,"\n")


# to find length of string
print(len(name) ,"\n")  # name = "My name is Gaurav"



#To convert whole string into upper or lower case (we use string 'name')
b = name.lower()
print(b)
b = name.upper()
print(b  ,"\n")


#to replace alphabets in string
c = "Gaurav , singh" # This is a string

d = c.replace("a","A")
print(d)


d = c.replace("au","A")
print(d ,"\n")


d = c.replace(",","\n")
print(d)


# to add two strings 
k = "Gaurav"
l = " Singh"
print("\n",  k+l)

