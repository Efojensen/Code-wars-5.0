#A python program to take as input a string of characters and divide them into 
#strings of length 2 each.
#Should the original string length be odd, an underscore sign shall be used to replace 
#the last character that should have been there

original = input("Enter in a string: ")

collection = []

i = 0

if original.__len__() % 2 == 0:
    while i < original.__len__():
        while i < original.__len__():
            collection.append(original[i] + original[i + 1])
            i += 2
            break
# We have managed to succesfully split any string into 2. Now for the else part, 
# It's just copying and pasting ;-)
else:
    original += "_"
    while i < original.__len__():
        while i < original.__len__():
            collection.append(original[i] + original[i + 1])
            i += 2
            break


print(collection)

# Et voila!! That took a while...
# I finally got it to work. I've been sitting here for about an hour. Make that two hours and 45 minutes :-)



