"""
x = "Fantastic "
def myfunc():
    print('python is ' + x)
    print ("Python is not " + x)
myfunc()

print('please tell us your opinon on both statments')
"""
temperature = input("temperature:")
if int(temperature) >= 20 and int(temperature) <= 30:
    print("Its a best day in recent times ")
    print("just go out and have fun")
    
elif int(temperature) > 30:
    print("its hot, drink more water")
    
elif int(temperature) <= 15 and int(temperature) >= 10:
    print("its a nit chilly out there1")
    print("better to take a jacket when you go out")
    
else:
    print("its cold! should wear a sweater along with jacket when we go out")
    
    
