fullName = "Lil Nacheaux"
age = 4

myArray = []
myArray.append(fullName)
myArray.append(age)
print myArray

def sayHello():
    print "Hello!"
sayHello()

splitName = fullName.split(" ")
print splitName

def sayName():
    print "Hello, %s!" % splitName[0]
sayName()

def myAge():
    born = 1982
    year = 2018
    print year - born
myAge()

def sumOdd():
    odd = []
    for i in range(1,20,2):
        odd.append(i)
    sum = 0
    for num in odd:
        sum += num
    print odd
    print sum
sumOdd()