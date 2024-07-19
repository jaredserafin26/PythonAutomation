#create list /array in other language
values = [1, 2, "jared", 4, 5]
# List is data type that allows multiple values and can be different data types

#value present in 1st index
print(values[0]) #1

print(values[3]) #4

print(values[-1]) #5 refers to the last index on the lists

print(values[1]) #2

print(values[2]) #jared

print(values[1:3]) #jared / the last index will not be printed / [2, 'jared']

values.insert(3,"serafin") #insert/inject new value on list data type
print(values) #[1, 2, 'jared', 'serafin', 4, 5]

values.append("End") #new value on the lists
print(values) #[1, 2, 'jared', 'serafin', 4, 5, 'End']

values[2] = "REDSCAR" #Updating
print(values)

del values[0] #Deleting
print(values)


#TUPLE - same as list data type but immutable / updation is not possible
val = (1, 2, "jared", 4.5)

print(val[1])
#val[2] = "RED" #invalid / change array to lists if you want to update
#print(val)

#DICTIONARY
dic = {"a": 2, 4:"bcd", "c": "Hello World"}
print(dic[4])
print(dic["c"])
print(dic["a"])

#create diction dynamically at run time / insert values on empty array
dict = {}

dict["firstname"] = "Jared"

dict["lastname"] = "Serafin"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])
