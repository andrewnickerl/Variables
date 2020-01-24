f = 0 #variables don't need to be explicity typed to be assigned a value
print(f)

f='abc'
print(f)

print("string " + str(123)) #even though variables in python can be declared implicitly, it is strongly typed and won't concat a string with an int without first parsing the int

def someFunction():
    global f #specifies that f is the global variable declared earlier, not only local to someFunction()
    f="def"
    print(f)

someFunction() 

del f
print(f) #won't run because previous line deletes f

