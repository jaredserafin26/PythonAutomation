file = open('test.txt')

#Read all the contents of file
#print(file.read(5)) #will read 2 characters in test.txt / #read n number of characters by passing parameter

#read one single line at a time readLine()
#print(file.readline())
#print(file.readline())

#file.close()

#Print line by line using readLine method
#line = file.readline()

#while line!= "": # diri mkdto ang na fetch na unod ka txt file
#    print(line) # ma print
#    line = file.readline() #will check mag print line sa sulod ka txt file

#values = [abc, bvdsaf, cat, dog, elephant]
for line in file.readlines(): #will print all txt file using for loop like list
    print(line)

file.close()