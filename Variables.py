#String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'


#Case-Sensitive
#Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a


u = 5
y = "John"
print(u, y)


#Example
b = 10   # global variable

def show():
    print(b)

show()
print(b)



#Changing Global Variable
c = 10

def change():
    global c
    c = 20

change()
print(c)