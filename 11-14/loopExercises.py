# # Capitalize a string
# word = "Hello"
# print word.upper()
# print word.capitalize()
# reverseString = word[::-1]
# print reverseString

# paragraph = "agdjaeotugfmasdgasotuwqrgoihtfwertmbysdfyykljsdry"
# myString = paragraph.upper()
# replacements = ["A", "4"], ["E", "3"], ["G", "6"], ["I","1"],["O", "0"], ["S","5"],["T","7"]
# for old, new in replacements:
#     myString = myString.replace(old,new)
# print myString

# vowels = "AaEeIiOoUu"
# numVal = 0
# vSet = set(vowels) #set transforms to a list (array, etc.) which cannot be changed
# rendWord = []
# impWord = raw_input("Please enter a word: ")
# for i in impWord:
#     if i in vSet:
#         numVal += 1
#         rendWord.append(i)
#         if numVal == 2:
#             rendWord.append((i)*3)
#     else:
#         numVal == 0
#         rendWord.append(i)
# wordRendered = "".join(rendWord)
# print wordRendered




# alphabet = "abcdefghijklmnopqrstuvwxyz"
# cipher = "lbh zhfg hayrnea jung lbh unir yrnearq"
# cipherList = list(cipher)
# decode = []
# for i in range(0,len(cipherList)):
#     for i in cipherList:
#         letter = alphabet[(len(alphabet[i]))-1]
#         decode.append(letter)
#     print decode

#strings

# for i in range(1,11):
#     print i   

# start = input("Starting Number?")
# end = input("End Number?")
# finalEnd = (end + 1)
# for i in range(start, finalEnd):
#     print i


# for i in range(0,11):
#     if i % 2 != 0:
#         print i

# i = 5
# while(i>0):
#     print "*****"
#     i = i - 1

# N = input("What are the dimensions of your square?")
# i = N
# star = N
# while (i>0):
#     print "*" * star
#     i = i-1

# width = input("width?")
# length = input("length?")
# visualLength = (length - 2)
# visualWidth = int(width) - 2
# print "*" * width
# while (visualLength > 0):
#     print "*" + (" " * visualWidth) + "*"
#     visualLength = visualLength - 1
# print "*" * width

# #Triangle Height
# height = input("height of triangle?")
# x = 1
# space = (height - 1)
# for i in range (0, height):
#     print (" " * space) + ("*" * x)
#     x = x + 2
#     space = space - 1

# #Triangle Width
# p = int(raw_input("Input width: "))
# p = p + 1
# for i in range (1,p,2):
#     print ("-"*p) + (i*"*")
#     p -=1

text = raw_input("Enter Text Here?")
stars = len(text) +2
print "*" * stars
print "*"+text+"*"
print "*" * stars

#List

# list = [1,2,3,4,5,6,7,8]
# print list.pop()
# print list.pop(0)

# for i in list:
#     if i % 2 == 0:
#         print i

# for j in list:
#     if j % 2 != 0:
#         print j

# list2 = [-1,-2,-4,-5,1,2,4,5]
# List3 = []
# for i in list2:
#     if i > 0:
#         List3.append(i)
# print List3 
        
# duplicates = [1,2,3,4,3,2,5,6,7,8,9,4,3,2,1,]
# newList = []
# for i in duplicates:
#     if i not in newList:
#         newList.append(i)
# print sorted(newList)        

# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = []
# for i in range(0,len(list1)):
#     list3.append(list1(i) * list2(i)) 
# print list3
    
