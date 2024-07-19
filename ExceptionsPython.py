
ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:     #raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0) # this is how you can fail test if condition is not met / expects condition / condition is always true, if condition is not true the test will fail


#Try catch=exept method
try:
    with open('test1.txt', 'r') as reader:
        reader.read()
        print("Success")
except:
    print("Some how i reached this block because there is failure")


try:
    with open('test.txt', 'r') as reader:
        reader.read()
        print("Success")

except Exception as e: #python generated error = [Errno 2] No such file or directory: 'test123.txt'
    print(e)

finally: #use to cleanup data / delete try except data/records/cookies
    print("cleaning up resources")
