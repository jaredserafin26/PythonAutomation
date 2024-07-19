str = "Jared.com"
str1 = "Consulting firm"
str3 = "Jared"

print(str[0]) #a from J=0 a=1 r=2 e=3 d=4

print(str[0:5]) #print "Jared"

print(str+str1) # concatenation of 2 string

print(str3 in str) #validation if string value of str3 is present in str / substring check

# split string value of variable str
var = str.split(".") # seperate jared.com using "." do it display as Jared com
print(var) #Jared com
print(var[0]) #will get the index of seperad value 0=Jared 1=com

str4 = " great "
print(str4.strip()) #removing white space from str4

print(str4.lstrip()) #remove left whitespace from str4

print(str4.rstrip()) #remove right whitespace from str4