greeting = "Good Morning"
a = 4

#if greeting = "Good Morning":
if a > 2:
    print(" Condition Matches")
else:
    print("Condition do not match")

print("if else condition code is completed")

#for loop
obj= [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# sum of first natural numbers 1+2+3+4+5 = 15
#range(i,j) -> i to j-1
summation = 0
for j in range(1, 6): #for(i=0;i<5;i++)
    summation = summation + j # 0+1 = summation=1, 1+2 = summation = 3, 3+3 = summation=6, 6+4 = summation=10, 10+5 = summation = 15
print(summation)

print("******************************************")
for k in range(1, 10, 5): #gin set 1, 10, 5. Ma display numbers sugod sa 1 + 5 = 6 output: 1 6
    print(k)
print("*****************************SKIPPING FIRST INDEX*************************")

for m in range(10): #ma display 0 1 2 3 4 5 6 7 8 9
    print(m)




