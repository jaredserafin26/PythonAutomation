it = 10

while it>1:
    if it == 9:
        it = it - 1
        continue #will skip specific iteration step / skip 9
    if it == 3:
        break #use for skipping value in while loop
    print(it)

    it = it - 1 #without this condition the loop will be infinite displaying 4

print("while loop execution is done")
