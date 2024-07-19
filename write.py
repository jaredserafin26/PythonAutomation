#alternative file = open('test.txt') without file.close() syntax / recommended
# 'r' = read, 'w' = write
#read the file and store all the lines in list
#revers the list
# write the list back to the file

with open('test.txt', 'r') as reader: #open ang test.txt
   content = reader.readlines() #holds the list of all the items present on test.txt [abc, bvdsaf, cat, dog, elephant]
   reversed(content) # [elephant, dog, cat, bvdsaf, abc]
   with open('test.txt', 'w') as writer:
       for line in reversed(content):
            writer.write(line)